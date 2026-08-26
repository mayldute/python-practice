"""
Task:
Determine whether a string of brackets is valid.

Requirements:
- The string may contain (), {}, and [].
- Every opening bracket must have a matching closing bracket.
- Brackets must close in the correct order.
- Return True if the string is valid.
- Return False otherwise.
- Aim for O(n) time complexity.
"""


def is_valid_parentheses(text: str) -> bool:
    stack = []
    brackets = {")": "(", "]": "[", "}": "{"}

    for char in text:
        if char in brackets.values():
            stack.append(char)
        elif char in brackets:
            if stack and stack[-1] == brackets[char]:
                stack.pop()
            else:
                return False

    return not stack
