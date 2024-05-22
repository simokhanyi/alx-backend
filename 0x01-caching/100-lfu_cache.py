#!/usr/bin/python3
"""
a class LFUCache that inherits from BaseCaching and is a caching system
"""

from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """
    LFUCache is a caching system that inherits from BaseCaching.
    It implements an LFU (Least Frequently Used) caching mechanism.
    """

    def __init__(self):
        """Initialize the cache and maintain the usage frequency and order."""
        super().__init__()
        self.usage_frequency = {}
        self.usage_order = []

    def put(self, key, item):
        """
        Add an item in the cache.

        Args:
            key (str): The key for the cache item.
            item (any): The item to be cached.
        """
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.cache_data[key] = item
            self.usage_frequency[key] += 1
            self.usage_order.remove(key)
            self.usage_order.append(key)
        else:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                # Find the least frequently used item
                min_freq = min(self.usage_frequency.values())
                lfu_keys = [
                    k for k, v in self.usage_frequency.items() if v == min_freq
                ]
                if len(lfu_keys) > 1:
                    lru_lfu_key = None
                    for k in self.usage_order:
                        if k in lfu_keys:
                            lru_lfu_key = k
                            break
                    self.usage_order.remove(lru_lfu_key)
                    del self.cache_data[lru_lfu_key]
                    del self.usage_frequency[lru_lfu_key]
                    print(f"DISCARD: {lru_lfu_key}")
                else:
                    lfu_key = lfu_keys[0]
                    self.usage_order.remove(lfu_key)
                    del self.cache_data[lfu_key]
                    del self.usage_frequency[lfu_key]
                    print(f"DISCARD: {lfu_key}")

            self.cache_data[key] = item
            self.usage_frequency[key] = 1
            self.usage_order.append(key)

    def get(self, key):
        """
        Get an item by key.

        Args:
            key (str): The key to retrieve from the cache.

        Returns:
            any: The value in self.cache_data linked to key,
                 or None if the key is None or doesn't exist.
        """
        if key is None or key not in self.cache_data:
            return None

        self.usage_frequency[key] += 1
        self.usage_order.remove(key)
        self.usage_order.append(key)
        return self.cache_data[key]
