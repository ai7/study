# https://leetcode.com/explore/interview/card/top-interview-questions-easy/97/dynamic-programming/566/
# https://leetcode.com/problems/maximum-subarray/description/

# Maximum Subarray
#
# Given an integer array nums, find the contiguous subarray
# (containing at least one number) which has the largest sum and
# return its sum.


class Solution:
    
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        A = nums
        if not A:
            return 0

        max_local = max_global = A[0]
        for x in A[1:]:
            max_local = max(max_local+x, x)
            max_global = max(max_global, max_local)

        return max_global

    # 202 / 202 test cases passed.
    # beats 97.13%
