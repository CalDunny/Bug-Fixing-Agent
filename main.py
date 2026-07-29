import os
import argparse
from dotenv import load_dotenv
from google import genai
from dataclasses import dataclass
from config import SYSTEM_PROMPT, AVAILABLE_FUNCTIONS, CALL_LIMIT
from functions.call_function import call_function

@dataclass
class GenerateResult:
    prev_id: str
    message: list[dict]


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

    message: str | list[dict] = args.user_prompt
    prev_id = None

    for i in range(CALL_LIMIT):
        response = generate_content(client, message, prev_id, args.verbose)
        if response==None:
            break
        prev_id = response.prev_id
        message = response.message
    if i==CALL_LIMIT:
        print("Error: Call limit exceeded")
        exit(1)


# generate a response from gemini using the API
def generate_content(client: genai.Client, message: list, prev_id: str, verbose) -> GenerateResult:
    response = client.interactions.create(
                model="gemini-3.5-flash-lite", 
                system_instruction=SYSTEM_PROMPT,
                input = message,
                previous_interaction_id = prev_id,
                tools = AVAILABLE_FUNCTIONS,
                store=True
                )
    
    if response.usage is None:
        raise RuntimeError("Error: Gemini response failed")
    
    if verbose:
        print(f"User prompt: {message}")
        print(f"Prompt tokens: {response.usage.total_input_tokens}")
        print(f"Response tokens: {response.usage.total_output_tokens}")

    # Complete any function calls made
    func_called = False
    result_message = None

    for step in response.steps:
        if step.type == "function_call":
            result_message = call_function(step, verbose)

            if not result_message["result"][0]["text"]:
                raise Exception("Error: Function call did not return a result")

            if verbose:
                print(f"-> {result_message["result"][0]["text"]}")

            func_called = True

    if not func_called:
        print(f"Response:\n{response.output_text}")
        return

    return GenerateResult(prev_id=response.id, message=[result_message])


if __name__ == "__main__":
    main()


