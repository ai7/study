# https://leetcode.com/explore/interview/card/top-interview-questions-easy/99/others/565/
# https://leetcode.com/problems/number-of-1-bits/description/

# Number of 1 Bits
#
# Write a function that takes an unsigned integer and returns the
# number of '1' bits it has (also known as the Hamming weight).

class Solution(object):

    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        return self.hamming2(n)

    # Note: clear right most bit that is on, then repeat until x is 0
    #
    # Clear right most bit that is on with "(n & n-1)", then repeat
    # until n is 0 (no longer True)
    #
    # Another option is to use python bin(x), which returns "0bxxxxx",
    # and use the count('1') function on string to count the number of
    # 1s.
    #
    # Standard solution is to check LSB and shift until x is 0.
    
    # regular impl based on bit trick
    def hamming1(self, n):

        count = 0
        while n:
            count += 1
            n &= (n - 1)  # clear right most 1 (n & n-1)

        return count

        # 49ms
        # beats 19.02%

    # using python bin() operation to convert to binary string repl
    def hamming2(self, n):

        return bin(n).count('1')

        # 37ms
        # beats 86.05%, wow
