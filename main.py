import os
import argparse
from dotenv import load_dotenv
from google import genai
from google.genai import types


def main():
    # initialise the API
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    if api_key is None:
        raise RuntimeError("Error: no API key found")
    client = genai.Client(api_key=api_key)
    
    # read argument from command line
    parser = argparse.ArgumentParser(description="Chatbot")
    parser.add_argument("user_prompt", type=str, help="User prompt")
    args = parser.parse_args()

    messages: list[types.Content] = [
        types.Content(role="user", parts=[types.Part(text=args.user_prompt)])
    ]

    generate_content(client, messages)


# generate a response from gemini using the API
def generate_content(client: genai.Client, messages: list[types.Content]):
    response = client.models.generate_content(
                model="gemini-2.5-flash", contents = messages)

    if (response.usage_metadata is None):
        raise RuntimeError("Error: Gemini response failed")
    
    print(f"User prompt: {messages}")
    print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
    print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
    print(f"Response:\n{response.text}")


if __name__ == "__main__":
    main()


