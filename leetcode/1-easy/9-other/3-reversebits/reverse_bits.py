# https://leetcode.com/explore/interview/card/top-interview-questions-easy/99/others/648/
# https://leetcode.com/problems/reverse-bits/description/

# Reverse Bits
#
# Reverse bits of a given 32 bits unsigned integer.

# this is not flip the bits, but rather, reverse the bits (like reverse string)

import unittest


class Solution:

    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        return self.my_reverse2(n)

    # Note: for each bit in n, set bit in m and shift left
    #
    # process n from right (LSB), set m from right and shift result
    # left.

    # reverse via bit operation
    def my_reverse2(self, n):
        m = 0
        for i in range(32):
            m <<= 1  # shift current result to left
            m |= n & 1  # set LSB on m
            n >>= 1  # shift input to right
        return m

    # 600 / 600 test cases passed.
    # 35ms
    # beats 99.32% of python submission
    def my_reverse(self, n):
        # bin(n)[2:]       # convert to bin, chop off '0b' prefix
        # .rjust(32, '0')  # fill left with 0 until width is 32
        # int(x[::-1], 2)  # reverse, then convert int from base2
        return int(bin(n)[2:].rjust(32, '0')[::-1], 2)


class TestReverse(unittest.TestCase):

    def setUp(self):
        self.sol = Solution()

    def test1(self):
        print(self.sol.reverseBits(123))


if __name__ == '__main__':
    unittest.main()
