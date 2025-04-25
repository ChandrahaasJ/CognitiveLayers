import asyncio
from mcp import ClientSession,StdioServerParameters
from mcp.client.stdio import stdio_client
from dotenv import load_dotenv
import os
from layers.Memory import Memory
from layers.Decision import take_decision
from layers.Perception import perception_extraction
from layers.Action import take_action
from google import genai
load_dotenv(dotenv_path=r"C:\EAG\.env")
ITERATIONS=3
AI=os.getenv("GEMINI_API_KEY")
client= genai.Client(api_key=AI)
# establish connection(Stdio_client) --> create a session(ClientSession) --> initialise the session
async def main(query : str):
    try:
        print("[agent] starting agent")
        server_params=StdioServerParameters(
            command="python",
            args=["mcpserver.py"],
            cwd=r"C:\EAG\CognitiveLayers"
        )
        try:
            async with stdio_client(server_params) as (read,write):
                print("connection established")
                try:
                    async with ClientSession(read,write) as session:
                        print("[agent]session created, initializing")
                        try:
                            await session.initialize()
                            print("[agent] MCP session initialized")
                            tools=await session.list_tools()
                            #print(tools)
                            memory=Memory()
                            prompt=f"you have {3-1} iterations remaining so solve this query by utitlising the iterations. You may end the return the FINAL_ANSWER befor the iterations end as well"
                            for i in range(3):
                                prompt+=query
                                facts=perception_extraction(client,prompt)
                                print("[AGENT] Facts gathered")
                                
                                print("[AGENT] gathering memory")
                                mem=memory.recall_Memory(client,facts)
                                print("[AGENT] memory gathered")
                                print("[AGENT] taking decision")
                                tools={"DSA solver":"can solve any sort of DSA problem","Deployer":"Can deploy any sort of software on AWS"}
                                decision=take_decision(client,mem,tools,query="hi")
                                print(decision)
                                prompt=f"this is the decision taken by the model + {decision} what to do next for the initial query : "
                                prompt+=f"you have {3-1-i-1} iterations remaining so solve this query by utitlising the iterations. You may end the return the FINAL_ANSWER befor the iterations end as well"
                        except Exception as e:
                            print(f"error while initialising the session : {e}")
                except Exception as e:
                    print(e)
        except Exception as e:
            print(f"error while creating the session : {e}")
    except Exception as e:
        print(f"Overall error {e}")





if __name__ == "__main__":
    q="hi"
    asyncio.run(main(q))
