"""
Task:
Implement a function that finds the unique values shared by two lists.

Requirements:
- Create a `find_common_items` function.
- Accept two lists of integers.
- Return values that appear in both lists.
- Each value should appear only once in the result.
- Preserve the order in which values first appear in `first`.
- Do not modify either input list.
- Return an empty list if the lists have no common values.

Examples:
    [1, 2, 3, 4], [3, 4, 5] → [3, 4]
    [4, 1, 2, 1], [1, 4, 7] → [4, 1]
    [1, 2, 3], [5, 6] → []

Optimization:
- Use a `set` for fast membership checks.
- Use a separate `set` to track values already added to the result.
"""


def find_common_items(first: list[int], second: list[int]) -> list[int]:
    result = []
    seen = set()
    second_set = set(second)

    for number in first:
        if number in second_set and number not in seen:
            result.append(number)
            seen.add(number)

    return result
