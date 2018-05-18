# https://leetcode.com/explore/interview/card/top-interview-questions-easy/99/others/721/
# https://leetcode.com/problems/valid-parentheses/description/

# Valid Parentheses
#
# Given a string containing just the characters '(', ')', '{', '}',
# '[' and ']', determine if the input string is valid.

import unittest


class Solution:

    # 76 / 76 test cases passed.
    # Status: Accepted
    # Runtime: 40 ms (beats 90.78% py3)
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        stack = []

        for c in s:

            if c in '({[':
                # for each char, push the required matching to stack
                if c == '(':
                    stack.append(')')
                elif c == '{':
                    stack.append('}')
                elif c == '[':
                    stack.append(']')

            elif c in ')}]':
                if not stack:  # nothing on stack
                    return False  # fail
                v = stack.pop() # top of stack should match current char
                if v != c:
                    return False

        return not stack  # stack should be empty at the end


class TestParen(unittest.TestCase):

    def setUp(self):
        self.sol = Solution()

    def test1(self):
        self.assertFalse(self.sol.isValid("([)]"))


if __name__ == '__main__':
    unittest.main()