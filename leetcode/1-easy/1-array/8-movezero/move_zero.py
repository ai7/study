# https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/567/
# https://leetcode.com/problems/move-zeroes/description/

# Move Zeroes
#
# Given an array nums, write a function to move all 0's to the end of
# it while maintaining the relative order of the non-zero elements.

import unittest


class Solution:

    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return
        A = nums

        n = len(A)
        if n < 2:
            return
        self.move3_sol3(A, n)

    # Note: swap any non zero with end of non-zero sequence.
    #
    # for each element, if not zero:
    #   swap with last non-zero-seq
    #   non-zero-seq++
    #
    # it's miraculous that this works! it's also a tiny bit simpler
    # than sol2. it's obvious that the non-zero-seq will all be >0,
    # it's less obvious that any 0 in between would've been
    # pushed/squeezed to the right side.

    # beats 93%, damn (from solution 3, damn)
    def move3_sol3(self, A, n):
        lastNonZero = 0
        for i in range(n):
            if A[i]:  # if not, simply i++
                # having an extra "if i != lastNonZero" for next line
                # does not seem to change speed, still 93%
                A[lastNonZero], A[i] = A[i], A[lastNonZero]
                lastNonZero += 1

    # Note: copy non-zero to end of non-zero seq, like qs partition.
    #
    # for each pos in array
    #   if item not zero:
    #     copy to end of non-zero pos; non_zero_pos++
    # fill remaining A[non_zero_pos+1:] with 0

    # beats 92%, damn
    def move3_sol2(self, A, n):
        # from solution 2, damn
        # for every non-zero element, simply copy/append it to to the end of non-zero seq
        lastNonZero = 0
        for i in range(n):
            if A[i]:  # if not, simply i++
                A[lastNonZero] = A[i]  # may do some extra silly copy
                lastNonZero += 1
        for i in range(lastNonZero, n):  # fill last n with 0
            A[i] = 0


# my overly complicated solution, haha
class MySolution:

    # doesn't work, does not maintain non zero order (reversed)
    def move1(self, A, n):
        i = 0  # start from beginning
        j = n-1  # start from end
        while i < j:
            # move j left until first non zero
            while j > i and A[j] == 0:
                j -= 1
            # move i right until first zero
            while i < j and A[i]:
                i += 1

            if i < j:
                A[i], A[j] = A[j], A[i]
                i += 1
                j -= 1

    def find_zero(self, A, s, n):
        """find index of first 0 in A with size n"""
        for i in range(s, n):
            if A[i] == 0:
                return i
        return None

    def find_non_zero(self, A, s, n):
        """find index of first 0 in A with size n"""
        for i in range(s, n):
            if A[i] != 0:
                return i
        return None

    # this works, but only beats 10 % of submissions
    # take2, j resume from previous j, now beats 64%!!
    # I think the function call killed the speed
    def move2(self, A, n):
        i = 0  # start from beginning
        j = None
        while i < n:
            i = self.find_zero(A, i, n)  # find first zero
            if i is None:  # if not found, done
                break
            if j is None:
                j = i
            j = self.find_non_zero(A, j+1, n)  # find first non zero after it
            if j is None:  # if not found, done
                break
            A[i], A[j] = A[j], A[i]  # swap
            i += 1  # go to next element


class TestMoveZero(unittest.TestCase):

    def setUp(self):
        self.sol = Solution()

    def test1(self):
        A = [0,1,0,3,12]
        self.sol.moveZeroes(A)
        self.assertEqual(A, [1,3,12,0,0])


if __name__ == '__main__':
    unittest.main()
