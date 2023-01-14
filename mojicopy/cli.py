from typing import Optional

import openai
import typer
import xerox

from mojicopy.ai_emoji import ai_emoji
from mojicopy.random_emoji import random_emoji
from mojicopy.settings import API_KEY_DOCS_URL, Settings, persist_settings

app = typer.Typer()


def _query_prompt() -> Optional[str]:
    try:
        return xerox.paste()
    except TypeError:
        return None


def _select_emoji(
    random: bool, settings: Settings, prompt: Optional[str] = None
) -> str:
    if random:
        return random_emoji()
    else:
        if prompt is None:
            prompt = _query_prompt()
        if prompt:
            return ai_emoji(prompt, settings.openai)
        return random_emoji()


def _output_emoji(emoji: str) -> None:
    typer.echo(emoji)
    xerox.copy(emoji)


@app.command()
def mojicopy(random: bool = False, prompt: Optional[str] = None):
    if random:
        if prompt is not None:
            typer.echo("Can't generate random ai emoji from prompt", err=True)
            exit(1)
    settings = Settings()
    if not random:
        if settings.openai.api_key is None:
            api_key = typer.prompt(
                f"OpenAI API key is not configured.\n"
                f"If you are out of credits, you can use the --random flag to generate random emojis"
                f"Get your OpenAI API key here {API_KEY_DOCS_URL}\n"
                f"Please enter your API key:"
            )
            settings.openai.api_key = api_key
            persist_settings(settings)
        openai.api_key = settings.openai.api_key

    _output_emoji(_select_emoji(random, settings, prompt=prompt))


if __name__ == "__main__":
    app()
