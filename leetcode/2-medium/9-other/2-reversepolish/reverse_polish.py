# https://leetcode.com/explore/interview/card/top-interview-questions-medium/114/others/823/
# https://leetcode.com/problems/evaluate-reverse-polish-notation/description/

# Evaluate the value of an arithmetic expression in Reverse Polish
# Notation.
#
# Valid operators are +, -, *, /. Each operand may be an integer or
# another expression.

import operator
import unittest


class Solution:

    # Note: use stack to evaluate, push result back on stack
    #
    # On number, push to stack. On operation, pop 2 from stack, apply
    # operation, and push result back on stack.

    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        return self.my_rpn(tokens)

    # 20 / 20 test cases passed.
    # Status: Accepted (on 1st try!)
    # Runtime: 44 ms (beats 97.97% py3)
    def my_rpn(self, tokens):

        if not tokens:
            return 0

        ops = {
            '+': operator.add,
            '-': operator.sub,
            '*': operator.mul,
            '/': operator.truediv
        }

        s = []
        for x in tokens:

            if x in ['+', '-', '*', '/']:
                b = s.pop()
                a = s.pop()
                v = int(ops[x](a, b))
                s.append(v)
            else:
                s.append(int(x))

        return s[0]


class TestRpn(unittest.TestCase):

    def setUp(self):
        self.sol = Solution()

    def test1(self):
        self.assertEqual(self.sol.evalRPN(["2", "1", "+", "3", "*"]), 9)
        self.assertEqual(self.sol.evalRPN(["4", "13", "5", "/", "+"]), 6)
        self.assertEqual(self.sol.evalRPN(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]), 22)


if __name__ == '__main__':
    unittest.main()
