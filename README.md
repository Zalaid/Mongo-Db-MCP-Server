# MongoDB MCP Server

A Model Context Protocol (MCP) server for MongoDB database operations. This server provides tools to interact with MongoDB databases through the MCP protocol with NATURAL LANGUAGE QUERIES.

## Author

**Zalaid**  
Email: zalaidbutt1@gmail.com

## Features

- **Find Documents**: Search for documents in MongoDB collections with filters and projections
- **Update Documents**: Update documents in collections using MongoDB update operations
- **Delete Documents**: Remove documents from collections based on filter criteria
- **List Collections**: Get a list of all collections in the database
- **Async Operations**: All database operations are performed asynchronously for better performance

## Prerequisites

- Python 3.8 or higher
- MongoDB database (local or remote)
- Claude Desktop application

## Installation & Setup

### 1. Environment Setup

1. Clone or download this project
2. Navigate to the `mongodb-server` directory
3. Create a `.env` file with your MongoDB configuration:

```env
MONGO_URI=mongodb://localhost:####
MONGO_DB_NAME=your_database_name
```

### 2. Install Dependencies

Install the required Python packages:

```bash
pip install -r requirements.txt
```

Or using uv:

```bash
uv pip install -r requirements.txt
```

### 3. Claude Desktop Configuration

Add the following configuration to your Claude Desktop settings:

#### For Windows Users: 
Replace the paths with your actual Python installation and project location.

```json
{
  "mcpServers": {
    "mongodb-server": {
      "command": "C:\\Users\\Zalaid\\AppData\\Local\\Programs\\Python\\Python313\\Scripts\\uv.EXE",
      "args": [
        "run",
        "--with", "mcp[cli]",
        "--with", "pymongo",
        "--with", "python-dotenv",
        "D:\\BSDS\\7th Semester\\Fyp Learning\\MCP-SERVER\\mongo-db-mcp-server\\mongodb-server\\server.py"
      ]
    }
  }
}
```

#### Alternative Configuration (using Python directly):

```json
{
  "mcpServers": {
    "mongodb-server": {
      "command": "python",
      "args": [
        "D:\\BSDS\\7th Semester\\Fyp Learning\\MCP-SERVER\\mongo-db-mcp-server\\mongodb-server\\server.py"
      ],
      "cwd": "D:\\BSDS\\7th Semester\\Fyp Learning\\MCP-SERVER\\mongo-db-mcp-server\\mongodb-server"
    }
  }
}
```

**Note**: Update the paths in the configuration to match your system's Python installation and project location.

## Available Tools

### 1. find_documents
Search for documents in a MongoDB collection.

**Parameters:**
- `collection_name` (string): Name of the collection to search
- `filter_query` (dict): MongoDB filter query
- `projection` (dict, optional): Fields to include/exclude in results

### 2. update_documents
Update documents in a MongoDB collection.

**Parameters:**
- `collection_name` (string): Name of the collection
- `filter_query` (dict): Filter to match documents
- `update_operation` (dict): MongoDB update operation

### 3. delete_documents
Delete documents from a MongoDB collection.

**Parameters:**
- `collection_name` (string): Name of the collection
- `filter_query` (dict): Filter to match documents to delete

### 4. list_collections
Get a list of all collections in the database.

**Parameters:** None

## Usage Examples

Once configured in Claude Desktop, you can use natural language to interact with your MongoDB database:

- "Find all users in the users collection"
- "Update the user with email 'john@example.com' to set status as 'active'"
- "Delete all documents in the logs collection older than 30 days"
- "Show me all collections in the database"

## Environment Variables

Create a `.env` file in the mongodb-server directory with:

```env
# MongoDB Connection
MONGO_URI=mongodb://localhost:###
# Or for MongoDB Atlas:
# MONGO_URI=mongodb+srv://username:password@cluster.mongodb.net/

# Database Name
MONGO_DB_NAME=your_database_name
```

## Troubleshooting

1. **Connection Issues**: Verify your MongoDB URI and ensure the database is running
2. **Permission Errors**: Make sure your MongoDB user has appropriate permissions
3. **Path Issues**: Ensure all file paths in the Claude Desktop configuration are correct
4. **Dependencies**: Run `pip install -r requirements.txt` to install missing packages

## Contributing

Contributions are welcome! Please feel free to submit issues and pull requests.

---

**Author**: Zalaid (zalaidbutt1@gmail.com)
