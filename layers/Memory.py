from dotenv import load_dotenv
import os
from google import genai
import re
# load_dotenv(dotenv_path=r"C:\EAG\.env")
# AI=os.getenv("GEMINI_API_KEY")
# client= genai.Client(api_key=AI)

class Memory:
    passwords=[]
    context=[]
    def __init__(self):
        self.passwords=[{"AWS":"abcd1234","OpenAI":"TSAIistheBEST"}]
        

    def getMemory(self):
        return self.context
    
    def appendMemory(self,mem):
        self.context.append(mem)

    def recall_Memory(self,client,facts):
        prompt=f"""You are a specialized Memory Agent with access to two critical data structures:

            1. PASSWORDS: {self.passwords}
            - Contains credentials and access tokens
            - Format: List of dictionaries with service:password pairs
            - Use Case: Authentication and service access verification

            2. CONTEXT: {self.context}
            - Contains previous conversation history
            - Format: List of chronological conversation entries
            - Use Case: Understanding historical interactions and commitments

            TASK:
            Analyze the following query against stored memory data: "{facts}"

            INSTRUCTIONS:
            1. MEMORY ANALYSIS STEPS:
            a) First, examine the context for any relevant historical information
            b) Then, check passwords if query involves service access
            c) Document your findings in each step

            2. OUTPUT STRUCTURE:
            Return your analysis in the following JSON format:
            {{
                "context_matches": [],      // List of relevant historical information
                "password_checks": [],      // List of relevant credential checks
                "temporal_conflicts": [],   // List of time-based conflicts
                "security_alerts": [],      // List of security concerns
                "final_response": "",       // Your formatted response to the user
                "reasoning_type": "",       // Type of memory operation performed
                "confidence_level": 0.0     // 0.0 to 1.0 scale
            }}

            3. REASONING GUIDELINES:
            - TAG each piece of information with its source: [CONTEXT] or [PASSWORDS]
            - VERIFY temporal consistency for appointments and schedules
            - ALERT if detecting potential security risks
            

            4. ERROR HANDLING:
            If you encounter any of these situations:
            - Ambiguous matches: List all possibilities
            - No matches: Return "NO_RELEVANT_MEMORY"
            - Conflicting information: Flag with "MEMORY_CONFLICT"
            - Security concerns: Raise "SECURITY_ALERT"

            5. SELF-VERIFICATION:
            Before finalizing your response:
            - Cross-reference dates and times
            - Verify credential access requirements
            - Check for logical contradictions
            - Validate temporal sequence of events

            Example Response:
            For query "Can I access AWS console?":
            {{
            "context_matches": ["[CONTEXT] Last AWS login attempt: 2 hours ago"],
            "password_checks": ["[PASSWORDS] AWS credentials found"],
            "temporal_conflicts": [],
            "security_alerts": ["Recent failed login attempts detected"],
            "final_response": "AWS console access is possible with stored credentials, but note there were recent failed login attempts.",
            "reasoning_type": "credential_verification",
            "confidence_level": 0.95
            }}

            Remember: Prioritize security and accuracy over completeness. If uncertain, flag it."""
        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=prompt
        )
        raw = response.text.strip()
        clean = re.sub(r"^```json|```$", "", raw.strip(), flags=re.MULTILINE).strip()
        return eval(clean)

