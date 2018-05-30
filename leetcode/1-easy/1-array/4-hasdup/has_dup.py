# https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/578/
# https://leetcode.com/problems/contains-duplicate/description/

# Contains Duplicate
#
# Given an array of integers, find if the array contains any
# duplicates.


class Solution:

    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if not nums:
            return False

        return self.dup2(nums, len(nums))

    # Note: convert to sets and compare length.

    # trivial solution using sets.
    # I suppose this works, since I see submissions like it
    def dup2(self, A, n):
        return len(set(A)) != len(A)

    # brute force, time limit exceeded
    def dup(self, A, n):
        for i in range(n):
            for j in range(i, n):
                if A[i] == A[j]:
                    return True
        return False
