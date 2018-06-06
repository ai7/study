# https://leetcode.com/explore/interview/card/top-interview-questions-medium/113/math/818/
# https://leetcode.com/problems/powx-n/description/

# Pow(x, n)
#
# Implement pow(x, n), which calculates x raised to the power n (x^n).
#
# Note:
#
# -100.0 < x < 100.0
# n is a 32-bit signed integer, within the range [-2^31, 2^31 - 1]

import unittest


class Solution:

    # Note: double or multiply depend on if n is even/odd.
    #
    # If n is even, we can use power of 2.
    # if n is odd, we can use multiply x.
    # A recursive solution works nicely. Alternatively we can
    # push operations we want to do on a stack, and then
    # do operation based on stack data.
    #
    # In each step, we either half n, or reduce n by one.
    # At least every other step is half, so runtime is
    # O(log n).

    # x^n, where x is not big, but n could be bit.
    #
    # 304 / 304 test cases passed.
    # Status: Accepted (on 1st try!)
    # Runtime: 40 ms (beats 99.65% py3)
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """

        def calc_pow(n):  # n should be positive
            if n == 1:  # base case
                return x
            elif n == 2:
                return x * x
            elif n % 2:  # if odd
                return x * calc_pow(n-1)
            else:
                v = calc_pow(n//2)
                return v * v

        if n == 0:
            return 1
        elif n > 0:
            return calc_pow(n)
        else:  # n < 0
            return 1 / calc_pow(-n)


class TestPow(unittest.TestCase):

    def setUp(self):
        self.sol = Solution()

    def test1(self):
        print(self.sol.myPow(2.0, 10))
        print(self.sol.myPow(2.1, 3))
        print(self.sol.myPow(2.0, -2))


if __name__ == '__main__':
    unittest.main()
