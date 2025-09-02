import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types

verbose = False
if len(sys.argv) == 1:
    print("Error: Pass the prompt as an argument")
    sys.exit(1)
elif len(sys.argv) == 3:
    if(sys.argv[2]=="--verbose"):
        verbose = True


messages = [
    types.Content(role="user", parts=[types.Part(text=sys.argv[1])]),
]

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)
response = client.models.generate_content(model="gemini-2.0-flash-001", contents=messages)
print("a")
text = response.text
prompt_tokens = response.usage_metadata.prompt_token_count
response_tokens = response.usage_metadata.candidates_token_count

print(text)
if verbose:
    print(f"User prompt: {sys.argv[1]}")
    print(f"Prompt tokens: {prompt_tokens}")
    print(f"Response tokens: {response_tokens}")