import ast

def get_function_definitions(node):
    """
    Extracts all function definitions from a given AST node.

    Args:
        node (ast.AST): The AST node to analyze.

    Returns:
        list[ast.FunctionDef]: A list of ast.FunctionDef objects representing functions.
    """
    return [n for n in ast.walk(node) if isinstance(n, ast.FunctionDef)]

def get_class_definitions(node):
    """
    Extracts all class definitions from a given AST node.

    Args:
        node (ast.AST): The AST node to analyze.

    Returns:
        list[ast.ClassDef]: A list of ast.ClassDef objects representing classes.
    """
    return [n for n in ast.walk(node) if isinstance(n, ast.ClassDef)]

def get_docstring(node):
    """
    Extracts the docstring of a given AST node.

    Args:
        node (ast.AST): The AST node to analyze.

    Returns:
        str: The docstring, or None if no docstring is present.
    """
    return ast.get_docstring(node)

def get_imports(node):
    """
    Extracts all import statements from a given AST node.

    Args:
        node (ast.AST): The AST node to analyze.

    Returns:
        list[ast.Import, ast.ImportFrom]: A list of import statements.
    """
    return [n for n in ast.walk(node) if isinstance(n, (ast.Import, ast.ImportFrom))]

# Additional utility functions can be added as needed
