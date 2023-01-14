import openai

from mojicopy.settings import OpenAiSettings


def ai_emoji(prompt: str, settings: OpenAiSettings) -> str:
    print("Here")
    response = openai.Completion.create(
        model=settings.model,
        prompt=f"""Give me a single emoji that describes "{prompt}"?""",
        max_tokens=settings.max_tokens,
    )
    print("got response")
    if response.choices:
        return response.choices[0].text.strip()
    raise RuntimeError("TODO: multiple attempts")
