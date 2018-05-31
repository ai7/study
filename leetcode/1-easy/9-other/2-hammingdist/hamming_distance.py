# https://leetcode.com/explore/interview/card/top-interview-questions-easy/99/others/762/
# https://leetcode.com/problems/hamming-distance/description/

# Hamming Distance
#
# The Hamming distance between two integers is the number of positions
# at which the corresponding bits are different.
#
# Given two integers x and y, calculate the Hamming distance.


class Solution(object):

    # Note: count the number of bits in x XOR y
    #
    # XOR returns 0 if bits are same, 1 if differ.
    
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        # 36ms
        # 149 / 149 test cases passed.
        # beats 100% of python3 submission, hehe
        bin(x ^ y).count('1')

        # basically XOR the 2 number, then count the number of 1s
