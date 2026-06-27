class FileProcessingError(Exception):
    """Base exception for file processing errors."""

    _error_code = 0

    def __init__(self, message=""):
        self.message = message
        super().__init__(self.message)


class UnsupportedFileTypeError(FileProcessingError):
    # Error code 1 - no matching processor found
    _error_code = 1

    def __init__(self, file_type=""):
        message = f"Unsupported file type: {file_type}" if file_type else "Unsupported file type"
        super().__init__(message)


class MalformedContentError(FileProcessingError):
    # Error code 2 - content doesn't match its declared format
    _error_code = 2

    def __init__(self, file_type="", detail=""):
        if detail:
            message = detail
        elif file_type:
            message = f"Invalid {file_type.upper()}"
        else:
            message = "Malformed content"
        super().__init__(message)


class EmptyContentError(FileProcessingError):
    # Error code 3 - nothing to parse
    _error_code = 3

    def __init__(self):
        super().__init__("File content cannot be empty")
