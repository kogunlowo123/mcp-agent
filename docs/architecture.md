# MCP Agent Architecture

Model Context Protocol agent that manages MCP server connections, discovers and exposes tools and resources, handles protocol negotiation, and enables standardized AI-to-service communication across heterogeneous tool ecosystems.

## Domain Tools

- **discover_servers**: Discover available MCP servers and their capabilities
- **connect_server**: Establish connection to an MCP server with authentication
- **list_tools**: List available tools from connected MCP servers
- **invoke_tool**: Invoke a tool on a connected MCP server
- **read_resource**: Read a resource exposed by an MCP server