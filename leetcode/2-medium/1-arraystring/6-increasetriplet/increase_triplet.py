# https://leetcode.com/explore/interview/card/top-interview-questions-medium/103/array-and-strings/781/
# https://leetcode.com/problems/increasing-triplet-subsequence/description/

# Increasing Triplet Subsequence
#
# Given an unsorted array return whether an increasing subsequence of
# length 3 exists or not in the array.

import unittest


class Solution:

    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if not nums or len(nums) < 3:
            return False

        return self.triplet2(nums)

    # I am dumbfounded after seeing this in the discussions.
    # so obvious yet I can't seem to come up with this.
    #
    # 61 / 61 test cases passed.
    # Status: Accepted
    # Runtime: 36 ms (beats 100% of py3, damn)
    def triplet2(self, A):
        x1 = x2 = float('inf')  # int_max
        for v in A:
            if v <= x1:
                x1 = v
            elif v <= x2:
                x2 = v
            else:
                return True
        return False


class SolutionMe:

    # after watching online videos, damn it
    # 60 / 61 test cases passed.
    # still time limit exceeded, damn it!
    def triplet1(self, A):

        # The dynamic programming aspect is a bit tricky to see for
        # me. Basically, we calculate the substr ending at position i
        # (for i in [1...n]), which can be quickly calculated based on
        # data from previous rounds.

        n = len(A)
        data = [1] * n  # allocate data array, fill with 1 initially

        for i in range(1, n):  # i from [1...n-1]
            for j in range(0, i):  # j from [0, i-1]
                if A[j] < A[i]:  # if j is less than i
                    # item j is less than item i, so whatever the
                    # maximum subseq length ending at j, the one
                    # ending at i is one more than that.
                    data[i] = max(data[i], data[j]+1)  # update data for i position
                    if data[i] >= 3:  # short-circuit since we only need to check for 3
                        return True

        return False


class TestTriplet(unittest.TestCase):

    def setUp(self):
        self.sol = Solution()

    def test1(self):
        self.assertTrue(self.sol.increasingTriplet([5,1,5,5,2,5,4]))


if __name__ == '__main__':
    unittest.main()
