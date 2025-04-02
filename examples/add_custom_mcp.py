"""
Example of how to create and add a custom MCP.
"""
from mcp.core.base_mcp import BaseMCP
from mcp.core.mcp_registry import MCPRegistry


# Create a custom MCP class
class CustomMCP(BaseMCP):
    def __init__(self, name, config=None):
        super().__init__(name, config)
    
    def process(self):
        input_text = self.config.get('input', '')
        operation = self.config.get('operation', 'uppercase')
        
        if operation == 'uppercase':
            return input_text.upper()
        elif operation == 'lowercase':
            return input_text.lower()
        elif operation == 'reverse':
            return input_text[::-1]
        else:
            return input_text


def main():
    # Create instance of your custom MCP
    custom_mcp = CustomMCP("text_transformer", {
        "input": "Hello World",
        "operation": "uppercase"
    })
    
    # Register your MCP
    MCPRegistry.register(custom_mcp)
    
    # Use your MCP
    result = custom_mcp.process()
    print(f"Result from custom MCP: {result}")
    
    # Change the configuration and process again
    custom_mcp.config["operation"] = "reverse"
    result = custom_mcp.process()
    print(f"Result after changing operation: {result}")


if __name__ == "__main__":
    main()
