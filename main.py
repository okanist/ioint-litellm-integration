import os
import requests
from dotenv import load_dotenv
from litellm import completion

# Load environment variables from .env file
load_dotenv()

IO_NET_API_KEY = os.getenv("IO_NET_API_KEY")
IO_NET_API_BASE = "https://api.intelligence.io.solutions/api/v1"

if not IO_NET_API_KEY:
    raise ValueError("IO_NET_API_KEY not found in .env file. Please set it.")

def fetch_supported_models():
    """Fetches the list of supported chat models from io.net."""
    try:
        url = "https://api.intelligence.io.solutions/api/v1/models"
        headers = {
            "accept": "application/json",
            "Authorization": f"Bearer {IO_NET_API_KEY}",
        }
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        raw_json = response.json()
        print("RAW API RESPONSE:", raw_json)  # <-- Debug print!
        all_models = raw_json.get("data", [])
        # All returned models are chat models!
        chat_models = [m["id"] for m in all_models]
        return chat_models
    except Exception as e:
        print(f"Could not fetch models: {e}")
        return []

def get_io_intelligence_completion(prompt: str, model: str):
    """
    Makes a completion request to io.net Intelligence via LiteLLM.
    """
    try:
        response = completion(
            model=f"openai/{model}",
            messages=[{"role": "user", "content": prompt}],
            api_key=IO_NET_API_KEY,
            api_base=IO_NET_API_BASE
        )
        return response.choices[0].message.content
    except Exception as e:
        print(f"Error calling io.net Intelligence API: {e}")
        return None

if __name__ == "__main__":
    print("io.net Intelligence / LiteLLM CLI Tester")
    print("----------------------------------------")
    print("Fetching available models...")
    models = fetch_supported_models()
    if not models:
        print("No chat models available. Check your API key or internet connection.")
        exit(1)
    print("\nAvailable chat models:")
    for idx, m in enumerate(models, 1):
        print(f"{idx}. {m}")
    while True:
        selection = input(f"\nSelect model by number (1-{len(models)}), or type model name: ").strip()
        if selection.isdigit() and 1 <= int(selection) <= len(models):
            model = models[int(selection) - 1]
            break
        elif selection in models:
            model = selection
            break
        else:
            print("Invalid selection. Try again.")

    prompt = input("Enter your prompt: ").strip()
    print(f"\nSending prompt to model: {model}\n")
    ai_response = get_io_intelligence_completion(prompt, model=model)
    if ai_response:
        print("\n--- AI Response ---")
        print(ai_response)
    else:
        print("\nFailed to get a response from io.net Intelligence.")

    print("\nTo find supported models, visit: https://docs.io.net/reference/get-models-list")
