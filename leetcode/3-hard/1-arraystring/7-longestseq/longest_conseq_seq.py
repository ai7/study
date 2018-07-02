# https://leetcode.com/explore/interview/card/top-interview-questions-hard/116/array-and-strings/833/
# https://leetcode.com/problems/longest-consecutive-sequence/description/

# Longest Consecutive Sequence
#
# Given an unsorted array of integers, find the length of the longest
# consecutive elements sequence.
#
# Your algorithm should run in O(n) complexity.

import unittest


class Solution:

    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return self.my_longest2(nums)

    # Note: put in set and try expand each element
    #
    # Put data in a set. Then, pop a random element from set, and try
    # to grow it (by trying to see if consecutive higher and lower
    # number exist). If so, remove those elements.
    #
    # Return the longest such sequence.
    #
    # Alternatively (from solution), for each element, if x-1 does not
    # exist (so this is the beginning), test next element until no
    # match. Code is slightly simpler, but slightly slower than my
    # solution.

    def my_longest2(self, A):
        s = set(A)
        longest = 0
        for x in s:
            if x-1 not in s:  # if this is start of new seq
                y = x + 1  # next pos
                while y in s:
                    y += 1
                longest = max(longest, y - x)
        return longest

    # 68 / 68 test cases passed.
    # Status: Accepted
    # Runtime: 40 ms (beats 99.73% py3)
    def my_longest(self, A):

        def grow(v):  # try to grow v in both directions
            res = 1  # length start with 1
            for i in range(1, len(s)+1):
                t = v + i  # next consecutive integer
                if t in s:
                    res += 1
                    s.remove(t)  # remove it from set
                else:
                    break
            for i in range(1, len(s)+1):
                t = v - i  # prev consecutive integer
                if t in s:
                    res += 1
                    s.remove(t)
                else:
                    break
            return res

        s = set(A)
        longest = 0

        while len(s) > longest:

            v = s.pop()  # pop random element
            longest = max(longest, grow(v))

        return longest


class TestLongest(unittest.TestCase):

    def setUp(self):
        self.sol = Solution()

    def test1(self):
        self.assertEqual(self.sol.longestConsecutive([100, 4, 200, 1, 3, 2]), 4)
        self.assertEqual(self.sol.longestConsecutive([1, 9, 3, 10, 4, 20, 2]), 4)
        self.assertEqual(self.sol.longestConsecutive([36, 41, 56, 35, 44, 33, 34, 92, 43, 32, 42]), 5)
        self.assertEqual(self.sol.longestConsecutive([]), 0)
        self.assertEqual(self.sol.longestConsecutive([1]), 1)
        self.assertEqual(self.sol.longestConsecutive([1,2]), 2)
        self.assertEqual(self.sol.longestConsecutive([1,3]), 1)


if __name__ == '__main__':
    unittest.main()
