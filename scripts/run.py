#!/usr/bin/env python3
"""
Run the Hello World application.

This script imports and executes the main function from the hello module.
"""

import sys
from pathlib import Path

# Add src directory to Python path
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from hello import main

if __name__ == "__main__":
    main()
