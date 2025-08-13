import httpx
from mcp.server.fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("mcp-blog-mock")

mock_api_url = "https://6899bca2fed141b96ba08415.mockapi.io/namefinancefial"

@mcp.tool()
def get_blogs():
    response = httpx.get(mock_api_url)
    return response.json()

@mcp.tool()
def search_blogs(query: str):
    response = httpx.get(mock_api_url)
    return response.json()