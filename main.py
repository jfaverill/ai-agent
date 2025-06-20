import sys
import os
from google import genai
from google.genai import types
from dotenv import load_dotenv
from call_function import available_functions
from prompts import system_prompt

def main():
    load_dotenv()
    args = sys.argv[1:]
    if not args:
        print("AI Code Assistant")
        print('\nUsage: python main.py "your prompt here" [--verbose]')
        print('Example: python main.py "How do I fix the calculator?"')
        sys.exit(1)
    verbose = False
    if args[-1] == "--verbose":
        verbose = True
        args = args[:-1]

    prompt = " ".join(args)

    messages = [
        types.Content(role="user", parts=[types.Part(text = prompt)]),
    ]

    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)
    
    response = client.models.generate_content(
        model = "gemini-2.0-flash-001",
        contents = messages,
        config=types.GenerateContentConfig(tools = [available_functions], 
                                           system_instruction = system_prompt)
    )

    if verbose:
        prompt_tokens = response.usage_metadata.prompt_token_count
        response_tokens = response.usage_metadata.candidates_token_count
        print(f"User prompt: {prompt}")
        print(f"Prompt tokens: {prompt_tokens}")
        print(f"Response tokens: {response_tokens}")

    if not response.function_calls:
        return response.text

    for function_call_part in response.function_calls:
        print(f"Calling function: {function_call_part.name}({function_call_part.args})")

if __name__ == "__main__":
    main()
