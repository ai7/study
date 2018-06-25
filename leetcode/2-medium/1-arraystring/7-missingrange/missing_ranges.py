# Missing Ranges
#
# Given a sorted integer array where the range of elements are [0, 99]
# inclusive, return its missing ranges. For example, given [0, 1, 3,
# 50, 75], return ["2", "4->49", "51->74", "76->99"]

import unittest


class Solution:

    def missingRange(self, nums):
        return self.my_range(nums, 0, 99)

    # Note: use dummy value at start/end of array
    #
    # Use a dummy value at start and end of array to reduce the number
    # of cases so we can simplify our loop.
    #
    # first: start value - 1
    # last : end value + 1
    #
    # This way, the rest of the algorithm flows cleanly.

    def my_range(self, A, start, end):

        def add_range(i, j):
            if i >= j:
                res.append(i)
            else:
                res.append([i, j])  # or "i -> j"

        n = len(A)
        res = []

        last = end + 1  # dummy last value
        prev = start - 1  # dummy first value

        for i in range(n + 1):
            v = A[i] if i < n else last
            if v - prev > 1:
                add_range(prev + 1, v - 1)
            prev = v

        return res


class TestRange(unittest.TestCase):

    def setUp(self):
        self.sol = Solution()

    def test1(self):
        print(self.sol.missingRange([0, 1, 3, 50, 75]))
        print(self.sol.missingRange([]))
        print(self.sol.missingRange([1]))


if __name__ == '__main__':
    unittest.main()
