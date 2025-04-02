"""
Base class for all Master Control Programs (MCPs).
"""
from abc import ABC, abstractmethod


class BaseMCP(ABC):
    """Base class for all MCP implementations."""
    
    def __init__(self, name, config=None):
        """
        Initialize a new MCP.
        
        Args:
            name: A unique identifier for this MCP
            config: A dictionary of configuration parameters
        """
        self.name = name
        self.config = config or {}
        
    @abstractmethod
    def process(self):
        """
        Process data according to this MCP's logic.
        
        This method must be implemented by all subclasses.
        
        Returns:
            The result of the processing
        """
        pass
    
    def validate_config(self):
        """
        Validate the MCP's configuration.
        
        Returns:
            bool: True if the configuration is valid, False otherwise
        """
        return True
    
    def __str__(self):
        return f"MCP({self.name})"
