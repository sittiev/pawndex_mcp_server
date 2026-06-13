# Contributing to PawnDex MCP Server

First off, thank you for considering contributing to the PawnDex MCP Server! It's people like you that make the Pawn ecosystem better.

## How Can I Contribute?

### Reporting Bugs
- Use GitHub Issues to report bugs.
- Describe the steps to reproduce the issue.
- Include information about your environment (Python version, MCP host).

### Suggesting Enhancements
- Open an issue with the "enhancement" label.
- Explain why this enhancement would be useful.

### Pull Requests
1. Fork the repo and create your branch from `main`.
2. If you've added code that should be tested, add tests.
3. Ensure the test suite passes (`uv run pytest`).
4. Follow the existing code style.

## Development Setup

```bash
uv sync --all-extras
uv run pawndex_mcp_server
```

## License
By contributing, you agree that your contributions will be licensed under its MIT License.
