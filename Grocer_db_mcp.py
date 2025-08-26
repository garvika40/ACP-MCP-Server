import pandas as pd 
from mcp.server.fastmcp import FastMCP
import os
from typing import Any

mcp = FastMCP("Grocery_List_Tool")
curr_path = os.getcwd()
data_path = os.path.join(curr_path, "Grocery.csv")

def load_data(data_path):
    "This function fetches the available list of groceries from the data"
    df = pd.read_csv(data_path)
    df_json = df.to_json()
    print(df.columns)
    return df_json


@mcp.tool()
async def fetch_available_grocery(json_data: dict[str, Any]) -> str | None:
    """Get the available groceries/ingredients and their quantities"""
    Grocery_json = load_data(data_path)   # no need for await since load_data isn’t async
    return Grocery_json


if __name__ == "__main__":
    # Debug run to see function output
    print(fetch_available_grocery.__doc__)
    import asyncio
    result = asyncio.run(fetch_available_grocery({}))
    print("Tool result:", result)
    
    # Comment this out if you only want local testing
    mcp.run(transport='stdio')



# load_data("/home/garvika/Desktop/ACP_MCP/Grocery.csv")