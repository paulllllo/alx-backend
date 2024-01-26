#!/usr/bin/env python3
"""An LFU caching module"""
BaseCaching = __import__('base_caching').BaseCaching


class LFUCache(BaseCaching):
    """An LFU caching system"""
    def __init__(self):
        """Initialize the class"""
        self.keys = []
        self.freq = {}
        super().__init__()

    def put(self, key, item):
        """Add an item in a cache"""
        if key is None or item is None:
            return

        if len(self.cache_data) >= super().MAX_ITEMS and key not in\
                self.cache_data:
            lfu = min(self.freq.values())
            lfu_keys = []
            for k, v in self.freq.items():
                if v == lfu:
                    lfu_keys.append(k)
            if len(lfu_keys) > 1:
                lru = {}
                for k in lfu_keys:
                    lru[k] = self.keys.index(k)
                least_index = min(lru.values())
                key_to_delete = self.keys[least_index]
            else:
                key_to_delete = lfu_keys[0]

            print(f"DISCARD: {key_to_delete}")
            del self.cache_data[key_to_delete]
            self.keys.pop(self.keys.index(key_to_delete))
            del self.freq[key_to_delete]

        if key in self.keys:
            self.keys.pop(self.keys.index(key))

        self.keys.append(key)
        self.cache_data[key] = item

        # update usage frequency
        if key in self.freq:
            self.freq[key] += 1
        else:
            self.freq[key] = 1

    def get(self, key):
        """Get an item by key"""
        if key is None or self.cache_data.get(key) is None:
            return None
        self.keys.pop(self.keys.index(key))
        self.keys.append(key)
        self.freq[key] += 1
        return self.cache_data[key]
