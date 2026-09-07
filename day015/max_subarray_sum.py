"""
Maximum Subarray Sum

Given a list of integers, find the maximum possible sum of a contiguous
subarray.

A contiguous subarray must contain adjacent elements from the original list.
The subarray may contain positive numbers, negative numbers, or zero.

Requirements:
    - Return the maximum sum of any contiguous subarray.
    - Return 0 if the input list is empty.
    - Handle lists containing only negative numbers correctly.
    - Do not sort the list.
    - Aim for O(n) time complexity.
    - Use O(1) extra space.

Examples:
    [-2, 1, -3, 4, -1, 2, 1, -5, 4] → 6
    [5, 4, -1, 7, 8] → 23
    [-3, -2, -5] → -2
    [] → 0
"""


def max_subarray_sum(nums: list[int]) -> int:
    if not nums:
        return 0

    current_sum = nums[0]
    max_sum = nums[0]

    for num in nums[1:]:
        current_sum += num

        if current_sum < num:
            current_sum = num

        max_sum = max(max_sum, current_sum)

    return max_sum


def max_subarray_sum_alternative(nums: list[int]) -> int:
    if not nums:
        return 0

    current_sum = nums[0]
    max_sum = nums[0]

    for num in nums[1:]:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)

    return max_sum
