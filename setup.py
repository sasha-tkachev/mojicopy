from pathlib import Path

import setuptools


def _read_requirements(filename):
    return [
        line.strip()
        for line in Path(filename).read_text().splitlines()
        if not line.startswith("#")
    ]


here = Path(__file__).parent.resolve()
long_description = (here / "README.md").read_text(encoding="utf-8")

if __name__ == "__main__":
    setuptools.setup(
        name="mojicopy",
        version="1.1.0",
        author="Alexander Tkachev",
        author_email="sasha64sasha@gmail.com",
        description="Tool to generate emojis from text prompts stored in the clipboard using OpenAI.",
        long_description_content_type="text/markdown",
        long_description=long_description,
        url="https://mojicopy.com",
        keywords=["emoji", "clipboard", "openai", "ChatGPT"],
        packages=setuptools.find_packages(),
        install_requires=_read_requirements("requirements.txt"),
        classifiers=[
            "Intended Audience :: Information Technology",
            "Intended Audience :: System Administrators",
            "Intended Audience :: Developers",
            "License :: OSI Approved :: Apache Software License",
            "Development Status :: 5 - Production/Stable",
            "Operating System :: OS Independent",
            "Programming Language :: Python :: 3",
            "Programming Language :: Python :: 3.7",
            "Programming Language :: Python :: 3.8",
            "Programming Language :: Python :: 3.9",
            "Programming Language :: Python :: 3.10",
        ],
        entry_points={
            "console_scripts": [
                "mojicopy = mojicopy.cli:app",
            ],
        },
    )
