"""
Task:
Merge overlapping intervals.

Requirements:
- Each interval is represented as [start, end].
- Merge intervals that overlap.
- Return a new list.
- Do not modify the original input.
- The result must be sorted by start value.
- Aim for O(n log n) time complexity.
"""


def merge_intervals(intervals: list[list[int]]) -> list[list[int]]:
    sorted_intervals = sorted(intervals)
    result = []

    for interval in sorted_intervals:
        if not result:
            result.append(interval.copy())
            continue

        current = result[-1]

        if interval[0] <= current[1]:
            current[1] = max(current[1], interval[1])
        else:
            result.append(interval.copy())

    return result
