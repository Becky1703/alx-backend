#!/usr/bin/env python3
"""FIFO Caching"""
from collections import OrderedDict

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """Class inherits from BaseCaching"""
    def __init__(self):
        """Function to initialize the parent class"""
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """Fnction to insert data into the cache"""
        if key or item is None:
            pass
        self.cache_data[key] = item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            first_key, _ = self.cache_data.popitem(False)
            print("DISCARD:", first_key)

    def get(self, key):
        """Function to retrieve data in the cache"""
        return self.cache_data.get(key, None)
