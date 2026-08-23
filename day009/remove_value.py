"""
Task:
Implement a function that removes all occurrences of a given value from a list.

Requirements:
- Create a `remove_value` function.
- The function accepts a list of integers and a value to remove.
- Remove every occurrence of the given value.
- Preserve the order of the remaining elements.
- Return a new list.
- Do not modify the original list.

Examples:
    [1, 2, 3, 2, 4], 2 → [1, 3, 4]
    [5, 5, 1, 5, 2], 5 → [1, 2]
    [1, 2, 3], 7 → [1, 2, 3]
    [], 5 → []
"""


def remove_value(items: list[int], value: int) -> list[int]:
    return [item for item in items if item != value]
