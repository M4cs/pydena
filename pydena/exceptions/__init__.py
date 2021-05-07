from pydantic import BaseModel

class Error(Exception):
    """Base Class for other exceptions"""
    pass

class RPCError(Error):
    """Exception raised for RPC error response
    
    Attributes:
        code(int): Error Code from RPC
        message(str): Error Message from RPC
    
    """
    def __init__(self, error: dict):
        self.message = error.get('error').get('message')
        self.code = error.get('error').get('code')
