"""
Task:
Find the second largest unique integer in a list.

Requirements:
- Return the second largest unique integer.
- Duplicate values should not affect the result.
- Return None if there are fewer than two unique values.
- Do not use sorted() or list.sort().
- Do not use set().
- Do not modify the original list.
- Traverse the list only once.
- Aim for O(n) time complexity.
- Aim for O(1) additional space.
"""


def second_largest(items: list[int]) -> int | None:

    if len(items) < 2:
        return None

    largest = items[0]
    second = None

    for item in items[1:]:
        if item < largest and (second is None or item > second):
            second = items[i]
        elif item > largest:
            second = largest
            largest = item

    return second
