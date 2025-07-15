# 🚀 io.net Intelligence + LiteLLM CLI Integration

This project demonstrates a robust integration of [io.net Intelligence](https://docs.io.net/) as an OpenAI-compatible LLM endpoint using [LiteLLM](https://github.com/BerriAI/litellm).  
You can fetch the latest available chat models from io.net, select a model interactively, enter any prompt, and get instant responses via the command line.

---

## Features

- **Automatic model discovery** — always up-to-date with your io.net deployment
- **OpenAI-compatible API calls** with LiteLLM, supporting custom `api_base`
- **.env-based API key management** (never hardcode secrets)
- **User-friendly CLI** to select a model and enter prompts
- **Clean, well-commented code** for easy understanding and maintenance

---

## Prerequisites

- Python 3.8 or higher
- pip

---

## Setup

1. **Clone or copy this repository/files** to your local machine.

2. **Install dependencies:**
    ```bash
    pip install requests python-dotenv litellm
    ```

3. **Create a `.env` file** in your project root:
    ```env
    IO_NET_API_KEY=your_actual_io_net_api_key_here
    ```
    > *Never share or commit your API key!*

---

## Usage

Run the script:

```bash
python main.py
````

* The script will fetch available chat models from your io.net endpoint.
* Select a model by number or name, enter your prompt, and get the AI response.

---

## Example Session

```plaintext
io.net Intelligence / LiteLLM CLI Tester
----------------------------------------
Fetching available models...

Available chat models:
1. deepseek-ai/DeepSeek-R1-0528
2. meta-llama/Llama-4-Maverick-17B-128E-Instruct-FP8
3. Qwen/Qwen3-235B-A22B-FP8
...
21. ibm-granite/granite-3.1-8b-instruct

Select model by number (1-21), or type model name: 2
Enter your prompt: Tell me a funny joke

Sending prompt to model: meta-llama/Llama-4-Maverick-17B-128E-Instruct-FP8

--- AI Response ---
Why couldn't the bicycle stand up by itself? Because it was two-tired!
```

---

## Model Reference

For more on io.net’s supported models:
👉 [io.net Model List Documentation](https://docs.io.net/reference/get-models-list)

---

## Code Structure

* `main.py` — The CLI interface and integration logic
* `.env` — Your io.net API key (never commit this!)
* `README.md` — You are here

---

## Troubleshooting

* **No chat models available:**

  * Check your internet connection.
  * Verify your API key and endpoint.
  * If needed, print the full API response for debugging.

* **BadRequestError: LLM Provider NOT provided:**

  * Ensure you’re using the `openai/` prefix in the model string (handled in this script).

* **Network or DNS errors:**

  * Try another network, check your DNS settings, or contact io.net support.

---

## License

MIT (or specify your license here)

---

## Credits

* [LiteLLM](https://github.com/BerriAI/litellm) by BerriAI
* [io.net Intelligence](https://docs.io.net/)

---

*Built for rapid prototyping and real-world deployments. Enjoy!*

```

---

**Feel free to edit, add badges, or adjust the license section as you wish.  
Let me know if you want an even more minimal or advanced version!**
```
