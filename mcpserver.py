from mcp.server.fastmcp import FastMCP
import math
import sys
mcp=FastMCP("Server") 

Flag=False
@mcp.tool()
def logger(password):
    '''logs you into AWS console'''
    if password=="abcd1234":
        Flag=True
        return True
    return False

@mcp.tool()
def deploy():
    if Flag==True:
        print("already logged into console, proceeding with deployment")
        print("Deployed successfully")
    else:
        print("not loggedin, proceeding with logging in")
        return "Need to log into Aws console first and then retry"

@mcp.tool()
def DSA_solver(question):
    """Can solve any type of DSA question"""
    print("received your question, processing.....")
    print("completed processing, The answer is")
    print("print(\"hello world\")")
# DEFINE RESOURCES

# Add a dynamic greeting resource
@mcp.resource("greeting://{name}")
def get_greeting(name: str) -> str:
    """Get a personalized greeting"""
    print("CALLED: get_greeting(name: str) -> str:")
    return f"Hello, {name}!"

if(__name__=='__main__'):
    print("stating the server")
    if(len(sys.argv)>1 and sys.argv[1]=="dev"):
        mcp.run()
    else:
        mcp.run(transport="stdio")