#!/usr/bin/env python3
"""ALX SE caching module"""
BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """An LRU caching system"""
    def __init__(self):
        """Initialize the class"""
        self.keys = []
        super().__init__()

    def put(self, key, item):
        """Add an item in a cache"""
        if key is None or item is None:
            return

        if len(self.cache_data) >= super().MAX_ITEMS and key not in\
                self.cache_data:
            print(f"DISCARD: {self.keys[0]}")
            del self.cache_data[self.keys[0]]
            self.keys.pop(0)
        if key in self.keys:
            self.keys.pop(self.keys.index(key))

        self.keys.append(key)
        self.cache_data[key] = item

    def get(self, key):
        """Get an item by key"""
        if key is None or self.cache_data.get(key) is None:
            return None
        self.keys.pop(self.keys.index(key))
        self.keys.append(key)
        return self.cache_data[key]
