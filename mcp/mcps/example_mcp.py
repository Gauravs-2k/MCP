"""
Example MCP implementation.
"""
from mcp.core.base_mcp import BaseMCP


class ExampleMCP(BaseMCP):
    """An example MCP implementation."""
    
    def __init__(self, name, config=None):
        super().__init__(name, config)
    
    def process(self):
        """
        Process data according to this MCP's logic.
        
        Returns:
            str: A message indicating the processing was completed
        """
        # Get a parameter from the config with a default value
        message = self.config.get('message', 'Hello from ExampleMCP!')
        return f"{message} (processed by {self.name})"
    
    def validate_config(self):
        """
        Validate that the config contains expected parameters.
        
        Returns:
            bool: True if the configuration is valid, False otherwise
        """
        # This is just a simple example, you can make this as complex as needed
        return True
