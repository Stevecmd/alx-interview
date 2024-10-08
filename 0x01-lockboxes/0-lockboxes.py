#!/usr/bin/python3
"""
This module contains a function that determines if all boxes can be opened.
"""

def canUnlockAll(boxes):
    """Determines if all boxes can be opened."""
    unlocked = [False] * len(boxes)  # Track unlocked boxes
    unlocked[0] = True  # The first box is unlocked
    keys = boxes[0]  # Start with keys from the first box

    for key in keys:
        if key < len(boxes) and not unlocked[key]:
            unlocked[key] = True  # Unlock the box with the key
            keys.extend(boxes[key])  # Add new keys from the unlocked box

    return all(unlocked)  # Return True if all boxes are unlocked
