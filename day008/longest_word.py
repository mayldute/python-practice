"""
Task:
Implement a function that finds the longest word in a list.

Requirements:
- Create a `longest_word` function.
- The function accepts a list of strings.
- Return the longest word in the list.
- If multiple words have the same maximum length, return the first one.
- Return `None` if the list is empty.

Examples:
    ["cat", "elephant", "dog"] → "elephant"
    ["hi", "hello", "hey"] → "hello"
    ["cat", "dog", "bird"] → "bird"
    [] → None
"""


def longest_word(words: list[str]) -> str | None:
    if not words:
        return None

    longest = words[0]

    for word in words[1:]:
        if len(word) > len(longest):
            longest = word

    return longest
