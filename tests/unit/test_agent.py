"""MCP Agent - Unit Tests."""

import pytest
from src.agent.tools import AgentTools


@pytest.mark.asyncio
async def test_discover_servers():
    """Test Discover available MCP servers and their capabilities."""
    tools = AgentTools()
    result = await tools.discover_servers(registry_url="test", filter_tags="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_connect_server():
    """Test Establish connection to an MCP server with authentication."""
    tools = AgentTools()
    result = await tools.connect_server(server_url="test", transport="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_list_tools():
    """Test List available tools from connected MCP servers."""
    tools = AgentTools()
    result = await tools.list_tools(server_id="test", category="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_invoke_tool():
    """Test Invoke a tool on a connected MCP server."""
    tools = AgentTools()
    result = await tools.invoke_tool(server_id="test", tool_name="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_agent_initialization():
    """Test that the agent initializes correctly."""
    from src.agent.mcp_agent_agent import McpAgentAgent
    agent = McpAgentAgent()
    assert agent.agent_id is not None
    assert agent._system_prompt is not None
    assert len(agent._tool_dispatch) > 0
