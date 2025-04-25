from Decision import take_decision
from Memory import Memory
from Perception import perception_extraction
import os
from dotenv import load_dotenv
from google import genai
load_dotenv(dotenv_path=r"C:\EAG\.env")
AI=os.getenv("GEMINI_API_KEY")
client= genai.Client(api_key=AI)
q=" what is 5+3 when it is multiplied by 100"
api_key=os.getenv("")
prompt=f"you have {3-1} iterations remaining so solve this query by utitlising the iterations. You may end the return the FINAL_ANSWER befor the iterations end as well"
for i in range(3):
    prompt+=q
    facts=perception_extraction(client,prompt)
    print("[AGENT] Facts gathered")
    obj=Memory()
    print("[AGENT] gathering memory")
    mem=obj.recall_Memory(client,facts)
    print("[AGENT] memory gathered")
    print("[AGENT] taking decision")
    tools={"DSA solver":"can solve any sort of DSA problem","Deployer":"Can deploy any sort of software on AWS"}
    decision=take_decision(client,mem,tools,query="hi")
    print(decision)
    prompt=f"this is the decision taken by the model + {decision} what to do next for the initial query : "
    prompt+=f"you have {3-1-i-1} iterations remaining so solve this query by utitlising the iterations. You may end the return the FINAL_ANSWER befor the iterations end as well"



