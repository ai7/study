# https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/727/
# https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/

# Remove Duplicates from Sorted Array
#
# Given a sorted array nums, remove the duplicates in-place such that
# each element appear only once and return the new length.

import unittest


class Solution:

    # Note: 2 pointer one pass copy solution.
    #
    # grow 2 region like qs partition.
    #
    # i (slow) starts with 1st element, j starts with 2nd element.
    # if A[i] and A[j] is different, increment i, and copy j to i.
    #
    # in essence, j is the frontier, whenever we encounter an element
    # that is different from our tail in smaller set, we add it to the
    # tail of our smaller set.
    #
    # since array is sorted, this will automatically ignore any
    # duplicates when A[i] == A[j]

    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return self.remove_dup2(nums)

    # simpler loop, from solution.
    # 161 / 161 test cases passed.
    # Status: Accepted
    # Runtime: 104 ms (beats 22.04% of py3)
    def remove_dup2(self, A):

        n = len(A)
        if n < 2:
            return n

        i = 0
        for j in range(1, n):
            if A[i] != A[j]:
                i += 1
                A[i] = A[j]

        return i+1

    # my version
    # use 2 pointers. i, left side, target, and j, right side, source.
    # advance j until next char is different (so j points to last
    # occurrence of current char), then copy j to i. increment both i &
    # j and repeat.
    def remove_dup(self, A):
        n = len(A)
        i = 0
        j = 0
        while j < n:
            A[i] = A[j]  # copy j to i
            while j+1 < n and A[j] == A[j + 1]:  # advance j while same
                j += 1
            i += 1
            j += 1
        return i


class TestRemoveDup(unittest.TestCase):

    def setUp(self):
        self.sol = Solution()

    def test1(self):
        A = [1, 2, 3, 4]
        v = self.sol.removeDuplicates(A)
        self.assertEqual(A[:v], [1, 2, 3, 4])

    def test2(self):
        A = [1, 2, 2, 2, 3, 4, 4, 4]
        v = self.sol.removeDuplicates(A)
        self.assertEqual(A[:v], [1, 2, 3, 4])


if __name__ == '__main__':
    unittest.main()
