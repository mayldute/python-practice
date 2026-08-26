"""
Task:
Implement a function that counts consecutive duplicates in a list.

Requirements:
- Create a `count_consecutive_duplicates` function.
- The function accepts a list of integers.
- Count how many times an element is equal to the element immediately before it.
- Only consecutive duplicates count.
- If the same value appears multiple times but not consecutively, it does not count.
- Return the total number of consecutive duplicates.
- Return 0 if there are no consecutive duplicates.
- An empty list should return 0.

Examples:
    [1, 1, 2, 2, 2, 3] → 3
    [1, 2, 1, 1] → 1
    [1, 2, 3, 4] → 0
    [5, 5, 5, 5] → 3
    [] → 0
"""


def count_consecutive_duplicates(items: list[int]) -> int:
    count = 0

    for i in range(1, len(items)):
        if items[i] == items[i - 1]:
            count += 1

    return count
