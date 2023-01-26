#!/usr/bin/python3
"""3-lru_cache module"""
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """inherits from BaseCaching and is a caching system"""

    def __init__(self):
        super().__init__()
        self.keyMap = {}
        self.count = 1

    def put(self, key, item):
        """assign to the dictionary
                self.cache_data the item value for the key"""
        if not key or not item:
            return
        if len(self.cache_data) > BaseCaching.MAX_ITEMS - 1\
                and (key not in self.cache_data.keys()):
            print('DISCARD: {}'.format(min(self.keyMap, key=self.keyMap.get)))
            del self.cache_data[min(self.keyMap, key=self.keyMap.get)]
            del self.keyMap[min(self.keyMap, key=self.keyMap.get)]
        self.cache_data[key] = item
        self.keyMap[key] = self.count
        self.count += 1

    def get(self, key):
        """return the value in self.cache_data linked to key"""
        if key is None or key not in self.cache_data.keys():
            return None
        self.keyMap[key] = self.count
        self.count += 1
        return self.cache_data[key]
