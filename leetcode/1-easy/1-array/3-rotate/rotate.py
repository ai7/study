# https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/646/
# https://leetcode.com/problems/rotate-array/description/

# Rotate Array
#
# Given an array, rotate the array to the right by k steps, where k is
# non-negative.

import unittest


class Solution:

    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n  # if k > length
        if k < 1:  # no rotate or negative
            return

        self.rotate2(nums, k, n)

    # using k size buffer, obvious solution
    def rotate1(self, A, k, n):

        T = A[n-k:]  # save last k elements

        for i in reversed(range(n-k)):
            A[i+k] = A[i]

        for i in range(k):
            A[i] = T[i]

    # using constant extra storage
    def rotate2(self, A, k, n):

        # loop assume 1 round is sufficient
        start = 0  # current round starting location
        i = 0
        previous = A[start]  # previous data

        for count in range(n):

            i = (i + k) % n  # new location
            t2 = A[i]  # save new loc value
            A[i] = previous  # copy src to target

            if i == start:  # if we've wrapped back, special case
                i += 1  # start at next slot
                start = i
                previous = A[i]  # save new previous_data (from new slot)
            else:
                previous = t2  # simply update previous data


class RotateTest(unittest.TestCase):

    def setUp(self):
        self.sol = Solution()

    def test1(self):
        A = [1, 2, 3, 4, 5, 6, 7]
        self.sol.rotate(A, 3)
        self.assertEqual(A, [5, 6, 7, 1, 2, 3, 4])

    def test2(self):
        A = [1, 2, 3, 4, 5, 6]
        self.sol.rotate(A, 2)
        self.assertEqual(A, [5, 6, 1, 2, 3, 4])

    def test3(self):
        A = [1, 2, 3, 4, 5, 6]
        self.sol.rotate(A, 3)
        self.assertEqual(A, [4, 5, 6, 1, 2, 3])


if __name__ == '__main__':
    unittest.main()
