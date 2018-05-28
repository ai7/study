# https://leetcode.com/explore/interview/card/top-interview-questions-medium/110/sorting-and-searching/798/
# https://leetcode.com/problems/sort-colors/description/

# Sort Colors
#
# Given an array with n objects colored red, white or blue, sort them
# in-place so that objects of the same color are adjacent, with the
# colors in the order red, white and blue.

import unittest


class Solution:

    # can we sort 3 distinct values in linear time with O(1) space?
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        # self.sort_a(nums)
        # self.sort_b(nums)
        self.sort_dutch(nums)

    # 87 / 87 test cases passed.
    # Status: Accepted
    # Runtime: 36 ms
    #
    # break array into low, mid, high sections. mid is the section we are
    # exploring. low and high are settled regions.
    #
    # repeat until mid crosses high
    #   0: swap a[Lo] and a[Mid]; Lo++; Mid++
    #   1: Mid++
    #   2: swap a[Mid] and a[Hi]; Hi–
    def sort_dutch(self, A):

        def swap(i, j):
            A[i], A[j] = A[j], A[i]

        low = mid = 0
        high = len(A)-1

        while mid <= high:
            if A[mid] == 0:  # item < middle
                swap(low, mid)  # swap with low (low++, mid++)
                low += 1
                mid += 1
            elif A[mid] == 2:  # item > middle
                swap(mid, high)  # swap with high (high--)
                high -= 1
            else:
                mid += 1

    # What an intriguing solution from forum post.
    # https://leetcode.com/problems/sort-colors/discuss/26500/Four-different-solutions
    #
    # We maintain 3 pointers that points to end of each segment, when we see:
    # - 3: only write 3
    # - 2: write both 2 and 3
    # - 1: write 1, 2, and 3
    #
    # in essense, we are pushing the 'sections' forward when we add
    # number to prior sections. It's a noval approach, but not
    # efficient or practical. ;)
    def sort_a(self, A):
        n0 = n1 = n2 = -1  # count of 0, 1 and 2
        for i in range(len(A)):
            if A[i] == 0:
                n2 += 1
                A[n2] = 2

                n1 += 1
                A[n1] = 1

                n0 += 1
                A[n0] = 0
            elif A[i] == 1:
                n2 += 1
                A[n2] = 2

                n1 += 1
                A[n1] = 1
            elif A[i] == 2:
                n2 += 1
                A[n2] = 2


class TestSort(unittest.TestCase):

    def setUp(self):
        self.sol =  Solution()

    def test1(self):
        A = [2,0,2,1,1,0]
        self.sol.sortColors(A)
        self.assertEqual(A, [0,0,1,1,2,2])

    def test2(self):
        A = [1,2,2,2,2,0,0,0,1,1]
        self.sol.sortColors(A)
        self.assertEqual(A,
                         [0, 0, 0, 1, 1, 1, 2, 2, 2, 2])


if __name__ == '__main__':
    unittest.main()
