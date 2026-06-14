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

<details>
<summary><b>Claude Desktop</b> — via <code>claude_desktop_config.json</code></summary>

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

</details>

<details>
<summary><b>Claude Code</b> — STDIO via <code>.mcp.json</code></summary>

Create a `.mcp.json` file in your project root:

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

Or add via CLI:

```bash
claude mcp add pawndex -- uv --directory /path/to/pawndex_mcp_server run pawndex_mcp_server
```

</details>

<details>
<summary><b>OpenCode</b> — config via <code>opencode.jsonc</code></summary>

Add to your `opencode.jsonc`:

```jsonc
{
  "$schema": "https://opencode.ai/config.json",
  "mcp": {
    "pawndex": {
      "type": "local",
      "command": [
        "uv",
        "--directory",
        "/path/to/pawndex_mcp_server",
        "run",
        "pawndex_mcp_server"
      ],
      "enabled": true
    }
  }
}
```

</details>

<details>
<summary><b>Gemini CLI</b> — config via <code>.gemini/settings.json</code></summary>

Add to your `.gemini/settings.json`:

```json
{
  "mcpServers": {
    "pawndex": {
      "command": "uv",
      "args": ["--directory", "/path/to/pawndex_mcp_server", "run", "pawndex_mcp_server"]
    }
  }
}
```

Or add via CLI:

```bash
gemini mcp add pawndex -- uv --directory /path/to/pawndex_mcp_server run pawndex_mcp_server
```

</details>

<details>
<summary><b>OpenAI Codex CLI</b> — config via <code>~/.codex/config.toml</code></summary>

Add to your `~/.codex/config.toml` or project-scoped `.codex/config.toml`:

```toml
[mcp_servers.pawndex]
command = "uv"
args = ["--directory", "/path/to/pawndex_mcp_server", "run", "pawndex_mcp_server"]
```

Or add via CLI:

```bash
codex mcp add pawndex -- uv --directory /path/to/pawndex_mcp_server run pawndex_mcp_server
```

</details>

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
