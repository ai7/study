# https://leetcode.com/explore/interview/card/top-interview-questions-medium/109/backtracking/793/
# https://leetcode.com/problems/letter-combinations-of-a-phone-number/description/

# Letter Combinations of a Phone Number
#
# Given a string containing digits from 2-9 inclusive, return all
# possible letter combinations that the number could represent.

import unittest


# map of digits to list of letters

DIGITS = {
    '1': [],
    '2': list('abc'),
    '3': list('def'),
    '4': list('ghi'),
    '5': list('jkl'),
    '6': list('mno'),
    '7': list('pqrs'),
    '8': list('tuv'),
    '9': list('wxyz')
}


class Solution:

    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        # we need a variable number of nested loops
        return self.combo1(digits)
        # return self.combo2(digits)

    # Note: use simple backtrack. for each possible char for digit,
    #   generate a subproblem by adding char to path, and recurse on
    #   remaining digits. When no more digits, add path to result.
        
    # cleaner dfs using inner function from discussion
    # dfs() don't need to take on so many parameters,
    # just the ones that change from level to level.
    def combo2(self, digits):

        def dfs(path, idx):  # prefix so far, and index for digits
            if idx == len(digits):  # reached leaf node
                res.append(path)  # insert answer into res array
                return
            for c in DIGITS[digits[idx]]:  # for each char the digit maps to
                dfs(path + c, idx + 1)  # run dfs from this location

        res = []  # return result here
        if digits:
            dfs('', 0)
        return res

    # my version, made into inner function later
    #
    # 25 / 25 test cases passed.
    # Status: Accepted
    # Runtime: 36 ms (beats 97.83% of py3)
    def combo1(self, digits):

        def build_list(input, path):
            if not input:  # leaf node, done
                res.append(path)
                return
            for v in DIGITS[input[0]]:  # for each char
                build_list(input[1:], path + v)

        res = []
        if digits:
            build_list(digits, '')
        return res


class TestCombination(unittest.TestCase):

    def setUp(self):
        self.sol = Solution()

    def test1(self):
        print(self.sol.letterCombinations('23'))
        print(self.sol.letterCombinations('2345'))


if __name__ == '__main__':
    unittest.main()
