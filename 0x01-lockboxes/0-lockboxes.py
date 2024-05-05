#!/usr/bin/python3
"""
Solution to lockboxex
"""
from collections import deque


def canUnlockAll(boxes):
    """
    Determining weather a series of boxes can be opened
    """
    if (type(boxes)) is not list:
        return False
    elif (len(boxes)) == 0:
        return False

    for k in range(1, len(boxes) - 1):
        boxes_checked = k in boxes[idx] and k != idx
        if boxes_checked:
            break
        if boxes_checked is False:
            return boxes_checked
    return True
