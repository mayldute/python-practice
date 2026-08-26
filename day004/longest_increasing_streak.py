"""
Task:
Find the length of the longest continuously increasing streak.

Requirements:
- Return the length of the longest sequence of consecutive elements
  where each element is greater than the previous one.
- The elements must be next to each other in the original list.
- Equal values break the streak.
- Return 0 for an empty list.
- Do not sort the list.
- Do not modify the original list.
- Aim for O(n) time complexity.
- Aim for O(1) additional space.
"""


def longest_increasing_streak(items: list[int]) -> int:
    if not items:
        return 0

    max_count = 1
    current_count = 1

    for i in range(1, len(items)):
        if items[i - 1] < items[i]:
            current_count += 1
            max_count = max(max_count, current_count)
        else:
            current_count = 1

    return max_count
