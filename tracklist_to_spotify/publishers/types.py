"""
Publisher agnostic types to be used across publishers
"""

from typing import TypedDict

class GenericTrackDetails(TypedDict):
    artist: str
    title: str
