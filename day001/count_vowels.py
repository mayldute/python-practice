def count_vowels(text: str) -> int:
    """
    Count the number of vowels in a given text.

    Args:
        text (str): The input string to count vowels in.

    Returns:
        int: The number of vowels in the input string.
    """
    vowels = "aeiouAEIOU"
    return sum(1 for char in text if char in vowels)