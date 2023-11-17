# Aphrodite Guidance Demo
This repository is about using [A Guidance Fork](https://github.com/miku448/guidance) with an [OpenAI Aphrodite Endpiont](https://github.com/PygmalionAI/aphrodite-engine#usage)

> :warning: This code is experimental and not meant for production use. It's just a proof of concept.

### Example
It's useful for enforcing a format when generating tokens.

```
Prompt:
+------------------------------------------------------------------------------+
|Common sense question and answer                                              |
|Question: What is the besto waifu in domekano?                                |
|Answer:{{#select "waifu"}} Hina{{or}} Rui{{/select}}                          |
+------------------------------------------------------------------------------+
Completion:
+------------------------------------------------------------------------------+
|Common sense question and answer                                              |
|Question: What is the besto waifu in domekano?                                |
|Answer: Hina                                                                  |
+------------------------------------------------------------------------------+
```

## Installation
First, clone this repository and install the requirements:

```bash
git clone https://github.com/miku448/aphrodite-guidance.git
cd aphrodite-guidance
pip install -r requirements.txt
```

## Usage
Once you have a `aphrodite.openai.api_server` running, you can modify the [`examples.py`](/examples.py) file to your liking and run it. It's using `mistralai/Mistral-7B-v0.1` and running it locally on the default Aphrodite's port.

```bash
python examples.py
```