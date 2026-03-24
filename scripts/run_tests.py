#!/usr/bin/env python3
"""
Run all tests for the Hello World project.
"""

import subprocess
import sys
from pathlib import Path

def main():
    """Execute pytest on the tests directory."""
    tests_dir = Path(__file__).parent.parent / "tests"
    result = subprocess.run(
        [sys.executable, "-m", "pytest", str(tests_dir), "-v"],
        cwd=Path(__file__).parent.parent
    )
    sys.exit(result.returncode)

if __name__ == "__main__":
    main()
