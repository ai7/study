# https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/546/
# https://leetcode.com/problems/two-sum/description/

# Two Sum
#
# Given an array of integers, return indices of the two numbers such
# that they add up to a specific target.


class Solution:

    # one pass hashtable, beats 100% of submissions, yeah!
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        # we need x + y = target
        A = nums
        s = {}
        for i in range(len(A)):
            x = A[i]
            y = target - x
            if y in s:  # if y already exist in table
                return [s[y], i]
            s[x] = i

        return []
