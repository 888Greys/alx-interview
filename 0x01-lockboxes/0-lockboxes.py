#!/usr/bin/python3
from collections import deque


def canUnlockAll(boxes):
    # craete a set to keep track of visited boxes
    visited = set()
    # initializes a queue with the first box

    queue = deque([0])

    while queue:
        current_box = queue.popleft()

        # mark the current box as visited

        visited.add(current_box)

        for key in boxes[current_box]:

            if key < len(boxes) and key not in visited:

                queue.append(key)

        return len(visited) == len(boxes)
