"""
Task:
Find the length of the longest contiguous subarray whose elements sum exactly to k.

Requirements:
- Return the length of the longest valid subarray.
- The elements must be contiguous in the original list.
- Return 0 if no such subarray exists.
- Do not modify the original list.
- The solution should work correctly with the given constraints on the input values.
"""


def longest_subarray_sum(items: list[int], k: int) -> int:
    runing_sum = 0
    sums = {0: -1}
    current_len = 0
    max_len = 0

    for idx in range(len(items)):
        runing_sum += items[idx]

        if runing_sum not in sums:
            sums[runing_sum] = idx

        needed_sum = runing_sum - k

        if needed_sum in sums:
            start_idx = sums[needed_sum]
            current_len = idx - start_idx
            max_len = max(max_len, current_len)

    return max_len
