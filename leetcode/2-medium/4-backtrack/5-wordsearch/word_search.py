# https://leetcode.com/explore/interview/card/top-interview-questions-medium/109/backtracking/797/
# https://leetcode.com/problems/word-search/description/

# Word Search
#
# Given a 2D board and a word, find if the word exists in the grid.
# The word can be constructed from letters of sequentially adjacent
# cell, where "adjacent" cells are those horizontally or vertically
# neighboring. The same letter cell may not be used more than once.

import unittest


class Solution:

    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        return self.my_search(board, word)

    # Note: run dfs on all matching 1st chars in board.
    #
    # in dfs, check whether current char is a match or not against the
    # current position in search word, if so, recurse on all 4
    # neighbors (clear char at current board position before recursive
    # dfs() call, and restore char after all 4 calls).

    # 87 / 87 test cases passed.
    # Status: Accepted (on 1st submit, yeah!)
    # Runtime: 260 ms
    def my_search(self, M, word):

        def dfs(pos, s):  # search from pos for string

            if not s:  # exhausted input, done
                return True

            r, c = pos[0], pos[1]  # check within board boundry
            if r < 0 or r >= rows:
                return False
            if c < 0 or c >= cols:
                return False

            if M[r][c] != s[0]:  # if current pos not match, done
                return False

            save = M[r][c]  # clear current char (so child dfs don't see it)
            M[r][c] = None
            retval = (dfs((r, c+1), s[1:]) or  # right
                        dfs((r, c-1), s[1:]) or  # left
                        dfs((r-1, c), s[1:]) or  # up
                        dfs((r+1, c), s[1:]))    # down
            M[r][c] = save

            return retval

        if not word:
            return False

        rows = len(M)
        cols = len(M[0])

        for i in range(rows):
            for j in [x for x, v in enumerate(M[i]) if v == word[0]]:
                if dfs((i, j), word):
                    return True

        return False


class TestWordSearch(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()
        self.board = [
            ['A', 'B', 'C', 'E'],
            ['S', 'F', 'C', 'S'],
            ['A', 'D', 'E', 'E']
        ]

    def test1(self):
        self.assertTrue(self.sol.exist(self.board, 'ABCCED'))
        self.assertTrue(self.sol.exist(self.board, 'SEE'))
        self.assertFalse(self.sol.exist(self.board, 'ABCB'))


if __name__ == '__main__':
    unittest.main()
