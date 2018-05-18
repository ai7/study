# https://leetcode.com/explore/interview/card/top-interview-questions-easy/97/dynamic-programming/569/
# https://leetcode.com/problems/climbing-stairs/description/

# Climbing Stairs
#
# You are climbing a stair case. It takes n steps to reach to the top.
# Each time you can either climb 1 or 2 steps. In how many distinct
# ways can you climb to the top?

import functools
import unittest


class Solution:

    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        return self.climb2(n)

    # nice way to calculate fib number
    def climb3(self, n):
        a = b = 1
        for _ in range(n):
            a, b = b, a + b
        return a

    # alternative version, when reach end, return 1, otherwise simple +
    @functools.lru_cache()
    def climb2(self, n):
        if n < 0:  # not a path if negative size
            return 0
        elif n == 0:  # reached top, return 1
            return 1
        else:  # sum of a + b branch
            return self.climb2(n - 1) + self.climb2(n - 2)  # this is actually fib number, damn!

        # 45 / 45 test cases passed.
        # beats 95.14%

    # my original version, +1 before branch, when reach end, return 0
    @functools.lru_cache()
    def climb1(self, n):
        if n < 1:
            return 0
        elif n == 1:  # one step, only one way
            return 1
        else:  # more than one step, can do both 1-step and 2-step
            a = self.climb1(n - 1)  # one step
            if a < 1:
                a = 1
            b = self.climb1(n - 2)  # two step
            if b < 1:
                b = 1
            return a + b

        # 45 / 45 test cases passed.
        # beats 95.14%


class TestClimb(unittest.TestCase):

    def setUp(self):
        self.sol = Solution()

    def test1(self):
        for i in range(5):
            print("{} {}".format(i, self.sol.climbStairs(i)))


if __name__ == '__main__':
    unittest.main()
