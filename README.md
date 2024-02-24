# 📋 Mojicopy

Tool to generate emojis from text prompts stored in the clipboard using OpenAI.

## 🔨 Installation

Install the mojicopy package using pip

```shell
pip install mojicopy
```

Get an [OpenAI API Key](https://beta.openai.com/account/api-keys) and place it inside the `OPENAI_API_KEY` environment variable

## 🏃‍♂️ Usage

Get an emoji from a prompt stored in your clipboard

```shell
mojicopy
>>> 🐈
```

Get an emoji from a prompt in the CLI

```shell
mojicopy --prompt "OpenAI API Key"
>>> 🔑
```

Get a random emoji into your clipboard

```shell
mojicopy --random
```

### VSCode Integration

TBD

### IntelliJ Integration

TBD
