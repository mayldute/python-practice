"""
Task:
Implement a simple Least Recently Used (LRU) cache.

Requirements:
- Create an LRUCache class.
- The cache has a fixed maximum capacity.
- `get(key)` returns the stored value or None if the key doesn't exist.
- `put(key, value)` adds or updates a value.
- Accessing a key with `get()` makes it recently used.
- Updating a key with `put()` also makes it recently used.
- When the cache exceeds its capacity, remove the least recently used item.
- `get()` and `put()` should both aim for O(n) time complexity.
"""


class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value


class LRUCache:
    def __init__(self, max_capacity):
        if max_capacity <= 0:
            raise ValueError("Maximum capacity can not be equal or less 0.")
        
        self.max_capacity = max_capacity
        self.cache: dict[str, Node] = {}
        self.recently_used = []

    def put(self, key: str, value: int) -> None:
        if key in self.cache:
            self.cache[key].value = value
            self.recently_used.remove(key)
            self.recently_used.append(key)
            return 

        node = Node(key, value)

        if len(self.cache) >= self.max_capacity:
            least_recently_used = self.recently_used.pop(0)
            del self.cache[least_recently_used]
        
        self.cache[key] = node
        self.recently_used.append(key)

    def get(self, key):
        if key in self.cache:
            self.recently_used.remove(key)
            self.recently_used.append(key)
            return self.cache[key].value
            
        return None
