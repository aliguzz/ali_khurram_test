import collections
from datetime import datetime
class LRUCache:
    def __init__(self, capacity, expire):
        self.cache = collections.OrderedDict()
        self.capacity = capacity
        self.expire = expire

    def get(self, key):
        global datetime
        if key not in self.cache:
            return -1
        val = self.cache[key]
        current_datetime = datetime.now()
        datetime = val[-1]
        difference = current_datetime - datetime
        if difference.seconds > self.expire:
            del self.cache[key]
            return -1
        del self.cache[key]
        self.cache[key] = val
        return val

    def set(self, key, value):
        global datetime
        value = list(value)
        if key in self.cache:
            prev_datetime = self.cache[key][-1]
            value.pop()
            value.append(prev_datetime)
            del self.cache[key]
        elif len(self.cache) == self.capacity:
            value.append(datetime.now())
            self.cache.popitem(last=False)
        else:
            value.append(datetime.now())
        value = tuple(value)
        self.cache[key] = value
