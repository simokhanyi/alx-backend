#!/usr/bin/python3
"""
a class BasicCache that inherits from BaseCaching and is a caching system
"""

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    BasicCache is a caching system that inherits from BaseCaching.
    This caching system has no limit and uses a dictionary for storage.
    """

    def put(self, key, item):
        """
        Add an item in the cache.

        Args:
            key (str): The key for the cache item.
            item (any): The item to be cached.
        """
        if key is not None and item is not None:
            self.cache_data[key] = item

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
