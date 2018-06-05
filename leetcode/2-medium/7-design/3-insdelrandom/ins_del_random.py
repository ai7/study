# https://leetcode.com/explore/interview/card/top-interview-questions-medium/112/design/813/
# https://leetcode.com/problems/insert-delete-getrandom-o1/description/

# Insert Delete GetRandom O(1)
#
# Design a data structure that supports all following operations in average O(1) time.
#
# - insert(val): Inserts an item val to the set if not already present.
# - remove(val): Removes an item val from the set if present.
# - getRandom: Returns a random element from current set of elements.
#   Each element must have the same probability of being returned.

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()

import random
import unittest


# 18 / 18 test cases passed.
# Status: Accepted
# Runtime: 104 ms (beats 90.34% of py3)
class RandomizedSet:

    # Note: hashtable of value to array index, ise array for get random
    #
    # Use a hashtable to store element and its index in array. Use the
    # array for size and get random() operation.
    #
    # on delete, do not shrink array size, simply copy last element
    # back to deleted index.

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.table = {}  # maps value to array index
        self.array = []  # list of values (for get random)
        self.a_size = 0  # array size

    def _array_add(self, val):
        n = len(self.array)  # get actual array size
        if self.a_size == n:  # if maxed out
            self.array.append(val)
            self.a_size = len(self.array)
        else:
            self.array[self.a_size] = val
            self.a_size += 1
        return self.a_size - 1

    def _array_del(self, idx):
        """Remove specific index from table"""
        last = self.a_size - 1  # last slow with data
        if idx != last:  # if not same, copy last to idx location
            self.array[idx] = self.array[last]  # copy element to new location
            self.table[self.array[idx]] = idx  # update element location in hash
        self.a_size -= 1

    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not
        already contain the specified element.

        :type val: int
        :rtype: bool
        """
        if val in self.table:
            return False
        self.table[val] = self._array_add(val)
        return True

    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained
        the specified element.

        :type val: int
        :rtype: bool
        """
        if val not in self.table:
            return False

        idx = self.table[val]
        self._array_del(idx)  # remove from array first
        del self.table[val]  # remove from hashtable

        return True

    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        if not self.table:
            return

        x = random.randint(0, self.a_size - 1)
        return self.array[x]


class TestRandomSet(unittest.TestCase):

    def setUp(self):
        pass

    def test1(self):
        obj = RandomizedSet()
        self.assertTrue(obj.insert(1))
        self.assertFalse(obj.remove(2))
        self.assertTrue(obj.insert(2))
        self.assertIn(obj.getRandom(), [1, 2])
        self.assertTrue(obj.remove(1))
        self.assertFalse(obj.insert(2))
        self.assertEqual(obj.getRandom(), 2)

    def test2(self):
        obj = RandomizedSet()
        self.assertTrue(obj.insert(0))
        self.assertTrue(obj.insert(1))
        self.assertTrue(obj.remove(0))
        self.assertTrue(obj.insert(2))
        self.assertTrue(obj.remove(1))
        self.assertIn(obj.getRandom(), [2])


if __name__ == '__main__':
    unittest.main()
