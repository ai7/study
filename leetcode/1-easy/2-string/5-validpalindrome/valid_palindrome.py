# https://leetcode.com/explore/interview/card/top-interview-questions-easy/127/strings/883/
# https://leetcode.com/problems/valid-palindrome/description/

# Valid Palindrome
#
# Given a string, determine if it is a palindrome, considering only
# alphanumeric characters and ignoring cases.

import collections
import unittest


class Solution:

    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s:
            return True

        # build list of lower case chars, ignore non alphanumeric
        chars = [x for x in s.lower() if x.isalnum()]

        # return chars == list(reversed(chars))
        return chars == chars[::-1]

        # 476 / 476 test cases passed.
        # beats 89.83%


class TestPalindrome(unittest.TestCase):

    def setUp(self):
        self.sol = Solution()

    def test1(self):
        s = 'A man, a plan, a canal: Panama'
        self.assertTrue(self.sol.isPalindrome(s))


if __name__ == '__main__':
    unittest.main()
