"""
Task:
Compress a string by replacing consecutive repeated characters
with the character followed by the number of repetitions.

Requirements:
- Accept a string.
- Consecutive identical characters should be grouped together.
- Each group should be represented by the character and its count.
- Characters that appear again later but are not consecutive start
  a new group.
- Return the compressed string.
- An empty string returns an empty string.
- A character appearing once should still include the count `1`.

Examples:
    "aaabbc" → "a3b2c1"
    "abcd" → "a1b1c1d1"
    "aabbbaa" → "a2b3a2"
    "11122" → "1322"
    "" → ""
"""


def compress_string(text: str) -> str:
    if not text:
        return ""

    current_char = text[0]
    current_count = 0
    result = ""

    for idx, char in enumerate(text):
        if current_char == char:
            current_count += 1
        else:
            result += f"{current_char}{current_count}"
            current_char = char
            current_count = 1

        if idx == len(text) - 1:
            result += f"{current_char}{current_count}"

    return result
