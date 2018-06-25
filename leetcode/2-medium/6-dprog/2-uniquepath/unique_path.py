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
        return self.my_path3(m, n)

    # Note: standard memorization, or dp with mxn | 2xn array
    #
    # We have basically f(a, b) = f(a-1, b) + f(a, b-1).
    #
    # Standard memo solution is easy to write.
    #
    # For DP, we can start with full mxn matrix, initialize first row
    # and first column to 1. Then basically compute matrix and return
    # bottom right corner value.
    #
    # An improvement is we only need the last 2 rows for doing this
    # calculation, so instead of keeping the full matrix, we just keep
    # the last 2 rows.

    # simple dp solution using full m x n matrix (down x right)
    def my_path2(self, right, down):

        # initialize matrix with value 1
        M = [[1 for r in range(right)] for c in range(down)]

        for i in range(1, down):
            for j in range(1, right):
                M[i][j] = M[i-1][j] + M[i][j-1]

        return M[down-1][right-1]

    # optimized with just 2 arrays
    def my_path3(self, right, down):

        prev = [1] * right
        curr = [1] * right

        for i in range(1, down):  # for each row from second+
            prev, curr = curr, prev  # swap so curr is ready for input
            for j in range(1, right):  # for each col from second+
                curr[j] = prev[j] + curr[j-1]

        return curr[right-1]  # return last element of current row

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
        self.assertEqual(self.sol.uniquePaths(1, 3), 1)
        self.assertEqual(self.sol.uniquePaths(2, 3), 3)
        self.assertEqual(self.sol.uniquePaths(3, 3), 6)
        self.assertEqual(self.sol.uniquePaths(4, 3), 10)
        self.assertEqual(self.sol.uniquePaths(4, 4), 20)


if __name__ == '__main__':
    unittest.main()
