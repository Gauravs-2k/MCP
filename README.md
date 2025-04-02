# MCP (Master Control Program) Framework

A flexible Python framework for creating and managing multiple Master Control Programs (MCPs).

## Features

- Register and manage multiple MCPs
- Easy-to-extend base MCP class
- Simple API for adding new MCP implementations
- Support for running MCPs with different configurations

## Getting Started

```bash
# Install dependencies
pip install -r requirements.txt

# Run an example
python examples/run_mcp.py
```

## Adding a New MCP

Create a new Python file in the `mcp/mcps/` directory that inherits from `BaseMCP`:

```python
from mcp.core.base_mcp import BaseMCP

class MyCustomMCP(BaseMCP):
    def __init__(self, name, config):
        super().__init__(name, config)
    
    def process(self):
        # Implement your MCP logic here
        return "Result from MyCustomMCP"
```

Then register it using the MCP registry:

```python
from mcp.core.mcp_registry import MCPRegistry
from mcp.mcps.my_custom_mcp import MyCustomMCP

# Create and register your MCP
my_mcp = MyCustomMCP("custom_mcp", {"param": "value"})
MCPRegistry.register(my_mcp)

# Get and run your MCP
mcp = MCPRegistry.get("custom_mcp")
result = mcp.process()
print(result)