from collections import OrderedDict
import time

class GeoDistributedLRUCache(object):
    """Using Dictionary to hold Cache"""
    def __init__(self, cacheSize=1024):
        self.cacheSize = cacheSize
        self.__values = {}
        self.__access_times = OrderedDict()
        self.access_iter = 0

    def size(self):
        return len(self.__values)

    def clear(self):
        """ Clears the dict"""
        self.__values.clear()
        self.__access_times.clear()

    def __contains__(self, key):
        return self.has_key(key)
        
    def has_key(self, key):
        return key in self.__values

    def __setitem__(self, key, value):
        self.__values[key] = value
        self.__access_times[key] = self.access_iter
        self.access_iter += 1
        self.cleanup()

    def __getitem__(self, key):
        self.__access_times[key] = self.access_iter
        self.access_iter += 1
        return self.__values[key]

    def __delete__(self, key):
        if key in self.__values:
            del self.__values[key]
            del self.__access_times[key]

    def cleanup(self):
        """ Deleting the oldest cache stored"""
        t = int(time.time())
        while (len(self.__values) > self.cacheSize):
            for oldestcache in self.__access_times:
                self.__delete__(oldestcache)
                break

