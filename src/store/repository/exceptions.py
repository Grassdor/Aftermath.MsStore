"""Common repository exceptions"""
from .error_codes import BASE, RECORD_NOT_FOUND


class UnknownRepositoryException(BaseException):
    """Base repository exception class"""

    def __init__(self, error_code: int = BASE):
        super().__init__()
        self.error_code = error_code

    def __str__(self) -> str:
        return f"UnknownRepositoryException [Code: {self.error_code}]: {super().__str__()}"


class NotFoundException(BaseException):
    """Handles not found cases when select records"""

    def __init__(self, error_code: int = RECORD_NOT_FOUND):
        super().__init__()
        self.error_code = error_code

    def __str__(self) -> str:
        return f"NotFoundException [Code: {self.error_code}]: {super().__str__()}"
