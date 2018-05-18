# https://leetcode.com/explore/interview/card/top-interview-questions-easy/127/strings/880/
# https://leetcode.com/problems/reverse-integer/description/

# Reverse Integer
#
# Given a 32-bit signed integer, reverse digits of an integer.


class Solution:

    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """

        str_x = str(x)  # convert int to str
        n = len(str_x)

        s = []
        negative = False

        for i in reversed(range(n)):
            if str_x[i] == '-':
                negative = True
                break  # done if we reach negative sign
            s.append(str_x[i])

        x = ''.join(s)  # convert array back to str
        x = int(x)  # convert back to int (will drop leading 0)
        if negative:  # finally add negative sign
            x = -x

        if x > 2147483647 or x < -2147483648:
            return 0

        return x

        # 1032 / 1032 test cases passed.
        # beat 85.29% of py3 submission
