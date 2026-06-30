import os
from dotenv import load_dotenv
from google import genai


def main():
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    if api_key is None:
        raise RuntimeError("Error: no API key found")
    
    test_contents = "Why is Boot.dev such a great place to learn backend development? Use one paragraph maximum."
    client = genai.Client(api_key=api_key)
    response = client.models.generate_content(model="gemini-2.5-flash", 
                contents = test_contents)

    if (response.usage_metadata is None):
        raise RuntimeError("Error: Gemini response failed")
    
    print(f"User prompt: {test_contents}")
    print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
    print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
    print(f"Response:\n{response.text}")


if __name__ == "__main__":
    main()
