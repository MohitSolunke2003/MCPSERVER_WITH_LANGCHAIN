from langchain_mcp_adapters.client import MultiServerMCPClient
from langgraph.prebuilt import create_react_agent
from langchain_groq import ChatGroq

from dotenv import load_dotenv
load_dotenv()

import asyncio

async def main():
    client=MultiServerMCPClient(
        {
            "math":{
                "command":"python",
                "args":["mathserver.py"], #Ensure correct absolute path
                "transport":"stdio",

            },
            "weather":{
                "url": "http://localhost:8000/mcp", #Ensure server is running here
                "transport": "streamable-http",
            }
        }
    ) 

    import os
    os.environ["GROQ_API_KEY"]=os.getenv("GROQ_API_KEY")

    tools=await client.get_tools()
    model=ChatGroq(model="qwen-qwq-32b")
    agent=create_react_agent(
        model,tools
    )

    math_response=await agent.ainvoke(
        {
            "message":[{"role": "user","content":"what's (3 + 5)*12?"}]
        }
    )

    print("Math Response:", math_response['message'][-1].content)

    weather_response=await agent.ainvoke(
        {"message":[{"role": "user","content":"what is the weather in CA"}]}

    )
    print("Weather Response:", weather_response['message'][-1].content)

asyncio.run(main())