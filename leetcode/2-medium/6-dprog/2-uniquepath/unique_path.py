# https://leetcode.com/explore/interview/card/top-interview-questions-medium/111/dynamic-programming/808/
# https://leetcode.com/problems/unique-paths/description/

# Unique Paths
#
# A robot is located at the top-left corner of a m x n grid (marked
# 'Start' in the diagram below).
#
# The robot can only move either down or right at any point in time.
# The robot is trying to reach the bottom-right corner of the grid
# (marked 'Finish' in the diagram below).
#
# How many possible unique paths are there?

import functools
import unittest


class Solution:
    
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        return self.my_path(m, n)

    # for bottom up dp, we can build a mxn matrix (only need half),
    # or, we can recognize that f(a, b) = f(a-1, b) + f(a, b-1),
    # and build up the answer that way...

    # need to read and understand this
    # https://leetcode.com/problems/unique-paths/discuss/22954/0ms-5-lines-DP-Solution-in-C++-with-Explanations

    def my_path2(self, right, down):

        # size right x down matrix
        pass


    # Note: standard memorization

    # 62 / 62 test cases passed.
    # Status: Accepted (on 1st submit!)
    # Runtime: 40 ms (beats 82.84% py3)
    def my_path(self, right, down):
        """number of right/down positions"""

        # haha this is basically f(a, b) = f(a-1, b) + f(a, b-1)
        @functools.lru_cache()
        def search(right, down):

            if right <= 1 or down <= 1:  # if only one row/column left, done
                return 1

            return search(right - 1, down) + search(right, down - 1)  # 2 options

        return search(right, down)


class TestPath(unittest.TestCase):

    def setUp(self):
        self.sol = Solution()

    def test1(self):
        print(self.sol.uniquePaths(1, 3))
        print(self.sol.uniquePaths(2, 3))
        print(self.sol.uniquePaths(3, 3))
        print(self.sol.uniquePaths(4, 3))
        print(self.sol.uniquePaths(4, 4))


if __name__ == '__main__':
    unittest.main()
