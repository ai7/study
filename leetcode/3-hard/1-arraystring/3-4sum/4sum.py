# https://leetcode.com/explore/interview/card/top-interview-questions-hard/116/array-and-strings/829/
# https://leetcode.com/problems/4sum-ii/description/

# 4Sum II
#
# Given four lists A, B, C, D of integer values, compute how many
# tuples (i, j, k, l) there are such that A[i] + B[j] + C[k] + D[l] is
# zero.

import collections
import unittest


class Solution:

    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        return self.my_4sum(A, B, C, D)

    # Note: build 2 pair-sum dict, iter and check opposite value
    #
    # Brute force is O(n^4). But, the last iteration is not needed, as
    # we can simply check if the last value we need exist in O(1) time
    # (via a set), so we can reduce it to O(n^3).
    #
    # We can further reduce this to O(n^2) by build a hash of all
    # pair-sum value, and a count of how many pairs made that value.
    # We do this for (A, B), and (C, D), so we have 2 of these
    # pair-sum maps.
    #
    # Then, we simply iterate through first dict, and check if the
    # opposite value we need is in the 2nd dict.
    #
    # The reason we don't need to build a 3rd (B, C) pair, is because
    # for any possible solution index, the corresponding sum value
    # must've been included in our first set.
    #
    # A nice trick to build the first pair is
    #   pair1 = collections.Counter(a+b for a in A for b in B)
    #
    # collections.Counter when accessing an unknown element returns 0!

    # shorter solution from discussion. ;)
    def my_4sum2(self, A, B, C, D):
        pair1 = collections.Counter(a+b for a in A for b in B)
        return sum(pair1[-c-d] for c in C for d in D)

    # 48 / 48 test cases passed.
    # Status: Accepted
    # Runtime: 508 ms (beats 50% py3)
    def my_4sum(self, A, B, C, D):

        pair1 = collections.defaultdict(int)  # count of sums for all (A, B) pair
        pair2 = collections.defaultdict(int)  # count of sums for (C, D)
        res = 0

        for a in A:
            for b in B:
                pair1[a+b] += 1  # increment counter for this sum value

        for c in C:
            for d in D:
                pair2[c+d] += 1

        for k, v in pair1.items():
            s2 = -k  # the opposite value to make sum == 0
            if s2 in pair2:
                res += v * pair2[s2]

        return res


class Test4Sum(unittest.TestCase):

    def setUp(self):
        self.sol = Solution()

    def test1(self):
        self.assertEqual(self.sol.fourSumCount([1, 2],
                                               [-2, -1],
                                               [-1, 2],
                                               [0, 2]),
                         2)
        self.assertEqual(self.sol.fourSumCount([-1, -1],
                                               [-1, 1],
                                               [-1, 1],
                                               [1, -1]),
                         6)


if __name__ == '__main__':
    unittest.main()
