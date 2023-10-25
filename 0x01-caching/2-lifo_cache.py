#!/usr/bin/env python3
"""LIFO Caching"""
from base_caching import BaseCaching
from collections import OrderedDict


class LIFOCache(BaseCaching):
    """Class inherits from BaseCaching"""

    def __init__(self):
        """Initializes the class"""
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """Function inserts data into cache"""
        if key or item is None:
            pass
        if key not in self.cache_data:
            if len(self.cache_data) + 1 > BaseCaching.MAX_ITEMS:
                last_key, _ = self.cache_data.popitem(True)
                print("DISCARD:", last_key)
        self.cache_data[key] = item
        self.cache_data.move_to_end(key, last=True)

    def get(self, key):
        """Function retrieves an item by key"""
        return self.cache_data.get(key, None)
