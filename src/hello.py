"""
Hello World Module

Provides a simple Hello World implementation with configurable greeting.
"""

__version__ = "1.0.0"


def greet(name: str = "World") -> str:
    """
    Return a greeting message.

    Args:
        name (str): The name to greet. Defaults to "World".

    Returns:
        str: A friendly greeting message.

    Example:
        >>> greet()
        'Hello, World!'
        >>> greet("Alice")
        'Hello, Alice!'
    """
    return f"Hello, {name}!"


def main():
    """Main entry point for the hello world application."""
    print(greet())


if __name__ == "__main__":
    main()
