# Aphrodite Guidance Demo
This repository is about using [Guidance](https://github.com/guidance-ai/guidance) with an [OpenAI Aphrodite Endpiont](https://github.com/PygmalionAI/aphrodite-engine#usage)

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

> :warning: This example requires logit_bias support for aphrodite. In case they're not already implemented, you can find the required changes [here](https://github.com/miku448/aphrodite-engine/commit/3deadbbc308aea7343a0491e08012c5cdf05d22d#diff-b10963af97b99d9e3d041a52242b40f7fc98c7c315c1ddc4e3127dfbdcf76b83L35).
