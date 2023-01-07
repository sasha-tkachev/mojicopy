from typing import Literal, Optional

import easygui
import typer
import xerox
from pydantic import BaseSettings, Field

from mojicopy.random_emoji import random_emoji

app = typer.Typer()

_ENVAR_KEY = "OPENAI_API_KEY"
_API_KEY_DOCS_URL = "https://beta.openai.com/account/api-keys"


class ClipboardNotification(BaseSettings):
    enabled: bool = False
    message: str = f"{_ENVAR_KEY} envar is missing"


_DEFAULT_MESSAGE = (
    f"Please configure OpenAI API key under the {_ENVAR_KEY} envar.\n"
    f"Make sure you have enough credits.\n"
    f"If you are out of credits, you can use the --random flag to generate random emojis"
    f"For more information about OpenAI API keys see {_API_KEY_DOCS_URL}\n"
)


class ConsoleNotification(BaseSettings):
    enabled: bool = True
    message: str = _DEFAULT_MESSAGE


class GUINotification(BaseSettings):
    enabled: bool = True
    message: str = _DEFAULT_MESSAGE


class NotifyUserOnMissingKey(BaseSettings):
    enabled: bool = True
    clipboard: ClipboardNotification = Field(default_factory=ClipboardNotification)
    console: ConsoleNotification = Field(default_factory=ConsoleNotification)
    gui: GUINotification = Field(default_factory=GUINotification)


class RandomFallback(BaseSettings):
    enabled: bool = True


class Settings(BaseSettings):
    openai_api_key: Optional[str] = Field(
        None,
        title="OpenAI API Key",
        description=f"Can be created at {_API_KEY_DOCS_URL}",
        env=_ENVAR_KEY,
    )

    notify_user: NotifyUserOnMissingKey = Field(default_factory=NotifyUserOnMissingKey)
    random_fallback: RandomFallback = Field(default_factory=RandomFallback)


def _notify_user_to_configure_open_ai_token(settings: NotifyUserOnMissingKey):
    assert settings.enabled
    if settings.console.enabled:
        typer.echo(settings.console.message, err=True)
    if settings.clipboard.enabled:
        xerox.paste(settings.clipboard.message)
    if settings.gui.enabled:
        easygui.msgbox("")


@app.command()
def mojicopy(random: bool = False):
    settings = Settings()
    if not random:
        if settings.openai_api_key is None:
            _notify_user_to_configure_open_ai_token(settings.notify_user)
    if random:
        typer.echo(random_emoji())
    else:

        typer.echo(random_emoji())


if __name__ == "__main__":
    app()
