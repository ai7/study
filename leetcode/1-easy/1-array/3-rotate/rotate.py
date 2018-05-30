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

    # Note: one pass in place solution using O(1) extra space.
    #
    # start with first element, copy it directly to its destination
    # (save dest element before copy). repeat for the saved dest
    # element. If we ever wrap back to the starting point before
    # finish, we start again at the next position.
    #
    # we do this total for n times. if array size is like a prime
    # number, then one pass would hit all distinct locations.
    # Otherwise it may wrap back to beginning element, so we need to
    # start at next location, until we've done this n times.
    #
    # Logic is a bit tedious to get right. Remember we need:
    # - var to track the starting pos (so we know wrap back) [start]
    # - var to step through elements [i]
    # - var to track previous data [previous]
    # - temp var for copy/save [t2]
    # with these vars we should be able to come up with correct logic
    # in reasonable time.

    # using constant extra storage
    def rotate2(self, A, k, n):

        # loop assume 1 round is sufficient
        start = 0  # start pos, so we know if we wrap back
        i = 0  # index for element to process
        previous = A[start]  # previous saved data before clobber

        for count in range(n):  # do this n times

            i = (i + k) % n  # compute new location
            t2 = A[i]  # save new loc value in temp var (not previous)
            A[i] = previous  # set target to previous value

            if i == start:  # if we've wrapped back, special case
                i += 1  # start at next slot
                start = i
                previous = A[i]  # save new previous_data (from new slot)
            else:
                previous = t2  # simply update previous data

    # obvious solution using buffer of size k
    def rotate(self, A, k, n):

        T = A[n-k:]  # save last k elements to T

        for i in reversed(range(n-k)):  # copy remain elements from end
            A[i+k] = A[i]

        for i in range(k):  # put saved T element in front
            A[i] = T[i]


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
