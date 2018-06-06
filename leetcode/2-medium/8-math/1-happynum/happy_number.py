# https://leetcode.com/explore/interview/card/top-interview-questions-medium/113/math/815/
# https://leetcode.com/problems/happy-number/description/

# Write an algorithm to determine if a number is "happy".
#
# A happy number is a number defined by the following process:
# Starting with any positive integer, replace the number by the sum of
# the squares of its digits, and repeat the process until the number
# equals 1 (where it will stay), or it loops endlessly in a cycle
# which does not include 1. Those numbers for which this process ends
# in 1 are happy numbers.

import unittest


class Solution:

    # Note: calculate next number and check if in history
    #
    # calculate the next number and check if we have seen it before.

    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return self.my_happy(n)

    # 401 / 401 test cases passed.
    # Status: Accepted
    # Runtime: 48 ms (beats 97.65% of py3)
    def my_happy(self, n):

        if n <= 0:
            return False
        elif n == 1:
            return True

        history = set()  # track the set of numbers we've seen
        history.add(n)

        while n != 1:

            # s = str(n)  # convert to string
            # s2 = [int(x) ** 2 for x in s]  # array of x^2 for each digit x
            # n = sum(s2)  # sum of those numbers

            n = sum([int(x) ** 2 for x in str(n)])
            if n in history:
                return False  # cycle, break
            else:
                history.add(n)

        return True


class TestHappy(unittest.TestCase):

    def setUp(self):
        self.sol = Solution()

    def test1(self):
        self.assertTrue(self.sol.isHappy(19))
        self.assertFalse(self.sol.isHappy(2))


if __name__ == '__main__':
    unittest.main()
