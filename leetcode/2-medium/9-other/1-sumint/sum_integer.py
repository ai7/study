# https://leetcode.com/explore/interview/card/top-interview-questions-medium/114/others/822/
# https://leetcode.com/problems/sum-of-two-integers/description/

# Sum of Two Integers
#
# Calculate the sum of two integers a and b, but you are not allowed
# to use the operator + and -.

import unittest


class Solution:

    # Note: a XOR b => add without carry, (a & b) << 1 => carry bits
    #
    # Then repeat again until carry becomes 0.
    #
    # A bit complicated for python, but what I came up with does work
    # for other languages such as Java/C.

    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        return self.my_sum2(a, b)

    # online solution that handles negative number in python, damn it.
    # 13 / 13 test cases passed.
    # Status: Accepted
    # Runtime: 32 ms (beats 100% of py3)
    def my_sum2(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        MAX_INT = 0x7FFFFFFF
        MIN_INT = 0x80000000
        MASK = 0x100000000
        while b:
            a, b = (a ^ b) % MASK, ((a & b) << 1) % MASK
        return a if a <= MAX_INT else ~((a % MIN_INT) ^ MAX_INT)

    # won't work for negative numbers, damn it.
    # it does work for other languages, just not python. double damn it.
    # python simulates infinite leading bits...
    def my_sum(self, a, b):

        # use XOR to add a and b, without considering carry
        # use AND with shift to calculate any carry.
        # keep using AND until number is 0.

        def bit_add(x, y):
            return x ^ y, (x & y) << 1

        a, b = bit_add(a, b)
        while b:
            a, b = bit_add(a, b)

        return a


class TestSum(unittest.TestCase):

    def setUp(self):
        self.sol = Solution()

    def test_positive(self):
        for i in range(10):
            for j in range(10):
                self.assertEqual(self.sol.getSum(i, j), i+j)

    def test_negative(self):
        self.assertEqual(self.sol.getSum(-1, 1), 0)


if __name__ == '__main__':
    unittest.main()
