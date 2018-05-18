# https://leetcode.com/explore/interview/card/top-interview-questions-easy/99/others/648/
# https://leetcode.com/problems/reverse-bits/description/

# Reverse Bits
#
# Reverse bits of a given 32 bits unsigned integer.

# this is not flip the bits, but rather, reverse the bits (like reverse string)

class Solution:

    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):

        # bin(n)[2:]       # convert to bin, chop off '0b' prefix
        # .rjust(32, '0')  # fill left with 0 until width is 32
        # int(x[::-1], 2)  # reverse, then convert int from base2
        return int(bin(n)[2:].rjust(32, '0')[::-1], 2)

        # 600 / 600 test cases passed.
        # 35ms
        # beats 99.32% of python submission
