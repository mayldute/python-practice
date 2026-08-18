"""
Task:
Sort words by how frequently they appear.

Requirements:
- Return a new list of words sorted by frequency in descending order.
- Words with the same frequency should keep their original order of first appearance.
- Treat uppercase and lowercase letters as the same.
- Do not modify the original list.
- Use a dictionary to count frequencies.
- Do not use collections.Counter.
"""


def sort_by_frequency(words: list[str]) -> list[str]:
    counts_words = {}

    for word in words:
        word = word.lower()
        counts_words[word] = counts_words.get(word, 0) + 1

    return [
        word
        for word, _ in sorted(
            counts_words.items(),
            key=lambda item: item[1],
            reverse=True
        )
    ]
