import logging
from typing import Any, Optional

import httpx
from fastmcp import FastMCP

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("pawndex_mcp_server")

# Initialize FastMCP server
mcp = FastMCP("PawnDex")

BASE_URL = "https://packages.open.mp/api/v1"


async def fetch_api(endpoint: str, params: Optional[dict] = None) -> Any:
    """Helper to fetch data from the PawnDex API."""
    headers = {"User-Agent": "PawnDex-MCP-Server/0.1.0"}
    async with httpx.AsyncClient(timeout=30.0, headers=headers) as client:

        url = f"{BASE_URL}/{endpoint}"
        logger.info(f"Fetching: {url} with params: {params}")
        try:
            response = await client.get(url, params=params)
            response.raise_for_status()
            return response.json()
        except httpx.HTTPStatusError as e:
            logger.error(
                f"HTTP error occurred: {e.response.status_code} - {e.response.text}"
            )
            raise RuntimeError(f"API error: {e.response.status_code}")
        except Exception as e:
            logger.error(f"An error occurred: {str(e)}")
            raise RuntimeError(f"Connection error: {str(e)}")


@mcp.tool()
async def search_packages(
    q: Optional[str] = None,
    sort: str = "best",
    direction: str = "desc",
    limit: int = 20,
    page: int = 1,
) -> str:
    """
    Search for Pawn packages on PawnDex.

    Args:
        q: Search query (e.g. 'mysql', 'is:official', 'user:openmultiplayer', 'label:plugin').
        sort: Field to sort by: 'stars', 'updated', or 'best'.
        direction: Sort direction: 'asc' or 'desc'.
        limit: Number of items to return (max 100).
        page: Page number for pagination.
    """
    params = {
        "q": q,
        "sort": sort,
        "dir": direction,
        "limit": min(limit, 100),
        "page": page,
    }
    # Remove None values
    params = {k: v for k, v in params.items() if v is not None}

    data = await fetch_api("packages", params=params)

    if not data.get("items"):
        return "No packages found matching the criteria."

    results = []
    for item in data["items"]:
        results.append(
            f"- **{item['user']}/{item['repo']}** ({item['stars']} ⭐)\n"
            f"  Description: {item.get('description', 'No description')}\n"
            f"  Labels: {', '.join(item.get('labels', []))}\n"
            f"  Updated: {item.get('updated', 'Unknown')}"
        )

    header = f"Found {len(data['items'])} packages (Page {page}):\n\n"
    footer = ""
    if data.get("hasNext"):
        footer = f"\n\n*Use page={page + 1} to see more results.*"

    return header + "\n".join(results) + footer


@mcp.tool()
async def get_package(owner: str, repo: str) -> str:
    """
    Get detailed information about a specific Pawn package.

    Args:
        owner: The GitHub username or organization (e.g. 'pawn-lang').
        repo: The repository name (e.g. 'samp-stdlib').
    """
    data = await fetch_api(f"packages/{owner}/{repo}")

    details = [
        f"# {data['user']}/{data['repo']}",
        f"**Description:** {data.get('description', 'No description')}",
        f"**Stars:** {data['stars']} | **Forks:** {data['forks']}",
        f"**Classification:** {data.get('classification', 'N/A')} | **Type:** {data.get('type', 'N/A')}",
        f"**Primary Language:** {data.get('primaryLanguage', 'N/A')}",
        f"**Updated:** {data.get('updated', 'N/A')}",
    ]

    if data.get("topics"):
        details.append(f"**Topics:** {', '.join(data['topics'])}")

    if data.get("labels"):
        details.append(f"**Labels:** {', '.join(data['labels'])}")

    if data.get("tags"):
        details.append(
            f"**Available Tags:** {', '.join(data['tags'][:10])}{'...' if len(data['tags']) > 10 else ''}"
        )

    if data.get("releases"):
        latest = data["releases"][0]
        details.append("\n## Latest Release")
        details.append(
            f"**Tag:** {latest.get('tag', 'N/A')} | **Name:** {latest.get('name', 'N/A')}"
        )
        if latest.get("body"):
            body = latest["body"][:500] + ("..." if len(latest["body"]) > 500 else "")
            details.append(f"\n{body}")

    return "\n".join(details)


@mcp.tool()
async def get_stats() -> str:
    """Get global statistics for the PawnDex index."""
    data = await fetch_api("stats")

    stats = [
        "# PawnDex Global Statistics",
        f"- **Total Packages:** {data.get('packageCount', 'N/A')}",
        f"- **Total Users:** {data.get('userCount', 'N/A')}",
        f"- **Total Stars:** {data.get('starCount', 'N/A')}",
        f"- **Total Downloads:** {data.get('totalDownloads', 'N/A')}",
    ]
    return "\n".join(stats)


@mcp.tool()
async def get_languages() -> str:
    """Get the list of supported languages in PawnDex."""
    data = await fetch_api("languages")

    if not isinstance(data, list):
        return str(data)

    languages = [f"- {lang}" for lang in data]
    return "# Supported Languages\n\n" + "\n".join(languages)


def main():
    """Main entry point for the MCP server."""
    mcp.run()


if __name__ == "__main__":
    main()
