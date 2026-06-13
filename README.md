# PawnDex MCP Server

A Model Context Protocol (MCP) server for [PawnDex](https://packages.open.mp/), the Pawn package index for the SA-MP / open.mp ecosystem.

This server enables AI assistants (like Claude) to:
- **Search** for Pawn packages with various filters.
- **Inspect** detailed information about specific repositories, including releases and tags.
- **Retrieve** global statistics and supported languages.

## Tools

1. `search_packages`: Search for packages using queries like `mysql`, `is:official`, `user:openmultiplayer`, etc.
2. `get_package`: Get full details for a `owner/repo` combination.
3. `get_stats`: View global PawnDex metrics.
4. `get_languages`: List supported languages in the index.

## Installation

### For Claude Desktop
Add the following to your `claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "pawndex": {
      "command": "uv",
      "args": [
        "--directory",
        "/path/to/pawndex_mcp_server",
        "run",
        "pawndex_mcp_server"
      ]
    }
  }
}
```

## Development
Requires Python 3.11+.

```bash
# Install dependencies
uv sync

# Run the server locally (STDIO)
uv run pawndex_mcp_server
```

## License
MIT
