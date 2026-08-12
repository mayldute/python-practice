"""
Task:
Find the missing number in a sequence.

Requirements:
- The list contains unique integers from 0 to n.
- Exactly one number from the sequence is missing.
- Return the missing number.
- Do not use set().
- Do not use sorted() or list.sort().
- Do not modify the original list.
- Aim for O(n) time complexity.
- Aim for O(1) additional space.
"""

def find_missing(items: list[int]) -> int:
    n = len(items) + 1
    expected_sum = 0
    actual_sum = 0
    
    for i in range(n):
        expected_sum += i

    for j in items:
        actual_sum += j

    return expected_sum - actual_sum


def find_missing_alternative(items: list[int]) -> int:
    expected_sum = sum(range(len(items) + 1))
    actual_sum = sum(items)

    return expected_sum - actual_sum
