import os
import json
from dotenv import load_dotenv
from google import genai

load_dotenv()
key = os.getenv("GEMINI_API_KEY")

if not key:
    print("❌ Error: GEMINI_API_KEY not found in .env file.")
else:
    # Print first 5 and last 5 chars to verify it loaded correctly without exposing the full key
    print(f"✅ Key loaded: {key[:5]}...{key[-5:]}")
    
    try:
        client = genai.Client(api_key=key)
        response = client.models.generate_content(
            model="gemini-2.0-flash", 
            contents="Hello"
        )
        print("🚀 API Connection Successful!")
    except Exception as e:
        print(f"❌ API Connection Failed: {e}")