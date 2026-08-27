"""
Task:
For every element in a list, return the product of all other elements.

Requirements:
- Accept a list of integers.
- Return a new list with the same length.
- For each position, calculate the product of every element except
  the element at that position.
- Preserve the order of the input positions.
- Do not use division.
- The input contains at least one element.
- Zero values must be handled correctly.

Examples:
    [1, 2, 3, 4] → [24, 12, 8, 6]
    [2, 3, 4] → [12, 8, 6]
    [0, 1, 2] → [2, 0, 0]
    [0, 1, 0] → [0, 0, 0]
    [5] → [1]
"""


def product_except_self(numbers: list[int]) -> list[int]:
    result = []
    total = 1

    for num in range(len(numbers)):
        for n in numbers[num + 1 :]:
            total *= n

        for m in numbers[:num]:
            total *= m

        result.append(total)
        total = 1

    return result


def product_except_self_alternative(numbers: list[int]) -> list[int]:
    result = [1] * len(numbers)

    left_product = 1

    for i in range(len(numbers)):
        result[i] = left_product
        left_product *= numbers[i]

    right_product = 1

    for i in range(len(numbers) - 1, -1, -1):
        result[i] *= right_product
        right_product *= numbers[i]

    return result
