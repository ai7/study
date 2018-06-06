# https://leetcode.com/explore/interview/card/top-interview-questions-medium/113/math/820/
# https://leetcode.com/problems/divide-two-integers/description/

# Divide Two Integers
#
# Given two integers dividend and divisor, divide two integers without
# using multiplication, division and mod operator.
#
# Return the quotient after dividing dividend by divisor. The integer
# division should truncate toward zero.

import unittest


class Solution:

    # Note: use >> + - to calc, shift divisor until max...
    #
    # To calculate x/y without *, /, or %, we can use >>, +, or -.
    #
    # First we shift y n times so it is as big as possible while still
    # less than x. we can now add 1 shifted n times to the left to our
    # result.
    #
    # We then recursively work on the reminder of x - (y << n). If no
    # shift is possible, we simply count the number of times we can
    # subtract y from x and add that to the result.
    #
    # Some silly complication around sign and max int limit.

    # 989 / 989 test cases passed.
    # Status: Accepted
    # Runtime: 60 ms (beats 85.45% of py3)
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """

        # how many times can we need to shift y without > x?
        # return maximum shift, and reminder
        def calc_shift(x, y):
            cnt = 0
            while (y << 1) <= x:
                y <<= 1
                cnt += 1
            return cnt, x - y

        # calculate x / y, assume both positive
        def calc_divide(x, y):

            if x < y:  # ie, 5 / 10
                return 0
            elif x == y:  # easy case
                return 1

            res = 0
            d, r = calc_shift(x, y)  # power, reminder
            if d > 0:
                a = 1 << d
                b = calc_divide(r, y)
                # return 1 << d + calc_divide(r, y)
                return a + b

            cnt = 0  # no raise to power, simply count number of subtractions
            while x >= y:
                x -= y
                cnt += 1

            return cnt

        if dividend < 0 and divisor < 0:  # if both < 0
            res = calc_divide(-dividend, -divisor)  # simply flip sign
        elif dividend < 0 or divisor < 0:  # if only one is zero
            res = - calc_divide(abs(dividend), abs(divisor))
        else:  # all positive
            res = calc_divide(dividend, divisor)

        min_int = - 2 ** 31
        max_int = 2 ** 31 - 1
        # check for stupid range
        if res < min_int:
            res = min_int
        elif res > max_int:
            res = max_int

        return res


class TestDivide(unittest.TestCase):

    def setUp(self):
        self.sol = Solution()

    def test1(self):
        self.assertEqual(self.sol.divide(10, 3), 3)
        self.assertEqual(self.sol.divide(7, 3), 2)
        self.assertEqual(self.sol.divide(12312312, 3211), 3834)

    def test1b(self):
        self.assertEqual(self.sol.divide(7, -3), -2)
        self.assertEqual(self.sol.divide(10, -3), -3)
        self.assertEqual(self.sol.divide(-10, 3), -3)
        self.assertEqual(self.sol.divide(-10, -3), 3)
        self.assertEqual(self.sol.divide(9, -3), -3)
        self.assertEqual(self.sol.divide(-9, 3), -3)
        self.assertEqual(self.sol.divide(-9, -3), 3)

    def test2(self):
        self.assertEqual(self.sol.divide(-2147483648, -1), 2147483647)


if __name__ == '__main__':
    unittest.main()
