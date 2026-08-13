"""
Task:
Merge two sorted lists into one sorted list.

Requirements:
- Both input lists are already sorted in ascending order.
- Return a new sorted list containing all elements from both lists.
- Preserve duplicate values.
- Do not modify the original lists.
- Do not use sorted() or list.sort().
- Aim for O(n + m) time complexity.
"""


def merge_sorted(first: list[int], second: list[int]) -> list[int]:
    result = []
    i = 0
    j = 0

    while i < len(first) and j < len(second):
        if first[i] <= second[j]:
            result.append(first[i])
            i += 1
        else:
            result.append(second[j])
            j += 1

    result.extend(first[i:])
    result.extend(second[j:])

    return result
