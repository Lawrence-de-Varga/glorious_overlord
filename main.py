import os
import sys

from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

# If no prompt is given exit
try:
    user_prompt = sys.argv[1]
except IndexError:
    sys.exit("1")

if user_prompt == "--verbose":
    raise Exception("'--verbose' option must be the second argument.")

# if the '--verbose' option is given, verbose will be set to true
# and more data about the prompt will be printed
try:
    user_arg = sys.argv[2]
    if user_arg == "--verbose":
        verbose = True
    else:
        raise Exception(f"'{user_arg}' is not a valid option.")
except IndexError:
    verbose = False


messages = [
    types.Content(role="user", parts=[types.Part(text=user_prompt)]),
]

client = genai.Client(api_key=api_key)
response = client.models.generate_content(
    model="gemini-2.0-flash-001", contents=messages
)
if verbose:
    print(f"User prompt: {user_prompt}")
    print()
    print(response.text)
    print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
    print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
else:
    print()
    print(response.text)
