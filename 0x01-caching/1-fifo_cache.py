#!/usr/bin/env python3
"""ALX SE caching module"""
BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """A caching system"""
    def __init__(self):
        """Initialize the class"""
        self.keys = []
        super().__init__()

    def put(self, key, item):
        """Add an item in a cache"""
        if key is None or item is None:
            return
        self.cache_data[key] = item
        self.keys.append(key)
        if len(self.keys) != len(self.cache_data):
            self.keys.pop()

        if len(self.cache_data) > super().MAX_ITEMS:
            print(f"DISCARD: {self.keys[0]}")
            del self.cache_data[self.keys[0]]
            self.keys.pop(0)

    def get(self, key):
        """Get an item by key"""
        if key is None or self.cache_data.get(key) is None:
            return None
        return self.cache_data[key]
