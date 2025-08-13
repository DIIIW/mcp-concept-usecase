from typing import Any
# import httpx
from mcp.server.fastmcp import FastMCP
from file_manager import get_folder_file_structure, move_file, read_txt_file

# Initialize FastMCP server
mcp = FastMCP("mcp-blog-mock")

# mock_api_url = "https://6899bca2fed141b96ba08415.mockapi.io/namefinancefial"

# @mcp.tool()
# def get_blogs():
#     response = httpx.get(mock_api_url)
#     return response.json()

# @mcp.tool()
# def search_blogs(query: str):
#     response = httpx.get(mock_api_url)
#     return response.json()

@mcp.tool()
def get_folder_file():
    """
    Returns folders (with /) and files as separate lists.
    """
    response = get_folder_file_structure()
    return response

@mcp.tool()
def move_file_to(src:str, dest:str):
    """
    Moves a file from src to dest.
    Creates destination folders if they don't exist.
    
    Parameters:
        src (str or Path): Source file path.
        dest (str or Path): Destination file path.
    """

    response = move_file(src, dest)
    return response


@mcp.tool()
def read_txt(src:str):
    """
    Reads a .txt file from the given relative path.

    Parameters:
        src (str or Path): Relative path to the text file (e.g., "folder/file.txt").

    Returns:
        str: JSON string containing:
            - "message": A description of the read operation.
            - "content": The file contents as a string.

    Raises:
        FileNotFoundError: If the file does not exist.
        ValueError: If the file is not a .txt file.
    """
    response = read_txt_file(src)
    return response

if __name__ == "__main__":
    mcp.run(transport='stdio')
