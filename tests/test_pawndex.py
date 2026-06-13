import pytest
from pawndex_mcp_server.server import search_packages, get_package, get_stats, get_languages

@pytest.mark.asyncio
async def test_search_packages():
    # Test with a common keyword
    result = await search_packages(q="mysql", limit=5)
    assert "Found" in result
    assert "mysql" in result.lower()

@pytest.mark.asyncio
async def test_get_package():
    # Test with a known package (from HAR)
    result = await get_package("NullSablex", "mysql_samp")
    assert "NullSablex/mysql_samp" in result
    assert "MySQL plugin" in result

@pytest.mark.asyncio
async def test_get_stats():
    result = await get_stats()
    assert "PawnDex Global Statistics" in result
    assert "Total Packages" in result

@pytest.mark.asyncio
async def test_get_languages():
    result = await get_languages()
    assert "Supported Languages" in result
    assert "English" in result
