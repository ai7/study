# https://leetcode.com/explore/interview/card/top-interview-questions-medium/114/others/824/
# https://leetcode.com/problems/majority-element/description/

# Majority Element
#
# Given an array of size n, find the majority element. The majority
# element is the element that appears more than n/2 times.

import collections
import unittest


class Solution:

    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return self.my_major2(nums)

    # Note: track/replace possible candidate on O(n) 1-pass.
    #
    # This is a neat solution based on Boyer-Moore Voting Algorithm.
    #
    # Start with the first element as possible candidate. For each
    # next element, if same, increment counter. if different,
    # decrement counter.
    #
    # Whenever counter reaches 0, replace candidate with current
    # element. Output current candidate at the very end.
    #
    # The intuition is that, when we replace the current candidate,
    # there are at least equal amount of different elements, so, it's
    # a safe replace. If it is indeed the majority element, because we
    # have seen an equal amount of other elements, it must exist as a
    # majority in what's remaining of the array, so we will still
    # choose it later on.
    #
    # Could we have missed a possible major element y when we have x
    # as candidate, before x dropped to 0? We might have, but y must
    # not have held a majority up to this point, since otherwise out
    # candidate would've been it. Therefore, if y is indeed the
    # majority element, for sure it would've been a majority element
    # in the rest of the array, so we will pick it later on.
    #
    # Basically when we replace candidates, it is a safe replace, and
    # will not change the majority element. It's a neat algorithm.

    # get majority via candidate counting
    # 44 / 44 test cases passed.
    # Status: Accepted
    # Runtime: 52 ms (beats 91.20% py3)
    def my_major2(self, A):
        if not A:
            return
        c = A[0]  # pick first element as candidate
        counter = 1  # set counter to 1
        for x in A[1:]:
            if c == x:  # if same, increment counter
                counter += 1
            else:  # if different, decrement counter
                counter -= 1
            if counter == 0:  # if counter drops to 0, replace candidate
                c = x
                counter = 1
        return c

    # get majority via counter. simple approach.
    #
    # 44 / 44 test cases passed.
    # Status: Accepted
    # Runtime: 56 ms
    def my_major(self, nums):

        if not nums:
            return

        count = collections.Counter(nums)
        n = len(nums)

        for x in nums:
            if count[x] >= n/2:
                return x


class TestMajor(unittest.TestCase):

    def setUp(self):
        self.sol = Solution()

    def test1(self):
        self.assertEqual(self.sol.majorityElement([3,2,3]), 3)
        self.assertEqual(self.sol.majorityElement([2,2,1,1,1,2,2]), 2)


if __name__ == '__main__':
    unittest.main()
