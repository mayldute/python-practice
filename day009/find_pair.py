"""
Task:
Implement a function that finds the first pair of numbers whose sum equals a target value.

Requirements:
- Create a `find_pair` function.
- The function accepts a list of integers and a target integer.
- The two numbers can be located anywhere in the list.
- The numbers must come from different positions.
- Duplicate values are allowed.
- Return the first valid pair found.
- If no valid pair exists, return `None`.
- Do not require the numbers to be next to each other.

Examples:
    [2, 7, 11, 15], 9 → (2, 7)
    [3, 2, 4], 6 → (2, 4)
    [1, 5, 3, 7], 10 → (3, 7)
    [1, 2, 3], 10 → None
    [5, 5], 10 → (5, 5)
"""


def find_pair(numbers: list[int], target: int) -> tuple[int, int] | None:
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] + numbers[j] == target:
                return (numbers[i], numbers[j])

    return None
