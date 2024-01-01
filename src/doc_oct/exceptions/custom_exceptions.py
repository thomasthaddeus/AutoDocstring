class DocOctError(Exception):
    """Base class for other exceptions in doc_oct."""
    pass

class FileReadError(DocOctError):
    """Raised when an error occurs in reading a file."""
    def __init__(self, file_path, message="Failed to read file"):
        self.file_path = file_path
        self.message = f"{message}: {file_path}"
        super().__init__(self.message)

class FileWriteError(DocOctError):
    """Raised when an error occurs in writing to a file."""
    def __init__(self, file_path, message="Failed to write to file"):
        self.file_path = file_path
        self.message = f"{message}: {file_path}"
        super().__init__(self.message)

class CodeAnalysisError(DocOctError):
    """Raised when an error occurs during code analysis."""
    def __init__(self, file_path, message="Error analyzing code"):
        self.file_path = file_path
        self.message = f"{message}: {file_path}"
        super().__init__(self.message)

class DocstringGenerationError(DocOctError):
    """Raised when an error occurs in generating a docstring."""
    def __init__(self, file_path, message="Error generating docstring"):
        self.file_path = file_path
        self.message = f"{message}: {file_path}"
        super().__init__(self.message)

class InvalidFilePathError(DocOctError):
    """Raised when the provided file path is invalid or does not exist."""
    def __init__(self, file_path, message="Invalid or non-existent file path"):
        self.file_path = file_path
        self.message = f"{message}: {file_path}"
        super().__init__(self.message)

class ParsingError(DocOctError):
    """Raised when parsing of the code fails."""
    def __init__(self, file_path, message="Failed to parse the code"):
        self.file_path = file_path
        self.message = f"{message}: {file_path}"
        super().__init__(self.message)

class NLPProcessingError(DocOctError):
    """Raised during failures in natural language processing tasks."""
    def __init__(self, message="NLP processing error"):
        self.message = message
        super().__init__(self.message)

class ModelLoadingError(DocOctError):
    """Raised when machine learning or NLP models fail to load."""
    def __init__(self, model_name, message="Failed to load model"):
        self.model_name = model_name
        self.message = f"{message}: {model_name}"
        super().__init__(self.message)

class DependencyResolutionError(DocOctError):
    """Raised when there is an issue with resolving dependencies."""
    def __init__(self, dependency_name, message="Failed to resolve dependency"):
        self.dependency_name = dependency_name
        self.message = f"{message}: {dependency_name}"
        super().__init__(self.message)

# Additional custom exceptions can be added as needed
