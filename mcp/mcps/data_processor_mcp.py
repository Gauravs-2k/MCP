"""
An MCP for processing data.
"""
from mcp.core.base_mcp import BaseMCP


class DataProcessorMCP(BaseMCP):
    """An MCP that processes data according to configured rules."""
    
    def __init__(self, name, config=None):
        super().__init__(name, config)
    
    def process(self):
        """
        Process data according to the configured rules.
        
        Returns:
            dict: The processing results
        """
        data = self.config.get('data', [])
        operation = self.config.get('operation', 'sum')
        
        if operation == 'sum':
            result = sum(data)
        elif operation == 'average':
            result = sum(data) / len(data) if data else 0
        elif operation == 'max':
            result = max(data) if data else None
        elif operation == 'min':
            result = min(data) if data else None
        else:
            result = None
            
        return {
            'operation': operation,
            'data': data,
            'result': result
        }
    
    def validate_config(self):
        """
        Validate the configuration.
        
        Returns:
            bool: True if the configuration is valid, False otherwise
        """
        if 'data' not in self.config:
            return False
        
        if not isinstance(self.config['data'], list):
            return False
            
        operation = self.config.get('operation', 'sum')
        valid_operations = ['sum', 'average', 'max', 'min']
        
        return operation in valid_operations
