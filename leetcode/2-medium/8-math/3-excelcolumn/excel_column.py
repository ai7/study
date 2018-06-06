# https://leetcode.com/explore/interview/card/top-interview-questions-medium/113/math/817/
# https://leetcode.com/problems/excel-sheet-column-number/description/

# Excel Sheet Column Number
#
# Given a column title as appear in an Excel sheet, return its
# corresponding column number.

import unittest


class Solution:

    # Note: atoi in base 26

    # 1000 / 1000 test cases passed.
    # Status: Accepted (on 1st try, yeah!)
    # Runtime: 60 ms (beats 94.22% py3)
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0

        res = 0
        for c in s.upper():
            res *= 26
            res += ord(c) - ord('A') + 1
        return res


class TestColumn(unittest.TestCase):

    def setUp(self):
        self.sol = Solution()

    def test1(self):
        self.assertEqual(self.sol.titleToNumber('A'), 1)
        self.assertEqual(self.sol.titleToNumber('AB'), 28)
        self.assertEqual(self.sol.titleToNumber('ZY'), 701)


if __name__ == '__main__':
    unittest.main()
