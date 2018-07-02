# https://leetcode.com/explore/interview/card/top-interview-questions-hard/116/array-and-strings/831/
# https://leetcode.com/problems/game-of-life/description/

# Game of Life
#
# Write a function to compute the next state (after one update) of the
# board given its current state.
#
# 1. Any live cell with fewer than two live neighbors dies, as if
#    caused by under-population.
# 2. Any live cell with two or three live neighbors lives on to the
#    next generation.
# 3. Any live cell with more than three live neighbors dies, as if by
#    over-population..
# 4. Any dead cell with exactly three live neighbors becomes a live
#    cell, as if by reproduction.

import unittest


class Solution:

    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        return self.my_game(board)

    # Note: store result on bit 2
    #
    # To do this in place, store the next round result in 2nd bit. Use
    # helper function to help elements so we can more easily handle
    # out of bound neighbors.

    # 23 / 23 test cases passed.
    # Status: Accepted (on 1st submit)
    # Runtime: 40 ms (beats 96.62% py2)
    def my_game(self, M):

        # wrapper for accessing element that handles borders
        def access(i, j):
            return M[i][j] if -1 < i < rows and -1 < j < cols else 0

        def neighbors(i, j):
            return [[i-1, j-1], [i-1, j], [i-1, j+1],
                    [i, j-1], [i, j+1],
                    [i+1, j-1], [i+1, j], [i+1, j+1]]

        def neighbors_count(i, j):
            cnt = 0
            for x in neighbors(i, j):
                # check LSB only
                cnt += 1 if access(x[0], x[1]) & 1 else 0
            return cnt

        rows = len(M)
        cols = len(M[0])

        for i in range(rows):
            for j in range(cols):
                neighbor = neighbors_count(i, j)
                if not M[i][j]:  # currently dead
                    if neighbor == 3:
                        M[i][j] = 2  # set 2nd bit to on
                else:  # currently alive
                    if 1 < neighbor < 4:
                        M[i][j] |= 2  # set 2nd bit to on

        # finally go th through board and set 2nd bit to 1st bit
        for i in range(rows):
            for j in range(cols):
                M[i][j] >>= 1


class TestGame(unittest.TestCase):

    def setUp(self):
        self.sol = Solution()

    def test1(self):
        A = [
            [0, 1, 0],
            [0, 0, 1],
            [1, 1, 1],
            [0, 0, 0]
        ]
        self.sol.gameOfLife(A)
        self.assertEqual(A,
                         [
                             [0, 0, 0],
                             [1, 0, 1],
                             [0, 1, 1],
                             [0, 1, 0]
                         ]
                         )


if __name__ == '__main__':
    unittest.main()
