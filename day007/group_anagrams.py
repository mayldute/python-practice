"""
Task:
Implement a function that groups anagrams together.

Requirements:
- Create a `group_anagrams` function that accepts a list of strings.
- Return a list of groups, where each group contains words that are anagrams.
- Words are anagrams if they contain the same letters with the same frequencies.
- Words that have no anagrams should still appear as a group containing one word.
- Preserve duplicate words.
- Return an empty list for empty input.
- The order of groups and words within groups does not matter.
- Do not use a library or built-in function that directly solves the anagram problem.
"""


def count_letters(word: str) -> dict[str, int]:
    counts = {}

    for char in word:
        counts[char] = counts.get(char, 0) + 1

    return counts


def group_anagrams(words: list[str]) -> list[list[str]]:
    anagram_groups = {}

    for word in words:
        letter_count = count_letters(word)
        key = tuple(sorted(letter_count.items()))

        if key not in anagram_groups:
            anagram_groups[key] = []

        anagram_groups[key].append(word)

    return list(anagram_groups.values())
