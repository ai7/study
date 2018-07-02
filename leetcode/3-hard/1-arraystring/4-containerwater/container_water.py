# https://leetcode.com/explore/interview/card/top-interview-questions-hard/116/array-and-strings/830/
# https://leetcode.com/problems/container-with-most-water/description/

# Container With Most Water
#
# Given n non-negative integers a1, a2, ..., an, where each represents
# a point at coordinate (i, ai). n vertical lines are drawn such that
# the two endpoints of line i is at (i, ai) and (i, 0). Find two
# lines, which together with x-axis forms a container, such that the
# container contains the most water.
#
# Note: You may not slant the container and n is at least 2.

import unittest


class Solution:

    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        return self.my_area2(height)

    # Note: start from both end and advance shorter lines
    #
    # The key is advance the shorter line, since we won't gain
    # anything by moving the longer line (since the area is still
    # limited by the shorter line).

    # 49 / 49 test cases passed.
    # Status: Accepted
    # Runtime: 72 ms
    def my_area2(self, A):
        res = 0
        i, j = 0, len(A) - 1  # start from both ends
        while i < j:
            res = max(res, (j - i) * min(A[i], A[j]))  # update max
            if A[i] < A[j]:  # move the shorter lines toward other line
                i += 1
            else:
                j -= 1
        return res

    # brute force
    def my_area(self, A):

        res = 0
        n = len(A)
        for i in range(n):
            for j in range(i+1, n):
                area = (j - i) * min(A[i], A[j])
                res = max(res, area)

        return res


class TestArea(unittest.TestCase):

    def setUp(self):
        self.sol = Solution()

    def test1(self):
        self.assertEqual(self.sol.maxArea([1, 1]), 1)
        self.assertEqual(self.sol.maxArea([1, 5, 4, 3]), 6)
        self.assertEqual(self.sol.maxArea([3, 1, 2, 4, 5]), 12)


if __name__ == '__main__':
    unittest.main()
