from dotenv import load_dotenv
import os
from google import genai
load_dotenv(dotenv_path=r"C:\EAG\.env")
import re
# AI=os.getenv("GEMINI_API_KEY")
# client= genai.Client(api_key=AI)
# prompt="Hi how are you?"
# response = client.models.generate_content(
#             model="gemini-2.0-flash",
#             contents=prompt
#         )

# print(response.text)

def perception_extraction(client,query):
    prompt = f"""
            You are an AI that extracts structured facts from user input.

            Input: "{query}"

            Return the response as a Python dictionary with keys:
            - intent: (brief phrase about what the user wants)
            - entities: a list of strings representing keywords or values (e.g., ["INDIA", "ASCII"])
            - tool_hint: (name of the MCP tool that might be useful, if any)

            Output only the dictionary on a single line. Do NOT wrap it in ```json or other formatting. Ensure `entities` is a list of strings, not a dictionary.
                """
    
    response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=prompt
        )
    raw=response.text.strip()
    print(raw)
    if "json" in raw:
        clean = re.sub(r"^```json|```$", "", raw.strip(), flags=re.MULTILINE).strip()
        return eval(clean)
    else:
        return raw
    
    
