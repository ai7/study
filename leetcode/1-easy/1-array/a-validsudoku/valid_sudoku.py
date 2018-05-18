# https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/769/
# https://leetcode.com/problems/valid-sudoku/description/

# Valid Sudoku
#
# Determine if a 9x9 Sudoku board is valid. Only the filled cells need
# to be validated.


class Solution:

    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        M = board  # shorthand for Matrix

        for i in range(9):  # check all rows
            if not self.check_row(M, i):
                return False
        for j in range(9):  # check all cols
            if not self.check_col(M, j):
                return False

        for i in range(0, 9, 3):  # check all 3x3 boxes
            for j in range(0, 9, 3):
                if not self.check_box(M, i, j):
                    return False

        return True

    def _check_val(self, s, v):
        if not v or v == '.':  # skip if dot (empty)
            return True
        d = int(v)
        if d < 1 or d > 9:  # should be between 1-9
            return False
        if v in s:
            return False
        s.add(v)
        return True

    def check_row(self, M, row):
        s = set()
        for v in M[row]:  # for each value in row i
            if not self._check_val(s, v):
                return False
        return len(s) < 10

    def check_col(self, M, col):
        s = set()
        for i in range(9):
            v = M[i][col]
            if not self._check_val(s, v):
                return False
        return len(s) < 10

    def check_box(self, M, row, col):
        """Check 3x3 box starting at row/col"""
        s = set()
        for i in range(3):
            for j in range(3):
                v = M[row+i][col+j]
                if not self._check_val(s, v):
                    return False
        return len(s) < 10

    # 475 / 504 test cases passed.
    # 504 / 504 test cases passed. (beats 68%)
