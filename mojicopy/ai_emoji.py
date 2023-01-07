import openai

from mojicopy.settings import OpenAiSettings


def ai_emoji(prompt: str, settings: OpenAiSettings) -> str:
    print("Here")
    response = openai.Completion.create(
        model=settings.model,
        prompt=f"""What are single emojis describes best the title "{prompt}"?""",
        max_tokens=settings.max_tokens,
    )
    print("got response")
    if response.choices:
        return response.choices[0].text.strip()
    raise RuntimeError("TODO: multiple attempts")
