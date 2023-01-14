from typing import Optional

from pydantic import BaseSettings, Field

API_KEY_DOCS_URL = "https://beta.openai.com/account/api-keys"


class OpenAiSettings(BaseSettings):
    api_key: Optional[str] = Field(
        None,
        title="OpenAI API Key",
        description=f"Can be created at {API_KEY_DOCS_URL}",
        env="OPENAI_API_KEY",
    )
    model: str = Field("text-davinci-003", env="OPENAI_MODEL")
    max_tokens: int = 100


class RandomEmojiSettings(BaseSettings):
    unicode_version: int = 6


class Settings(BaseSettings):
    openai: OpenAiSettings = Field(
        title="OpenAI Settings", default_factory=OpenAiSettings
    )
    random: RandomEmojiSettings = Field(
        title="Random Emoji Settings", default_factory=RandomEmojiSettings
    )


def persist_settings(settings: Settings):
    pass
