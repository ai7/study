# https://leetcode.com/explore/interview/card/top-interview-questions-medium/109/backtracking/794/
# https://leetcode.com/problems/generate-parentheses/description/

# Generate Parentheses
#
# Given n pairs of parentheses, write a function to generate all
# combinations of well-formed parentheses.

import unittest


class Solution:
    
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        return self.gen_paren1(n)

    # Note: recursively explore path, keep track of number of open and
    #   close parens left.
    #   - if no open and close paren left, done, add path as result
    #   - if no open paren, add all close paren to path and done.
    #   - if no close paren (but have open), use open and recurse on
    #     open-1 and close+1.
    #   - if both open/close available, recurse on booth
    
    # my solution, getting use to using inner functions!
    #
    # 8 / 8 test cases passed.
    # Status: Accepted (on 1st submit)
    # Runtime: 40 ms (beats 97.85% of py3)
    def gen_paren1(self, n):

        def dfs(path, a, b):  # prefix, # of open, # of close remaining
            if a <= 0 and b <= 0:  # exhausted all input, done
                res.append(path)
                return
            elif a <= 0:  # no more open paren (but have close paren)
                res.append(path + ')' * b)
                return
            elif b <= 0:  # no more close paren (but have open paren)
                dfs(path + '(', a-1, b+1)
            else:  # have both open/close paren available, branch into both
                dfs(path + '(', a-1, b+1)  # use open paren
                dfs(path + ')', a, b-1)  # use close paren

        res = []
        if n:
            dfs('', n, 0)
        return res


class TestParen(unittest.TestCase):

    def setUp(self):
        self.sol = Solution()

    def test1(self):
        print(self.sol.generateParenthesis(0))
        print(self.sol.generateParenthesis(1))
        print(self.sol.generateParenthesis(2))
        print(self.sol.generateParenthesis(3))


if __name__ == '__main__':
    unittest.main()
