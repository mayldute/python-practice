"""
Task: Remove duplicates while preserving order.

Requirements:
- Keep the first occurrence of each item.
- Preserve original order.
- Do not use set() directly.
- Aim for O(n) complexity.
"""

def remove_duplicates(items: list[int]) -> list[int]:
    """
    Remove duplicates from a list of integers while preserving the original order.
    """
    seen = set()
    unique_items = []
    
    for item in items:
        if item not in seen:
            seen.add(item)
            unique_items.append(item)
    
    return unique_items