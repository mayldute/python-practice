"""
Task:
Implement a function that finds the first word whose length meets a minimum requirement.

Requirements:
- Create a `find_first_long_word` function.
- The function accepts a list of strings and a minimum length.
- Return the first word whose length is greater than or equal to `min_length`.
- Stop searching as soon as a matching word is found.
- Return `None` if no word meets the minimum length.
- Preserve the original list.

Examples:
    ["cat", "dog", "elephant", "bird"], 5 → "elephant"
    ["hi", "hello", "world"], 5 → "hello"
    ["cat", "dog"], 10 → None
    [], 3 → None
"""


def find_first_long_word(words: list[str], min_length: int) -> str | None:
    for word in words:
        if len(word) >= min_length:
            return word

    return None
