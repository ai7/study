# https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/549/
# https://leetcode.com/problems/single-number/description/

# Single Number
#
# Given a non-empty array of integers, every element appears twice
# except for one. Find that single one.


class Solution:

    # Note: XOR all the numbers together. Result is missing number.
    
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        v = nums[0]
        for x in nums[1:]:
            v ^= x
        return v
