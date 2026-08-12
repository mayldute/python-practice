"""
Task:
Group words by their length.

Requirements:
- Return a dictionary where each key is a word length.
- The value for each key should be a list of words with that length.
- Preserve the original order of the words.
- Preserve duplicate words.
- Return an empty dictionary if the input list is empty.
- Do not use collections.defaultdict.
- Do not modify the original list.
- Aim for O(n) time complexity.
"""

def group_by_length(words: list[str]) -> dict[int, list[str]]:
    result = {}

    for word in words:
        result.setdefault(len(word), []).append(word)

    return result
