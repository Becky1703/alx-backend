#!/usr/bin/env python3
"""Basic Caching"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """Class inherits from BaseCaching"""
    def put(self, key, item):
        """Fnction to put data into a caching system"""
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """Fnction to retrieve the data stored in the cached system"""
        return self.cache_data.get(key, None)
