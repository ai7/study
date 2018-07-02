# https://leetcode.com/explore/interview/card/top-interview-questions-hard/116/array-and-strings/828/
# https://leetcode.com/problems/spiral-matrix/description/

# Spiral Matrix
#
# Given a matrix of m x n elements (m rows, n columns), return all
# elements of the matrix in spiral order.

import unittest


class Solution:

    # Note: define start/end box, the rest should follow

    # 22 / 22 test cases passed.
    # Status: Accepted
    # Runtime: 40 ms
    def spiralOrder(self, M):

        if not M:
            return []

        n = len(M)      # of rows
        m = len(M[0])   # of columns
        retval = []

        # define start/end box
        row_s = 0
        row_e = n - 1
        col_s = 0
        col_e = m - 1

        while row_s <= row_e and col_s <= col_e:

            # if one item in box
            if row_s == row_e and col_s == col_e:
                retval.append(M[row_s][col_s])

            # if has only one row
            elif row_s == row_e:
                for x in range(col_s, col_e + 1):  # end+1 since no next step
                    retval.append(M[row_s][x])

            # if only has one column
            elif col_s == col_e:
                for x in range(row_s, row_e + 1):  # end+1 since no next step
                    retval.append((M[x][col_s]))

            else:
                # print top
                for x in range(col_s, col_e):  # for each list, add all but last
                    retval.append(M[row_s][x])

                # print right
                for x in range(row_s, row_e):
                    retval.append(M[x][col_e])

                # print bottom
                for x in range(col_e, col_s, -1):
                    retval.append(M[row_e][x])

                # print left
                for x in range(row_e, row_s, -1):
                    retval.append((M[x][col_s]))

            # shrink box
            row_s += 1
            row_e -= 1
            col_s += 1
            col_e -= 1

        return retval


class TestSpiral(unittest.TestCase):

    def setUp(self):
        self.sol = Solution()

    def test1(self):
        A = [[0, 1, 2, 3],
             [4, 5, 6, 7],
             [8, 9, 10, 11],
             [12, 13, 14, 15]]
        self.assertEqual(self.sol.spiralOrder(A),
                         [0, 1, 2, 3, 7, 11, 15, 14, 13, 12, 8, 4, 5, 6, 10, 9])

    def test2(self):
        B = [[0, 1, 2],
             [4, 5, 6],
             [8, 9, 10]]
        self.assertEqual(self.sol.spiralOrder(B),
                         [0, 1, 2, 6, 10, 9, 8, 4, 5])


if __name__ == '__main__':
    unittest.main()
