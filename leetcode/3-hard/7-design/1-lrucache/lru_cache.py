# https://leetcode.com/explore/interview/card/top-interview-questions-hard/122/design/867/
# https://leetcode.com/problems/lru-cache/

# Design and implement a data structure for Least Recently Used (LRU)
# cache. It should support the following operations: get and put.
#
# get(key) - Get the value (will always be positive) of the key if the
#            key exists in the cache, otherwise return -1.
#
# put(key, value) - Set or insert the value if the key is not already
#                   present. When the cache reached its capacity, it
#                   should invalidate the least recently used item
#                   before inserting a new item.

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

import unittest


class Node:

    def __init__(self, k, v):
        self.key = k  # cache key (from list to dict)
        self.val = v  # cache value
        self.next = None
        self.prev = None


# Note: store Node with k/v as hashtable value.
#
# Use hashtable for key lookup, use double-link-list to track recent
# items. Store link list node as hashtable value.
#
# we need the key in LinkList node since on eviction we need to remove
# entry from dictionary using said key.
#
# Can be simpler if we use dummy head/tail nodes.

# simpler version using dummy head/tail elements
# 18 / 18 test cases passed.
# Status: Accepted
# Runtime: 156 ms (beats 72.87% py3)
class LRUCache2:

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.cache = {}
        self.head = Node(0, 0)  # dummy head
        self.tail = Node(0, 0)  # dummy tail
        self.head.next = self.tail  # set head/tail as ending nodes
        self.tail.prev = self.head

    def __len__(self):
        return len(self.cache)

    def _add(self, x):  # insert node after dummy head element
        first = self.head.next  # save current first real node
        first.prev = x
        self.head.next = x  # set new head
        x.next = first
        x.prev = self.head

    def _remove(self, x):  # remove (real) node from list
        x.prev.next = x.next  # always have prev/next since we use dummy
        x.next.prev = x.prev
        return x

    def _remove_tail(self):  # remove last node
        if len(self):
            return self._remove(self.tail.prev)

    def _move_to_front(self, x):
        if x != self.head.next:
            self._remove(x)
            self._add(x)

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.cache:
            return -1

        node = self.cache[key]
        self._move_to_front(node)  # move node to front of list

        return node.val

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if key in self.cache:  # if key is in cache
            node = self.cache[key]
            node.val = value  # update value
            self._move_to_front(node)  # move to front
        else:  # not in cache
            if len(self) == self.capacity:  # if capacity reached
                node = self._remove_tail()  # remove tail node
                del self.cache[node.key]  # remove data from dict
            node = Node(key, value)
            self.cache[key] = node
            self._add(node)


# 18 / 18 test cases passed.
# Status: Accepted
# Runtime: 156 ms (beats 72.87% py3)
class LRUCache:

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.cache = {}
        self.head = None
        self.tail = None
        self.size = 0

    def __len__(self):
        assert len(self.cache) == self.size
        return self.size

    def _add(self, x):  # add node to front of our list

        x.next = self.head
        if x.next:
            x.next.prev = x
        x.prev = None
        self.head = x  # reset head

        if not self.tail:  # if no tail, set to x, otherwise no change
            self.tail = x

        self.size += 1

    def _remove(self, x):  # remove node from list
        if x.prev:
            x.prev.next = x.next
        if x.next:
            x.next.prev = x.prev
        if x == self.head:
            self.head = self.head.next
        if x == self.tail:
            self.tail = self.tail.prev
        self.size -= 1
        return x

    def _remove_tail(self):
        return self._remove(self.tail)

    def _move_to_front(self, x):
        if x != self.head:
            self._remove(x)
            self._add(x)

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.cache:
            return -1

        node = self.cache[key]
        self._move_to_front(node)  # move node to front of list

        return node.val

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if key in self.cache:  # if key is in cache
            node = self.cache[key]
            node.val = value  # update value
            self._move_to_front(node)  # move to front
        else:  # not in cache
            if len(self) == self.capacity:  # if capacity reached
                node = self._remove_tail()  # remove tail node
                del self.cache[node.key]  # remove data from dict
            node = Node(key, value)
            self.cache[key] = node
            self._add(node)


class TestCache(unittest.TestCase):

    def test1(self):
        cache = LRUCache(2)
        cache.put(1, 1)
        self.assertEqual(len(cache), 1)
        cache.put(2, 2)
        self.assertEqual(len(cache), 2)
        self.assertEqual(cache.get(1), 1)  # return 1
        cache.put(3, 3)  # evicts 2
        self.assertEqual(cache.get(2), -1)
        cache.put(4, 4)  # evicts 1
        self.assertEqual(cache.get(1), -1)
        self.assertEqual(cache.get(3), 3)
        self.assertEqual(cache.get(4), 4)

    def test2(self):
        cache = LRUCache2(2)
        cache.put(1, 1)
        self.assertEqual(len(cache), 1)
        cache.put(2, 2)
        self.assertEqual(len(cache), 2)
        self.assertEqual(cache.get(1), 1)  # return 1
        cache.put(3, 3)  # evicts 2
        self.assertEqual(cache.get(2), -1)
        cache.put(4, 4)  # evicts 1
        self.assertEqual(cache.get(1), -1)
        self.assertEqual(cache.get(3), 3)
        self.assertEqual(cache.get(4), 4)


if __name__ == '__main__':
    unittest.main()
