# https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/546/
# https://leetcode.com/problems/two-sum/description/

# Two Sum
#
# Given an array of integers, return indices of the two numbers such
# that they add up to a specific target.


class Solution:

    # Note: one pass hashtable solution.
    #
    # for each element
    #   check if target - self is in hashtable.
    #   if not: add self to table, value is index.

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

    # can't use sort array and 2 pointer from both end
    # because we need to return index, not value, as sorting
    # the array would mess up the index.
