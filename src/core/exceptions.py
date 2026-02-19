class CustomException(Exception):
    """Base class for other exceptions"""
    pass

class FileNotFound(CustomException):
    """Raised when a file is not found in the system"""
    pass

class PermissionDenied(CustomException):
    """Raised when permission is denied"""
    pass

class InvalidConfiguration(CustomException):
    """Raised for invalid configuration settings"""
    pass

class TimeoutError(CustomException):
    """Raised when an operation times out"""
    pass