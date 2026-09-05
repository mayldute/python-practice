"""
Task: Longest Substring Without Repeating Characters

Given a string, return the length of the longest substring
that contains no repeated characters.

A substring must contain consecutive characters.

Examples:
    "abcabcbb" -> 3
    "bbbbb"    -> 1
    "pwwkew"   -> 3
    ""         -> 0
    "abcdef"   -> 6

Requirements:
    - Return an integer.
    - Handle an empty string.
    - Handle strings containing spaces and special characters.
    - Do not use a set or dictionary containing every possible substring.

Examples of valid substrings:
    "abc" from "abcabcbb"
    "wke" from "pwwkew"
"""


def longest_substring_without_repeating_v1(s: str) -> int:
    if not s:
        return 0

    count = 1
    max_count = 1
    current_substring = s[0]

    for i in range(1, len(s)):
        if s[i] not in current_substring:
            current_substring += s[i]
            count += 1
            max_count = max(max_count, count)
        else:
            current_substring = (
                current_substring[current_substring.find(s[i]) + 1 :] + s[i]
            )
            count = len(current_substring)
            max_count = max(max_count, count)

    return max_count


def longest_substring_without_repeating_v2(s: str) -> int:
    seen = set()
    left = 0
    max_count = 0

    for right in range(len(s)):
        while s[right] in seen:
            seen.remove(s[left])
            left += 1

        seen.add(s[right])
        max_count = max(max_count, right - left + 1)

    return max_count
