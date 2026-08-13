"""
Task:
Move all zeros to the end of a list.

Requirements:
- Return a new list with all zeros moved to the end.
- Preserve the relative order of all non-zero elements.
- Preserve the number of zeros.
- Do not modify the original list.
- Do not use sorted() or list.sort().
- Do not use .count(0).
- Aim for O(n) time complexity.
"""

def move_zeros(items: list[int]) -> list[int]:
    zeros = []
    nums = []

    for item in items:
        if item == 0:
            zeros.append(item)
        else:
            nums.append(item)

    return nums + zeros
