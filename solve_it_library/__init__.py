"""
SOLVE-IT Knowledge Base Library (`solve_it_library`)

This package provides programmatic access to the SOLVE-IT knowledge base data.
"""

from .solveit_library import KnowledgeBase, SOLVEITDataError

__all__ = ["KnowledgeBase", "SOLVEITDataError"]
