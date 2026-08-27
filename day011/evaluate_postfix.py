"""
Task:
Evaluate an arithmetic expression written in postfix notation.

Requirements:
- Accept a list of strings representing numbers and operators.
- Supported operators are "+", "-", "*", and "/".
- Numbers are integers.
- Each operator operates on the two preceding values.
- Division should use normal Python division.
- Return the final result as a float.
- The expression is guaranteed to be valid.
- The input contains at least one token.

Examples:
    ["2", "3", "+"] → 5.0
    ["5", "2", "-"] → 3.0
    ["4", "3", "*"] → 12.0
    ["8", "2", "/"] → 4.0
    ["2", "3", "+", "4", "*"] → 20.0
    ["5", "1", "2", "+", "4", "*", "+", "3", "-"] → 14.0
"""

import operator


def evaluate_postfix(items: list[str]) -> float:
    nums = []

    operators = {
        "+": operator.add,
        "-": operator.sub,
        "*": operator.mul,
        "/": operator.truediv,
    }

    for item in items:
        if item in operators:
            b = nums.pop()
            a = nums.pop()

            oper_res = operators[item](a, b)
            nums.append(oper_res)

        else:
            nums.append(float(item))

    return nums[0]
