from collections import OrderedDict

class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = OrderedDict()

    def get(self, key):
        if key in self.cache:
            self.cache.move_to_end(key)
            return self.cache[key]
        return -1

    def put(self, key, value):
        if key in self.cache:
            self.cache.move_to_end(key)
        self.cache[key] = value
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)

def test_lru_cache_basic():
    c = LRUCache(2)
    c.put(1, 1)
    c.put(2, 2)
    return [c.get(1), c.get(3)]

def test_lru_cache_eviction():
    c = LRUCache(2)
    c.put(1, 1)
    c.put(2, 2)
    c.put(3, 3)
    r1 = c.get(1)
    r2 = c.get(3)
    c.put(4, 4)
    r3 = c.get(4)
    return [r1, r2, r3]

def test_lru_cache_update():
    c = LRUCache(2)
    c.put(1, 1)
    c.put(2, 2)
    c.get(1)
    c.put(3, 3)
    return [c.get(1), c.get(2), c.get(3)]

print(test_lru_cache_basic())
print(test_lru_cache_eviction())
print(test_lru_cache_update())
