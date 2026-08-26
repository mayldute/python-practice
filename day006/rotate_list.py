"""
Task:
Rotate a list to the right by a given number of positions.

Requirements:
- Return a new list.
- Do not modify the original list.
- Move elements from the end of the list to the beginning.
- If k is larger than the list length, wrap around.
- Return [] for an empty list.
- Do not use collections.deque.
"""


def rotate_right(items: list[int], k: int) -> list[int]:
    if not items:
        return []

    k %= len(items)

    return items[-k:] + items[:-k]
