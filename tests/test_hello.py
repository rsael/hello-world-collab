"""
Unit tests for the hello module.
"""

import pytest
from hello import greet, main


def test_greet_default():
    """Test greeting with default name."""
    result = greet()
    assert result == "Hello, World!"


def test_greet_custom_name():
    """Test greeting with custom name."""
    result = greet("Alice")
    assert result == "Hello, Alice!"


def test_greet_empty_string():
    """Test greeting with empty string."""
    result = greet("")
    assert result == "Hello, !"


def test_main(capsys):
    """Test main function output."""
    main()
    captured = capsys.readouterr()
    assert captured.out.strip() == "Hello, World!"


@pytest.mark.parametrize("name,expected", [
    ("Bob", "Hello, Bob!"),
    ("Eve", "Hello, Eve!"),
    ("Multi-Agent", "Hello, Multi-Agent!"),
])
def test_greet_multiple_names(name, expected):
    """Parametrized test for various names."""
    assert greet(name) == expected
