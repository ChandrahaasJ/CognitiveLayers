from .Memory import Memory
from dotenv import load_dotenv
import os
from google import genai
from .Perception import perception_extraction
AI=os.getenv("GEMINI_API_KEY")
client= genai.Client(api_key=AI)

def take_decision(Client,memory,tools,query):
    prompt=f""" you have the following tools along with their descriptions : {tools} 
    and this is the context from previous conversations : {memory}
    in case you need access to any passwords, you can get them by accessing the above data structure
    now,you need to pick the set of tools that are needed from above.
    return the answer in a python list.
    examples :
    1. QUERY: Solve the following DSA Question: You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed,
    the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.
    Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.
    OUTPUT : ["array","dynamic programming"] here for example, array and dynamic programming are tools
    or incase you already have the answer, return it as follows:
    [FINAL_ANSWER : Agent Finished execution]  //you have the answer in tools
    
    2. QUERY : Deploy this software on AWS
       OUTPUT : ["EC2","S3","ECS"] here for example, EC2,S3 and ECS are all tools 
       or
       return
       [FINAL_ANSWER: Successfully deployed] //you have the answer in facts
       
    GUIDELINES:
    1. only include the tools in the output if you the tool exists and
       use only the tools and context provided.
    2. In case you dont have any means of solving the problem your OUTPUT should
       return ["CANNOT_SOLVE"]
    3. return the name of tool in the list --> example : [DSA solver] 
    4. DO NOT CREATE YOUR OWN TOOLS. Either return CANNOT_SOLVE or FINAL_ANSWER in case you dont have tools that can be used
      return FINAL_ANSWER if you have the answer in the facts provided. Otherwise return CANNOT_SOLVE"""
    
    
    response = Client.models.generate_content(
            model="gemini-2.0-flash",
            contents=prompt
        )
    
    return response.text

query="""the answer is 100"""
facts=perception_extraction(client,query)
print(facts)
obj=Memory()
mem=obj.recall_Memory(client,facts)

tools={"DSA solver":"can solve any sort of DSA problem","Deployer":"Can deploy any sort of software on AWS"}
ans=take_decision(client,mem,tools,query)
print(ans)