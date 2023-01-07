import openai
import typer
import xerox

from mojicopy.ai_emoji import ai_emoji
from mojicopy.random_emoji import random_emoji
from mojicopy.settings import API_KEY_DOCS_URL, Settings, persist_settings

app = typer.Typer()


def _select_emoji(random: bool, settings: Settings) -> str:
    if random:
        return random_emoji()
    else:
        return ai_emoji(xerox.paste(), settings.openai)


@app.command()
def mojicopy(random: bool = False):
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

    emoji = _select_emoji(random, settings)
    typer.echo(emoji)
    xerox.copy(emoji)


if __name__ == "__main__":
    app()
