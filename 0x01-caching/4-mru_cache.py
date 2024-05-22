#!/usr/bin/python3
"""
a class MRUCache that inherits from BaseCaching and is a caching system
"""

from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """
    MRUCache is a caching system that inherits from BaseCaching.
    It implements an MRU (Most Recently Used) caching mechanism.
    """

    def __init__(self):
        """Initialize the cache and maintain the usage order."""
        super().__init__()
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
            self.usage_order.remove(key)
        elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            mru_key = self.usage_order.pop()
            del self.cache_data[mru_key]
            print(f"DISCARD: {mru_key}")

        self.cache_data[key] = item
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

        self.usage_order.remove(key)
        self.usage_order.append(key)
        return self.cache_data[key]
