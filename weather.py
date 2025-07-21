from mcp.server.fastmcp import FastMCP

mcp=FastMCP("weather")

@mcp.tool()
async def get_weather(location:str)->str:
    """Gget the weather location"""
    return "It's a always raining in CA"

if __name__=="__main__":
    mcp.run(transport="streamable-http")