import asyncio
from mcp import ClientSession,StdioServerParameters
from mcp.client.stdio import stdio_client
from dotenv import load_dotenv
import os
from layers.Memory import Memory
from layers.Decision import take_decision
from layers.Perception import perception_extraction
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
                            print(tools)
                            facts=perception_extraction(client,query)
                            memory=Memory()
                            for i in range(ITERATIONS):
                                print(f"================================= Itearation {i+1}========================================================")
                                if(i==0):
                                    print("[Agent] processing the query sent user")
                                print(f"[Agent] processing the query sent from the iteration {i+1}")
                                print("[Perception_Agent] the facts from the query are {facts}")
                                imp_memory=memory.recall_Memory(facts)
                                print("[Memory Agent] Retrieved your passcodes and prvious conversations")
                                print("[Decision Agent] making a decision from the facts,memories and tools available")
                                ans=take_decision(client,imp_memory,tools,query)
                                print("[Agent] Decision taken by the decision_agent now sending the decision to Action Agent")
                                print("[Action Agent] Received the Decisions, processing ....")
                                action=take_action(ans) 
                                if "FINAL_ANSWER" in action:
                                    print("[Agent] Exiting Execution")
                                    break
                                if(i!=2):
                                    print("[Agent]Moving on to the next Iteration")
                                else:
                                    print("[Agent] Iterations Exhausted, now exiting the execution")
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
