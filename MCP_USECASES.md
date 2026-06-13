# PawnDex MCP Server: Common Use Cases & Examples

This document provides AI agents with context and examples on how to effectively use the tools provided by the PawnDex MCP server.

## 1. Package Discovery

When looking for libraries, plugins, or scripts for the Pawn ecosystem.

*   **Search for a specific topic:**
    `search_packages({"q": "mysql"})`
*   **Find official packages:**
    `search_packages({"q": "is:official"})`
*   **Filter by label (e.g., plugins):**
    `search_packages({"q": "label:plugin"})`
*   **Search by user/organization:**
    `search_packages({"q": "user:openmultiplayer"})`

## 2. Package Inspection

Get detailed information about a package to evaluate its suitability.

### `get_package`
Retrieves comprehensive details including description, stars, forks, tags, and the latest release notes.

*   `get_package({"owner": "pawn-lang", "repo": "samp-stdlib"})`

## 3. Global Insights

Understand the scale and variety of the Pawn ecosystem.

### `get_stats`
View total counts of packages, users, stars, and downloads across the entire index.

### `get_languages`
See which languages are supported and indexed in PawnDex (e.g., English, Portuguese, etc.).

## Example Workflow for AI Agents

1.  **Requirement:** User wants a MySQL library for open.mp.
2.  **Step 1:** `search_packages({"q": "mysql", "sort": "stars"})` to find popular options.
3.  **Step 2:** `get_package({"owner": "NullSablex", "repo": "mysql_samp"})` to check release notes and features of a top candidate.
4.  **Step 3:** Summarize the findings to the user, highlighting why the selected package is a good fit.
