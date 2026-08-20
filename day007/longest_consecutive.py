"""
Task:
Find the length of the longest sequence of consecutive integers.

Requirements:
- Return the length of the longest consecutive sequence.
- The numbers do not need to be adjacent in the original list.
- Duplicate values should be ignored.
- Return 0 for an empty list.
- Do not modify the original list.
- Aim for O(n) time complexity.
"""


def longest_consecutive(items: list[int]) -> int:
    if not items:
        return 0

    numbers = set(items)
    max_count = 0

    for num in numbers:
        if num - 1 not in numbers:
            current_num = num
            count = 1

            while current_num + 1 in numbers:
                current_num += 1
                count += 1

        max_count = max(max_count, count)
        
    return max_count
