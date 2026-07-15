"""
Task: Count word frequency in a text.

Requirements:
- Ignore letter case.
- Ignore punctuation.
- Return a dictionary with words and counts.
- Use dictionary operations.
"""

import string
from collections import Counter


def normalize(text: str) -> list[str]:
    """
    Normalize the input text by removing punctuation (except apostrophes), converting to lowercase, and splitting into words.
    """
    return (
        text.translate(str.maketrans("", "", string.punctuation.replace("'", "")))
        .lower()
        .split()
    )

def count_words(text: str) -> dict[str, int]:
    """
    Count the number of occurrences of each word in a given text.
    """
    word_counts = {}
    
    for word in normalize(text):
        word_counts[word] = word_counts.get(word, 0) + 1
    return word_counts

def count_words_alternative(text: str) -> dict[str, int]:
    """
    Count the number of occurrences of each word in a given text using Counter.
    """
    return dict(Counter(normalize(text)))
