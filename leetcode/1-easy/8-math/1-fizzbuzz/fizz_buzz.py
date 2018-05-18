# https://leetcode.com/explore/interview/card/top-interview-questions-easy/102/math/743/
# https://leetcode.com/problems/fizz-buzz/description/

# Fizz Buzz
#
# Write a program that outputs the string representation of numbers
# from 1 to n
#   %3 -> Fizz
#   %5 -> Buzz
#   both -> FizzBuzz


class Solution:

    # this is too simple... ;)
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        retval = []

        for i in range(1, n+1):
            s = ""
            if i % 3 == 0:
                s += 'Fizz'
            if i % 5 == 0:
                s += 'Buzz'
            retval.append(s if s else str(i))

        return retval

    # beats 77.61