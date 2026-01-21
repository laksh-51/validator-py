import os
import sys
import json
from google import genai
from google.genai import types
from dotenv import load_dotenv

load_dotenv()

# Explicitly initialize the new Client
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

SYSTEM_PROMPT = """
You are a strict JSON data validator. Validate the user profile based on these high-level rules:
- name: Required and non-empty. [Warning if < 3 chars]
- email: Must be a valid format. [Warning if disposable]
- age: Must be a positive number. [Warning if < 18]
- country: Must be a valid ISO-2 code (e.g., US, IN).
- phone: Required and in E.164 format. [Warning if country code mismatch]

Return ONLY: {"is_valid": bool, "errors": string[], "warnings": string[]}
"""

def validate_user(data):
    try:
        # Gemini 2.5 Flash is the standard for fast, structured validation in 2026
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=f"Validate this JSON: {json.dumps(data)}",
            config=types.GenerateContentConfig(
                system_instruction=SYSTEM_PROMPT,
                response_mime_type="application/json" # Enforces JSON Mode
            )
        )
        return response.text
    except Exception as e:
        return json.dumps({"is_valid": False, "errors": [f"SDK Error: {str(e)}"], "warnings": []})

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python validate_user.py <file.json>")
        sys.exit(1)
        
    with open(sys.argv[1], 'r') as f:
        print(validate_user(json.load(f)))