"""
Example script for running MCPs.
"""
from mcp.core.mcp_registry import MCPRegistry
from mcp.mcps.example_mcp import ExampleMCP
from mcp.mcps.data_processor_mcp import DataProcessorMCP


def main():
    # Create and register a simple example MCP
    example = ExampleMCP("example", {"message": "Custom message from example MCP"})
    MCPRegistry.register(example)
    
    # Create and register a data processor MCP
    data_processor = DataProcessorMCP("data_processor", {
        "data": [1, 2, 3, 4, 5],
        "operation": "average"
    })
    MCPRegistry.register(data_processor)
    
    # List all registered MCPs
    print("Registered MCPs:", MCPRegistry.list())
    
    # Run the example MCP
    example_mcp = MCPRegistry.get("example")
    example_result = example_mcp.process()
    print(f"Result from example MCP: {example_result}")
    
    # Run the data processor MCP
    processor_mcp = MCPRegistry.get("data_processor")
    processor_result = processor_mcp.process()
    print(f"Result from data processor MCP: {processor_result}")


if __name__ == "__main__":
    main()
