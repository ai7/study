# https://leetcode.com/explore/interview/card/top-interview-questions-easy/99/others/722/
# https://leetcode.com/problems/missing-number/description/

# Missing Number
#
# Given an array containing n distinct numbers taken from 0, 1, 2,
# ..., n, find the one that is missing from the array.


class Solution:

    # 122 / 122 test cases passed.
    # Status: Accepted
    # Runtie: 44 ms (beats 99.54% of py3)
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        t = int((n * (n + 1)) / 2)
        return t - sum(nums)


    # neat bit trick from solution.
    #
    # Initialize an integer to n, and XOR it with every index and
    # value, we will be left with the missing number.
    def missingNumber2(self, nums):
        missing = len(nums)
        for i, num in enumerate(nums):
            missing ^= i ^ num
        return missing
