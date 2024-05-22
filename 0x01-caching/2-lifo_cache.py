#!/usr/bin/python3
"""
a class LIFOCache that inherits from BaseCaching and is a caching system
"""

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """
    LIFOCache is a caching system that inherits from BaseCaching.
    It implements a LIFO (Last-In, First-Out) caching mechanism.
    """

    def __init__(self):
        """Initialize the cache and maintain order of insertion."""
        super().__init__()
        self.order = []

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
            self.order.remove(key)
        elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            last_key = self.order.pop()
            del self.cache_data[last_key]
            print(f"DISCARD: {last_key}")

        self.cache_data[key] = item
        self.order.append(key)

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
        return self.cache_data[key]
