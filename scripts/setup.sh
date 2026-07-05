#!/bin/bash
set -euo pipefail
echo "Setting up MCP Agent..."
pip install -e ".[dev]"
echo "Setup complete!"
