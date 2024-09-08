from fastapi import status


class AppError(Exception):
    def __init__(self, message: str, error_code=status.HTTP_500_INTERNAL_SERVER_ERROR):
        super().__init__(message)
        self.error_code = error_code
        self.message = message

    def __str__(self):
        if self.error_code:
            return f"[Error {self.error_code}] {super().__str__()}"
        return super().__str__()


class ErrorNotFound(AppError):
    def __init__(self, message: str = 'data not found', error_code=status.HTTP_404_NOT_FOUND):
        super().__init__(message, error_code)


class ErrorInvalidInput(AppError):
    def __init__(self, message: str = 'invalid user input', error_code=status.HTTP_400_BAD_REQUEST):
        super().__init__(message, error_code)
