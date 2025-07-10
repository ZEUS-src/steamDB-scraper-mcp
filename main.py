from tools.sb import SteamDB
from mcp.server.fastmcp import FastMCP
mcp = FastMCP("SteamDB")
steam_db = SteamDB()
from pathlib import Path

@mcp.tool()
def parse_from_steamDB_with_rank(rank: int) -> dict:
    """
    Parse(get) the data from SteamDB with the given (rank|id)
    """
    return steam_db.parser_one(rank)

@mcp.tool()
def parse_all_from_steamDB() -> str:
    """
    Parse(get) the data of all games on SteamDB
    """
    # steam_db.__reset_tables__()
    for i in range(steam_db.total_games):
        steam_db.parser_one(i)
    return f"Parsed {len(steam_db.all_tables)} games from SteamDB"

@mcp.tool()
def get_all_parsed_from_steamDB() -> list[dict]:
    """
    Get all parsed data from SteamDB until now
    """
    return steam_db.all_tables

@mcp.tool()
def get_total_games_on_steamDB() -> str:
    """
    get total games on steamDB page (total the games shown in steamDB)
    """
    return f"Total games on SteamDB: {steam_db.total_games}"

@mcp.tool()
def save_current_parsed(filename: str="steamDB",file_type: str="csv"):
    """
    save the current parsed data to a file (csv or parquet)
    """
    
    if file_type == "csv":
        return steam_db.save_to_csv(f"{filename}.{file_type}")
    elif file_type == "parquet":
        return steam_db.save_to_parquet(f"{filename}.{file_type}")
    else:
        return "Invalid file type"

if __name__ == "__main__":
    steam_db.openBrowser()  # Open browser once at startup
    mcp.run(transport='stdio')