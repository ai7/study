# https://leetcode.com/explore/interview/card/top-interview-questions-hard/116/array-and-strings/827/
# https://leetcode.com/problems/product-of-array-except-self/description/

# Product of Array Except Self
#
# Given an array nums of n integers where n > 1, return an array
# output such that output[i] is equal to the product of all the
# elements of nums except nums[i].

# Note: Please solve it without division and in O(n).

import unittest


class Solution:

    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        return self.my_prod2(nums)

    # Note: use 2 array to store cumulative prod from left & right
    #
    # Use 2 additional memo array to store cumulative products from
    # left and right side respectively. Then we can simply compute our
    # final result by fetching the relevant result from left/right
    # memo array to compute product except this current node.
    #
    # Alternatively, we don't actually need 2 separate array.
    #
    # We first compute cumulative product of left half (but shifted so
    # that res[i] contains products of i's left elements, so res[0] is
    # always 1, res[1] is A[0], res[-1] is all except last).
    #
    # at this point, res[i] contains half of the answer, the left
    # side. The trick is that we can do the same thing, and add in the
    # right side result directly to res[i] while processing from right
    # end without requiring any extra space.
    #
    # The first solution is easier to remember, but code is more. 2nd
    # solution is tricker to come up with, but easier to code.

    # from solution, don't need 2 separate array
    # 17 / 17 test cases passed.
    # Status: Accepted
    # Runtime: 100 ms
    def my_prod2(self, A):

        if not A:  # some sanity check and edge cases
            return []
        n = len(A)
        if n < 2:
            return []

        res = [1] * n  # return value

        # first pass, res[i] stores cumulative product of [0, i-1] (left side)
        # res[0] is a dummy value 1, since its left side is empty
        p = 1
        for i in range(n):
            res[i] = p
            p *= A[i]

        # what's missing now in res[i] is simply the right side, so we
        # run through another iteration to include the right side
        p = 1
        for i in reversed(range(n)):
            res[i] *= p  # update result by adding right cumulative product
            p *= A[i]

        return res

    # 17 / 17 test cases passed.
    # Status: Accepted (on 1st try)
    # Runtime: 112 ms (beats 74.14% py3)
    def my_prod(self, A):

        if not A:  # some sanity check and edge cases
            return []
        n = len(A)
        if n < 2:
            return []

        res = [None] * n  # return value

        left = [A[0]] * n  # cumulative product from left side -->
        right = [A[-1]] * n  # cumulative product from right side <--

        for i in range(1, n):  # fill left side cache result
            left[i] = left[i-1] * A[i]

        for i in reversed(range(0, n-1)):
            right[i] = right[i+1] * A[i]

        # now compute result
        for i in range(n):
            p1 = 1 if i == 0 else left[i-1]  # prod of left side
            p2 = 1 if i == n-1 else right[i+1]  # prod of right side
            res[i] = p1 * p2

        return res


class TestProduct(unittest.TestCase):

    def setUp(self):
        self.sol = Solution()

    def test1(self):
        self.assertEqual(self.sol.productExceptSelf([1,2,3,4]),
                         [24, 12, 8, 6])


if __name__ == '__main__':
    unittest.main()
