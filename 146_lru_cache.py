# 146. LRU Cache
#
# Design and implement a data structure for Least Recently Used (LRU) cache.
# It should support the following operations: get and put.
#
# get(key) - Get the value (will always be positive) of the key if the key exists in the cache,
# otherwise return -1.
# put(key, value) - Set or insert the value if the key is not already present.
# When the cache reached its capacity, it should invalidate the least recently used item
# before inserting a new item.
#
# Follow up:
# Could you do both operations in O(1) time complexity?
#
# Example:
#
# LRUCache cache = new LRUCache( 2 /* capacity */ );
#
# cache.put(1, 1);
# cache.put(2, 2);
# cache.get(1);       // returns 1
# cache.put(3, 3);    // evicts key 2
# cache.get(2);       // returns -1 (not found)
# cache.put(4, 4);    // evicts key 1
# cache.get(1);       // returns -1 (not found)
# cache.get(3);       // returns 3
# cache.get(4);       // returns 4

import collections


# http://www.cnblogs.com/chruny/p/5477982.html
class LRUCache(object):
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.length = 0
        self.dict = collections.OrderedDict()

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        try:
            value = self.dict[key]
            del self.dict[key]
            self.dict[key] = value
            return value
        except:
            return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        The popitem() method for ordered dictionaries returns and removes a (key, value) pair.
        The pairs are returned in LIFO order if last is true or FIFO order if false.
        """
        try:
            del self.dict[key]
            self.dict[key] = value
        except:
            if self.length == self.capacity:
                self.dict.popitem(last=False)
                self.length -= 1
            self.dict[key] = value
            self.length += 1

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.dict:
            value = self.dict[key]
            del self.dict[key]
            self.dict[key] = value
            return value
        return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if key in self.dict:
            del self.dict[key]
            self.dict[key] = value
        else:
            # when key not in dict, add it until reach capacity
            # then pop first item, and add new value.
            if self.length == self.capacity:
                self.dict.popitem(last=False)
                self.dict[key] = value
            else:
                self.dict[key] = value
                self.length += 1


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

if __name__ == '__main__':
    lru_cache = LRUCache(3)
    lru_cache.put(1, 1)
    lru_cache.put(2, 2)
    lru_cache.put(3, 3)
    assert lru_cache.get(0) == -1
    assert lru_cache.get(1) == 1
    lru_cache.put(1, 10)
    assert lru_cache.get(1) == 10
    lru_cache.put(4, 4)
    assert lru_cache.get(2) == -1
