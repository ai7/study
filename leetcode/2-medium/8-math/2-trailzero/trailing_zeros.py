# https://leetcode.com/explore/interview/card/top-interview-questions-medium/113/math/816/
# https://leetcode.com/problems/factorial-trailing-zeroes/description/

# Factorial Trailing Zeroes
#
# Given an integer n, return the number of trailing zeroes in n!
#
# Note: Your solution should be in logarithmic time complexity.

import functools
import unittest


class Solution:

    # Note: how many multiple of 5, 5^2, 5^3, ...
    #
    # We need to calculate the number of 5s in the factorial expansion
    # of n. If n is 100!, this is 5, 10, 15, 20... 100.
    #
    # How many of these do we have? It's n/5. But we are not done. 25,
    # 50, 75 have one extra 5 in it. So we need to count those as well.
    #
    # How many, it's exactly count5() of n/5. This part is a bit
    # tricky to see. But essentially we are counting number of
    # multiple of 5, followed by number of multiple of 25 (each one
    # have 2 5s), then multiple of 125 (35s), etc.
    #
    # Ie, how many multiple of 25 are there in n? it's n/25.
    #
    # So this results in the recursion of
    # F(n) = n/5 + F(n/5)
    #
    # https://leetcode.com/problems/factorial-trailing-zeroes/discuss/52373/Simple-CC++-Solution-(with-detailed-explaination)

    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        return self.my_zeros3(n)

    # recursive approach
    def my_zeros3(self, n):
        if n < 5:
            return 0
        return n // 5 + self.my_zeros3(n // 5)

    # iterative approach
    # 502 / 502 test cases passed.
    # Status: Accepted
    # Runtime: 44 ms (beats 98.31% py3)
    def my_zeros4(self, n):
        res = 0
        while n >= 5:
            res += n // 5
            n //= 5
        return res


# my 2 solutions that didn't work for huge numbers.
class SolutionX:

    # still doesn't work, mostly the same as first one
    def my_zeros2(self, n):

        @functools.lru_cache()
        def count5(x):
            if x < 5 or x % 5:
                return 0
            else:
                return 1 + count5(x // 5)

        res = 0
        for i in range(5, n+1, 5):
            res += count5(i)

        return res

    # 500 / 502 test cases passed.
    # Time Limit Exceeded
    # Last executed input: 1808548329
    # this is still not fast enough?
    def my_zeros(self, n):

        if n < 5:
            return 0

        res = 0
        mem = {}

        for i in range(5, n+1, 5):  # step through to n in steps of 5
            cnt = 0
            t = i
            while t % 5 == 0:
                cnt += 1
                t //= 5
                if t in mem:
                    cnt += mem[t]
                    break
            res += cnt
            mem[i] = cnt

        return res


class TestZeros(unittest.TestCase):

    def setUp(self):
        self.sol = Solution()

    def test1(self):
        print(self.sol.trailingZeroes(5))
        print(self.sol.trailingZeroes(25))
        print(self.sol.trailingZeroes(100))
        print(self.sol.trailingZeroes(10000))
        print(self.sol.trailingZeroes(1808548329))


if __name__ == '__main__':
    unittest.main()
