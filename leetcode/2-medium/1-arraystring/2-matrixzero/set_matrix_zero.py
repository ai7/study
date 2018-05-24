# https://leetcode.com/explore/interview/card/top-interview-questions-medium/103/array-and-strings/777/
# https://leetcode.com/problems/set-matrix-zeroes/description/

# Set Matrix Zeroes
#
# Given a m x n matrix, if an element is 0, set its entire row and
# column to 0. Do it in-place.


class Solution:

    # 159 / 159 test cases passed.
    # Status: Accepted
    # Runtime: 100 ms (beats 96.64% of py3)
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        M = matrix
        if not M:
            return

        m = len(matrix)  # rows
        n = len(matrix[0])  # cols

        row0 = False  # does row0 or col0 contains any zero?
        col0 = False

        # check if row0 contains 0
        if 0 in matrix[0]:
            row0 = True
        # check if col0 contains 0
        for i in range(m):
            if M[i][0] == 0:
                col0 = True
                break

        # now scan through rest of matrix
        # set row/col 0 entry to 0 if needed
        for i in range(1, m):
            for j in range(1, n):
                if M[i][j] == 0:
                    M[i][0] = 0  # set column 0 data to zero
                    M[0][j] = 0  # set row 0 data to zero

        # now set rows to 0 based on col0 data
        for i in range(1, m):
            if M[i][0] == 0:
                self.set_row_zero(M, i)

        # set cols to 0 based on row0 data
        for j in range(1, n):
            if M[0][j] == 0:
                self.set_col_zero(M, j)

        # finally set row0/col0
        if row0:
            self.set_row_zero(M, 0)
        if col0:
            self.set_col_zero(M, 0)

        return

    def set_row_zero(self, M, row):
        r = M[row]  # get the row
        for i in range(len(r)):  # for each item in row
            r[i] = 0

    def set_col_zero(self, M, col):
        for i in range(len(M)):  # for each row
            M[i][col] = 0  # set column col to zero
