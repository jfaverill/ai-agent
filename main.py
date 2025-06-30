import sys
import os
from google import genai
from google.genai import types
from dotenv import load_dotenv
from call_function import available_functions, call_function
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

    if verbose:
        print(f"User prompt: {prompt}")

    messages = [
        types.Content(role="user", parts=[types.Part(text = prompt)]),
    ]

    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)
    generate_content(client, messages, verbose)
    
def generate_content(client, messages, verbose):
    for i in range(20):
        response = client.models.generate_content(
            model = "gemini-2.0-flash-001",
            contents = messages,
            config=types.GenerateContentConfig(tools = [available_functions], 
                                            system_instruction = system_prompt)
        )

        for candidate in response.candidates:
            messages.append(candidate.content)

        if verbose:
            prompt_tokens = response.usage_metadata.prompt_token_count
            response_tokens = response.usage_metadata.candidates_token_count
            print(f"Prompt tokens: {prompt_tokens}")
            print(f"Response tokens: {response_tokens}")

        if not response.function_calls:
            print(response.text)
            break
        else:
            function_responses = []
            for function_call_part in response.function_calls:
                function_call_result = call_function(function_call_part, verbose)
                messages.append(function_call_result)
                if (not function_call_result.parts[0].function_response.response
                    or not function_call_result.parts):
                    raise Exception("empty function call result")
                if verbose:
                    print(f"-> {function_call_result.parts[0].function_response.response}")
                function_responses.append(function_call_result.parts[0])
            if not function_responses:
                raise Exception("no function responses generated, exiting")

if __name__ == "__main__":
    main()
