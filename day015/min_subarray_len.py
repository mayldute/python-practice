"""
Minimum Size Subarray Sum

Given a positive target and a list of positive integers, find the
minimum length of a contiguous subarray whose sum is greater than
or equal to the target.

Return 0 if no such subarray exists.

The solution uses a sliding window:
    - Expand the window by moving the right pointer.
    - Shrink the window from the left while its sum is valid.
    - Track the smallest valid window length.
"""


def min_subarray_len(target: int, nums: list[int]) -> int:
    left = 0
    current_sum = 0
    min_len = None

    for right in range(len(nums)):
        current_sum += nums[right]

        while current_sum >= target:
            current_len = right - left + 1

            if min_len is None:
                min_len = current_len
            else:
                min_len = min(min_len, current_len)

            current_sum -= nums[left]
            left += 1

    if min_len is None:
        return 0

    return min_len
