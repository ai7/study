# https://leetcode.com/explore/interview/card/top-interview-questions-medium/109/backtracking/795/
# https://leetcode.com/problems/permutations/description/

# Permutations
#
# Given a collection of distinct integers, return all possible
# permutations.

import unittest


class Solution:
    
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        return self.gen_permute(nums)

    # Note: backtrack, for each item in array, create a subproblem by
    #   add item to path, and recurse on array without this item. when
    #   array have been exhausted, add path to result. branch factor
    #   at each step is length of array at that step.
    
    # 25 / 25 test cases passed.
    # Status: Accepted (on 1st submit, yeah)
    # Runtime: 52 ms (beats 97.59% 10am)
    def gen_permute(self, nums):

        def backtrack(path, remain):
            if not remain:  # if exhausted list
                res.append(path)  # add current 'path' to result
                return
            for i in range(len(remain)):  # for each char in char list
                v = remain[i]
                data_next = remain[:i] + remain[i + 1:]  # copy list except pos i
                backtrack(path + [v], data_next)

        res = []
        if nums:
            backtrack([], nums)
        return res


class TestPermute(unittest.TestCase):

    def setUp(self):
        self.sol = Solution()

    def test1(self):
        print(self.sol.permute([1,2,3]))


if __name__ == '__main__':
    unittest.main()
