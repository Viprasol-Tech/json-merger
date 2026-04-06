"""
json-merger - Merge multiple JSON objects intelligently

Part of Viprasol Utilities: https://viprasol.com
"""

__version__ = "0.1.0"
__author__ = "Viprasol"
__email__ = "hello@viprasol.com"

from .core import JsonMerger, merge, process, main

__all__ = ["JsonMerger", "merge", "process", "main"]
