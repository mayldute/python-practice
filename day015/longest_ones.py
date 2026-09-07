"""
Longest Consecutive Ones

Given a list containing only 0s and 1s, find the maximum number of
consecutive 1s.

Return 0 if the list is empty or contains no 1s.

When a 0 is encountered, the current sequence is reset.
"""


def longest_ones(nums: list[int]) -> int:
    current_len = 0
    max_len = 0

    for num in nums:
        if num == 0:
            current_len = 0
        else:
            current_len += 1
            max_len = max(max_len, current_len)

    return max_len
