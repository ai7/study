# https://leetcode.com/explore/interview/card/top-interview-questions-easy/102/math/878/
# https://leetcode.com/problems/roman-to-integer/description/

# Roman to Integer
#
# Given a roman numeral, convert it to an integer. Input is guaranteed
# to be within the range from 1 to 3999

import unittest


ROMAN = {
    'I': 1,  # regular chars
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000,

    'IV': 4,  # special combos
    'IX': 9,
    'XL': 40,
    'XC': 90,
    'CD': 400,
    'CM': 900
}


class Solution:

    # Note: check special combo, then regular search
    #
    # For each position, first check double digit combo, if so,
    # consume 2 chars. If not, use as single chars.

    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0

        retval = 0

        n = len(s)
        i = 0
        while i < n:

            if n - i == 1:  # if only one char remain
                retval += ROMAN[s[i]]
                i += 1
                continue

            # try special combo
            v = ROMAN.get(s[i:i+2], 0)
            if v:
                retval += v
                i += 2
            else:
                retval += ROMAN[s[i]]
                i += 1

        return retval

    # 3999 / 3999 test cases passed.
    # beat 95.09%, yeah!


class TestRoman(unittest.TestCase):

    def setUp(self):
        self.sol = Solution()

    def test1(self):
        self.assertEqual(self.sol.romanToInt('III'), 3)
        self.assertEqual(self.sol.romanToInt('IV'), 4)
        self.assertEqual(self.sol.romanToInt('IX'), 9)
        self.assertEqual(self.sol.romanToInt('LVIII'), 58)
        self.assertEqual(self.sol.romanToInt('MCMXCIV'), 1994)


if __name__ == '__main__':
    unittest.main()
