"""
Import colorama library
"""
from colorama import init

# Initiaate Colorama
init(autoreset=True)


class Color:
    """
    Colors to be used in run.py for text highlighting
    """
    YELLOW = "\033[1;33;48m"
    RED = "\033[1;31;48m"
    GREEN = "\033[1;32;48m"
    BLUE = "\033[1;34;48m"
