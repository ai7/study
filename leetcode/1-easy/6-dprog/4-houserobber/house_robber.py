# https://leetcode.com/explore/interview/card/top-interview-questions-easy/97/dynamic-programming/576/
# https://leetcode.com/problems/house-robber/description/

# House Robber

# You are a professional robber planning to rob houses along a street.
# Each house has a certain amount of money stashed, the only
# constraint stopping you from robbing each of them is that adjacent
# houses have security system connected and it will automatically
# contact the police if two adjacent houses were broken into on the
# same night.
#
# Given a list of non-negative integers representing the amount of
# money of each house, determine the maximum amount of money you can
# rob tonight without alerting the police.

import functools


class Solution:
    
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        # return self.rob_memorize(nums)
        return self.rob_dp2(nums)

    # Note: max of 2 cases (rob this one, or rob next one)
    #
    # Go through array, and compute the max of 2 cases:
    # - rob this house + recurse on 2 houses down to end.
    # - recurse on the next house (don't rob current house)
    #
    # For bottom up dp, mainly recognize this is:
    #   f(k) = max( A[k] + f(k-2), f(k-1) )
    # so just start from 3rd element and apply this formula.
    #
    # dp is easier to visualize with a result array, but can be done
    # without creating an array (using 3 variables, a, b, c).
    
    # recursive with memorization
    def rob_memorize(self, A):

        @functools.lru_cache()
        def rob_helper(s, e):

            n = e - s  # number of houses we have
            if n < 1:  # nothing to rob
                return 0
            elif n == 1:  # only one house
                return A[s]

            # we have 2 cases, rob or don't rob first house
            case1 = A[s] + rob_helper(s + 2, e) # rob 1st house, plus remaining
            case2 = rob_helper(s + 1, e)  # don't rob first, with remaining

            return max(case1, case2)

        return rob_helper(0, len(A))

        # 69 / 69 test cases passed.
        # beats 81.59% of py3

    # bottom up dynamic programming approach
    #
    # f(0) = A[0]
    # f(1) = max(A[0], A[1])
    # f(k) = max( A[k]+f(k-2), f(k-1) )
    def rob_dp1(self, A):

        n = len(A)
        if n == 1:
            return A[0]

        f = [None] * n
        f[0] = A[0]
        f[1] = max(A[0], A[1])
        for i in range(2, n):
            f[i] = max(f[i-2] + A[i], f[i-1])
        return f[-1]

        # beats 98.56% of py3

    # without creating the array
    # figured out myself, yeah!
    def rob_dp2(self, A):

        n = len(A)
        if n == 1:
            return A[0]

        a = A[0]
        b = max(A[0], A[1])
        for i in range(2, n):
            c = max(a + A[i], b)  # rob ith house (plus k-2), or k-1
            a, b = b, c
        return b
