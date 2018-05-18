# https://leetcode.com/explore/interview/card/top-interview-questions-easy/102/math/745/
# https://leetcode.com/problems/power-of-three/description/

# Power of Three
#
# Given an integer, write a function to determine if it is a power of three.

# ie, 45 % 3 is 0, but 45 is not power of 3
# so it is not simply "n % 3 == 0" haha


class Solution:

    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return self.check1_divide(n)

    # option1: loop iteration: keep divide by 3 until 1
    def check1_divide(self, n):
        if n < 1:
            return False

        while n % 3 == 0:
            n //= 3

        return n == 1

    # option2: convert to base 3, and ensure it is like 10000...

    # option3, log(n)/log(3) should be integer, tricky to implement

    # option4: integer limitation
    def check4_int_limit(self, n):
        # 1162261467 = pow(3, 19), or 3^19, the highest n power of n for 32bit int
        return n > 0 and 1162261467 % n == 0
