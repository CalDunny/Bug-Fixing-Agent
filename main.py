import os
import argparse
from dotenv import load_dotenv
from google import genai
from google.genai import types
from config import SYSTEM_PROMPT, AVAILABLE_FUNCTIONS


def main() -> None:
    # initialise the API
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    if api_key is None:
        raise RuntimeError("Error: no API key found")
    client = genai.Client(api_key=api_key)
    
    # read argument from command line
    parser = argparse.ArgumentParser(description="Chatbot")
    parser.add_argument("user_prompt", type=str, help="User prompt")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    args = parser.parse_args()

    messages: str = args.user_prompt
    

    generate_content(client, messages, args.verbose)


# generate a response from gemini using the API
def generate_content(client: genai.Client, messages: list[dict], verbose) -> None:
    response = client.interactions.create(
                model="gemini-2.5-flash", 
                system_instruction=SYSTEM_PROMPT,
                input = messages,
                tools = AVAILABLE_FUNCTIONS,
                store=False
                )
    
    if response.usage is None:
        raise RuntimeError("Error: Gemini response failed")
    
    if verbose:
        print(f"User prompt: {messages}")
        print(f"Prompt tokens: {response.usage.total_input_tokens}")
        print(f"Response tokens: {response.usage.total_output_tokens}")
    
    print(f"Response:\n{response.output_text}")


if __name__ == "__main__":
    main()


