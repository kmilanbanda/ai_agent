import os
from dotenv import load_dotenv
from google import genai
from google.genai import types
import sys


def main():
    #raise exception if no user prompt
    args = sys.argv[1:]

    if not args:
        raise Exception("No prompt provided.\n Example: python main.py What is the meaning of life?")
        sys.exit(1)

    verbose = False
    if args[-1] == "--verbose":
        verbose = True
        user_prompt = " ".join(args[0:-1])
    else:
        user_prompt = " ".join(args)
        
    #load .env
    load_dotenv()

    #get api key
    api_key = os.environ.get("GEMINI_API_KEY")

    #set client
    client = genai.Client(api_key=api_key)
    
    #get response from client using given model and user prompt
    model = "gemini-2.0-flash-001"

    messages = [
        types.Content(role="user", parts=[types.Part(text=user_prompt)]),
    ]

    response = client.models.generate_content(
        model=model, 
        contents=messages
    )
    
    #print response text
    print(response.text)

    #print verbose options
    prompt_tokens = response.usage_metadata.prompt_token_count
    response_tokens = response.usage_metadata.candidates_token_count
    if verbose:
        print("User prompt:", user_prompt)
        print("Prompt tokens:", prompt_tokens)
        print("Response tokens:", response_tokens)

main()
