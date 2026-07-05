# MCP Agent

[![CI](https://github.com/kogunlowo123/mcp-agent/actions/workflows/ci.yml/badge.svg)](https://github.com/kogunlowo123/mcp-agent/actions/workflows/ci.yml)
[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)

> **Category**: AI Engineering | **Cloud**: MULTI-CLOUD | **LLM**: gpt-4o

Model Context Protocol agent that manages MCP server connections, discovers and exposes tools and resources, handles protocol negotiation, and enables standardized AI-to-service communication across heterogeneous tool ecosystems.

---

## Domain-Specific Tools

| Tool | Description |
|------|-------------|
| `discover_servers` | Discover available MCP servers and their capabilities |
| `connect_server` | Establish connection to an MCP server with authentication |
| `list_tools` | List available tools from connected MCP servers |
| `invoke_tool` | Invoke a tool on a connected MCP server |
| `read_resource` | Read a resource exposed by an MCP server |

## API Endpoints

| Method | Path | Description |
|--------|------|-------------|
| `GET` | `/api/v1/mcp/servers/discover` | Discover MCP servers |
| `POST` | `/api/v1/mcp/servers/connect` | Connect to MCP server |
| `GET` | `/api/v1/mcp/tools` | List available tools |
| `POST` | `/api/v1/mcp/tools/invoke` | Invoke MCP tool |
| `GET` | `/api/v1/mcp/resources/{resource_uri}` | Read MCP resource |

## Features

- Server Management
- Tool Discovery
- Resource Exposure
- Protocol Negotiation
- Connection Pooling

## Integrations

- Mcp Stdio
- Mcp Sse
- Mcp Websocket
- Tool Registry
- Auth Provider

## Architecture

```
mcp-agent/
├── src/
│   ├── agent/              # Domain-specific agent logic
│   │   ├── mcp_agent_agent.py  # Main agent with domain tools
│   │   ├── tools.py        # 5 domain-specific tools
│   │   └── prompts.py      # Expert system prompts
│   ├── api/                # FastAPI routes
│   │   └── routes/
│   │       ├── domain.py   # 5 domain-specific endpoints
│   │       └── health.py   # Health check
│   ├── connectors/         # 5 integration connectors
│   ├── config/             # Settings and configuration
│   ├── models/             # Domain-specific Pydantic schemas
│   ├── rag/                # RAG pipeline
│   ├── mcp/                # MCP server
│   └── a2a/                # Agent-to-agent protocol
├── tests/
├── infrastructure/         # Terraform, K8s, Helm, Docker
├── dashboard/              # Next.js frontend
└── docs/                   # Architecture and deployment docs
```

## Quick Start

```bash
# Install
pip install -e ".[dev]"

# Run
make dev

# Test
make test

# Docker
docker compose up -d
```

## Primary Service

**MCP Protocol + MCP Servers + Tool Registries**

---

Built as part of the Enterprise AI Agent Platform.
