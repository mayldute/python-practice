"""
Solve the Daily Temperatures problem using a monotonic stack.

For each temperature, return the number of days that must pass before
a strictly warmer temperature appears. If no warmer temperature exists
in the future, return 0 for that day.

Requirements:
- Return a new list.
- Preserve the original input list.
- Keep each result aligned with its corresponding input index.
- Return an empty list for an empty input.
- Handle repeated temperatures correctly.
- Use a stack to track temperatures that are waiting for a warmer day.
- Avoid comparing every temperature with all following temperatures.
- Aim for O(n) time complexity.
- Use O(n) additional space complexity.

Examples:
- [73, 74, 75, 71, 69, 72, 76, 73]
  -> [1, 1, 4, 2, 1, 1, 0, 0]
- [30, 40, 50, 60]
  -> [1, 1, 1, 0]
- [60, 50, 40, 30]
  -> [0, 0, 0, 0]
- []
  -> []
"""


def daily_temperatures(temperatures: list[int]) -> list[int]:
    res = [0] * len(temperatures)
    stack = []

    for idx, temp in enumerate(temperatures):
        while stack and temp > stack[-1][0]:
            stack_temp, stack_idx = stack.pop()  # noqa: RUF059
            res[stack_idx] = idx - stack_idx

        stack.append([temp, idx])

    return res
