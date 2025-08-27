import os
import json
import asyncio
from dotenv import load_dotenv
from pymongo import MongoClient
from bson import ObjectId

# 1. Import the correct FastMCP class
from mcp.server.fastmcp import FastMCP

# --- Configuration and Database Setup ---
load_dotenv()
MONGO_URI = os.getenv("MONGO_URI")
MONGO_DB_NAME = os.getenv("MONGO_DB_NAME")

if not MONGO_URI or not MONGO_DB_NAME:
    raise ValueError("MONGO_URI and MONGO_DB_NAME must be set in the .env file.")

client = MongoClient(MONGO_URI)
db = client[MONGO_DB_NAME]

# 2. Create the FastMCP instance, just like the nmap server
mcp_server = FastMCP("mongo_database_tools")

# --- Helper Class for JSON Serialization ---
class JSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        return json.JSONEncoder.default(self, o)

# --- 3. Define Tools using the @mcp_server.tool() decorator and async/await ---
# We make the functions async and run the blocking database calls in a separate thread.

@mcp_server.tool()
async def find_documents(collection_name: str, filter_query: dict, projection: dict = None) -> str:
    """Searches for documents in a specified MongoDB collection."""
    def blocking_find():
        try:
            collection = db[collection_name]
            documents = list(collection.find(filter_query, projection))
            if not documents:
                return f"No documents found in '{collection_name}' with the specified filter."
            return json.dumps(documents, cls=JSONEncoder)
        except Exception as e:
            return f"An error occurred while finding documents: {str(e)}"
    return await asyncio.to_thread(blocking_find)

@mcp_server.tool()
async def update_documents(collection_name: str, filter_query: dict, update_operation: dict) -> str:
    """Updates documents in a specified MongoDB collection."""
    def blocking_update():
        try:
            collection = db[collection_name]
            result = collection.update_many(filter_query, update_operation)
            return f"Successfully updated {result.modified_count} document(s)."
        except Exception as e:
            return f"An error occurred while updating documents: {str(e)}"
    return await asyncio.to_thread(blocking_update)

@mcp_server.tool()
async def delete_documents(collection_name: str, filter_query: dict) -> str:
    """Deletes documents from a specified MongoDB collection."""
    def blocking_delete():
        try:
            collection = db[collection_name]
            result = collection.delete_many(filter_query)
            return f"Successfully deleted {result.deleted_count} document(s)."
        except Exception as e:
            return f"An error occurred while deleting documents: {str(e)}"
    return await asyncio.to_thread(blocking_delete)

@mcp_server.tool()
async def list_collections() -> str:
    """Lists all collection names in the current database."""
    def blocking_list():
        try:
            return f"Available collections: {db.list_collection_names()}"
        except Exception as e:
            return f"An error occurred while listing collections: {str(e)}"
    return await asyncio.to_thread(blocking_list)

# --- 4. Create the main entry point to run the server ---
def main():
    """Entry point for the MCP server"""
    mcp_server.run()

if __name__ == "__main__":
    main()