# https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/727/
# https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/

# Remove Duplicates from Sorted Array
#
# Given a sorted array nums, remove the duplicates in-place such that
# each element appear only once and return the new length.


class Solution:

    # Note: 2 pointer one pass copy solution.
    #
    # use 2 pointers. i, left side, target, and j, right side, source.
    # advance j until next char is different (so j points to last
    # occurrence of current char), then copy j to i. increment both i &
    # j and repeat.
    
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        i = 0
        j = 0
        while j < n:
            nums[i] = nums[j]  # copy j to i
            while j+1 < n and nums[j] == nums[j+1]:  # advance j while same
                j += 1
            i += 1
            j += 1
        return i
