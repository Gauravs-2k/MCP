"""
Registry for tracking and accessing MCPs.
"""


class MCPRegistry:
    """Registry for all MCPs in the system."""
    
    _mcps = {}
    
    @classmethod
    def register(cls, mcp):
        """
        Register a new MCP.
        
        Args:
            mcp: The MCP instance to register
            
        Returns:
            The registered MCP
        """
        cls._mcps[mcp.name] = mcp
        return mcp
    
    @classmethod
    def get(cls, name):
        """
        Get an MCP by name.
        
        Args:
            name: The name of the MCP to retrieve
            
        Returns:
            The MCP instance or None if not found
        """
        return cls._mcps.get(name)
    
    @classmethod
    def list(cls):
        """
        List all registered MCPs.
        
        Returns:
            A list of MCP names
        """
        return list(cls._mcps.keys())
    
    @classmethod
    def remove(cls, name):
        """
        Remove an MCP from the registry.
        
        Args:
            name: The name of the MCP to remove
            
        Returns:
            The removed MCP or None if not found
        """
        return cls._mcps.pop(name, None)
