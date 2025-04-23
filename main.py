import asyncio
from mcp import ClientSession,StdioServerParameters
from mcp.client.stdio import stdio_client
from dotenv import load_dotenv
import os
load_dotenv(dotenv_path=r"C:\EAG\.env")

AI=os.getenv("GEMINI_API_KEY")
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
