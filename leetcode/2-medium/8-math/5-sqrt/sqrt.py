# https://leetcode.com/explore/interview/card/top-interview-questions-medium/113/math/819/

# Sqrt(x)
#
# Implement int sqrt(int x). Since the return type is an integer, the
# decimal digits are truncated and only the integer part of the result
# is returned.

import unittest


class Solution:

    # finally one that I worked out myself, hehe
    #
    # 1017 / 1017 test cases passed.
    # Status: Accepted
    # Runtime: 64 ms (beats 80.49% py3)
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < 2:
            return x

        low, high = 0, x
        last = None
        while low < high:

            m = (low + high) // 2  # find mid point
            if m == last:  # if not making progress, done
                break
            last = m

            m2 = m ** 2
            if m2 == x:  # found exact match, done
                return m
            elif m2 > x:  # m is too big, drop high to mid
                high = m
            else:  #  m2 < x, m is too small, raise low to mid
                low = m
            
        return last


class TestSqrt(unittest.TestCase):

    def setUp(self):
        self.sol = Solution()

    def test1(self):
        print(self.sol.mySqrt(20))
        print(self.sol.mySqrt(100))
        print(self.sol.mySqrt(101))
        print(self.sol.mySqrt(120))
        print(self.sol.mySqrt(121))


if __name__ == '__main__':
    unittest.main()
