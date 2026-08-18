"""
Task:
Flatten a list containing nested lists of integers.

Requirements:
- Convert a nested list into a single flat list.
- Preserve the original order of elements.
- Support arbitrary nesting depth.
- Do not use external libraries.
- Do not modify the original input.
- Return a new list.
"""


def flatten(items: list) -> list[int]:
    result = []

    for item in items:
        if isinstance(item, list):
            result.extend(flatten(item))
        else:
            result.append(item)

    return result
