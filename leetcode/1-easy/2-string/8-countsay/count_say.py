# https://leetcode.com/explore/interview/card/top-interview-questions-easy/127/strings/886/
# https://leetcode.com/problems/count-and-say/description/

# Count and Say
#
# Given an integer n, generate the nth term of the count-and-say
# sequence.
#
# The count-and-say sequence is the sequence of integers with the
# first five terms as following: 1, 11, 21, 1211, 111221

import re
import unittest

# cache = {1: '1'}
# highest = 1
cache = {}


class Solution:

    # Note: send previous say output as input for next say.
    #
    # repeat n-1 times:  # first one is "1"
    #   result = say_x(result)
    #
    # say_x() simply breaks result into groups of same chars, and
    # process each group and add to result:
    #   figure out length of group, convert len to string, write value
    #   write single instance of char
    
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        # return self.say_regular(n)
        return self.say_cached1(n)

    # non cached, beats 84.91%
    def say_regular(self, n):
        result = "1"
        for i in range(n-1):
            result = self.say_x(result)  # feed previous result into encoder

        return result

    def say_x(self, s):

        # breaks s into chunks of same chars, like
        # ['1111', '2', '3', '2', '111']
        data = [m.group(0) for m in re.finditer(r"(\d)\1*", s)]

        result = []
        for x in data:
            n = len(x)
            result.append(str(n))
            result.append(x[0])

        val = ''.join(result)

        return val

    # beats 98.37, slightly better I suppose
    def say_cached1(self, n):
        result = "1"
        for i in range(n-1):
            if i in cache:
                result = cache[i]
            else:
                result = self.say_x(result)  # feed previous result into encoder
                cache[i] = result
        return result

    # only 84.91%? disappointing, optimization is hard, even though
    # this seems like it should be better, haha.
    def say_cached2(self, n):
        global highest

        if n in cache:  # short circuit if in cache
            return cache[n]

        result = cache[highest]
        for i in range(highest+1, n+1):
            result = self.say_x(result)  # feed previous result into encoder
            cache[i] = result
            highest = i
        assert(highest == i)

        return result


class TestSay(unittest.TestCase):

    def setUp(self):
        self.sol = Solution()

    def test_say1(self):
        print(self.sol.countAndSay(1))
        print(self.sol.countAndSay(2))
        print(self.sol.countAndSay(3))
        print(self.sol.countAndSay(4))
        print(self.sol.countAndSay(5))


if __name__ == '__main__':
    unittest.main()
