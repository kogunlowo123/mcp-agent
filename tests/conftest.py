"""Test configuration for MCP Agent."""

import pytest


@pytest.fixture
def agent_config():
    return {"name": "mcp-agent", "category": "AI Engineering"}
