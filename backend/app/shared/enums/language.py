"""
Shared Enums — Programming language identifiers.
"""

from enum import StrEnum


class ProgrammingLanguage(StrEnum):
    """Supported source code languages."""
    PYTHON = "python"
    TYPESCRIPT = "typescript"
    JAVASCRIPT = "javascript"
    JAVA = "java"
    CPP = "cpp"
    UNKNOWN = "unknown"
