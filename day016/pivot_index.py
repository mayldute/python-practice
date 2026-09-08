"""
Find the leftmost pivot index in a list of integers.

A pivot index is an index where the sum of all elements strictly
to the left equals the sum of all elements strictly to the right.
The pivot element itself must not be included in either sum.

Requirements:
- Return the leftmost valid pivot index.
- Return -1 if no pivot index exists.
- Return -1 for an empty list.
- Handle positive, negative, and zero values.

Examples:
- [1, 7, 3, 6, 5, 6] -> 3
- [1, 2, 3] -> -1
- [2, 1, -1] -> 0
- [0, 0, 0, 0] -> 0
- [] -> -1
"""


def pivot_index_v1(nums: list[int]) -> int:
    for idx in range(len(nums)):
        if sum(nums[:idx]) == sum(nums[idx + 1 :]):
            return idx

    return -1


def pivot_index_v2(nums: list[int]) -> int:
    total_sum = sum(nums)
    left_sum = 0

    for idx in range(len(nums)):
        right_sum = total_sum - left_sum - nums[idx]

        if left_sum == right_sum:
            return idx

        left_sum += nums[idx]

    return -1
