# https://leetcode.com/explore/interview/card/top-interview-questions-easy/127/strings/884/
# https://leetcode.com/problems/string-to-integer-atoi/description/

# String to Integer (atoi)
#
# Implement atoi which converts a string to an integer.


class Solution:

    # Note: left to right, and *= 10 result each time.
    
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0

        s = s.strip()  # trim whitespace from both ends
        if not s:
            return 0

        negative = False
        start = 0
        if s[0] == '-':
            negative = True
            start = 1
        elif s[0] == '+':
            start = 1

        v = 0
        for i in range(start, len(s)):

            c = s[i]  # get the char
            if not c.isdigit():
                break

            v *= 10
            v += ord(c) - ord('0')

        if negative:
            v = -v

        # shrink to min/max int
        if v > 2147483647:
            v = 2147483647
        elif v < -2147483648:
            v = -2147483648

        return v

        # 1079 / 1079 test cases passed.
        # beats 99% of python3 submission
