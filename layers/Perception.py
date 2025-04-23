from dotenv import load_dotenv
import os
from google import genai
load_dotenv(dotenv_path=r"C:\EAG\.env")
AI=os.getenv("GEMINI_API_KEY")
client= genai.Client(api_key=AI)
prompt="Hi how are you?"
response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=prompt
        )

print(response.text)
