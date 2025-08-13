from typing import Any
from mcp.server.fastmcp import FastMCP
from file_manager import get_folder_file_structure, move_file, read_txt_file
from aitable_api import get_filter_record

# Initialize FastMCP server
mcp = FastMCP("mcp-file")

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


@mcp.tool()
def get_aitable_specific_filter_condition(condition:str, maxRecords:int):
    """
    Retrieve Airtable records that match a specific filter condition.

    Args:
        conditions (str): A valid Airtable formula expression for filtering.
            This must follow Airtable's formula syntax.
        maxRecords (int): The maximum number of records to fetch. default 5. 

    Description:
        Sends a GET request to the Airtable API and returns only the records 
        that match the specified filter formula. The `conditions` string 
        should be formatted according to Airtable's `filterByFormula` rules.

    Example:
        get_filter_record("{team} = 'Team A'")
        #### Retrieves all records where the 'team' field is exactly 'Team A'.

        get_filter_record("AND({status} = 'active', {score} > 80)")
        #### Retrieves all records where 'status' is 'active' and 'score' is greater than 80.
    """
    response = get_filter_record(condition, maxRecords)
    return response

if __name__ == "__main__":
    mcp.run(transport='stdio')
