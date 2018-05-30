# https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/770/
# https://leetcode.com/problems/rotate-image/description/

# Rotate Image
#
# You are given an n x n 2D matrix representing an image. Rotate the
# image by 90 degrees (clockwise).

import unittest


class Solution:

    # Note: process image in layers from outer layer down to n/2.
    #
    # for each layer, use 'start' and 'end' variable.
    #   for each individual row/column, use 'offset' variable
    #
    # the rest follows easily once we have these vars.

    # beats 97% of python submission
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        M = matrix
        n = len(matrix)

        for layer in range(int(n / 2)):  # for each layer

            start = layer  # first element
            end = n - start - 1  # last element

            for i in range(start, end):  # for all except last

                offset = i - start  # how far has i advanced from start

                # save top
                t = M[start][i]
                # top = left
                M[start][i] = M[end-offset][start]
                # left = bottom
                M[end-offset][start] = M[end][end-offset]
                # bottom = right
                M[end][end - offset] = M[i][end]
                # right = t
                M[i][end] = t


class TestRotate(unittest.TestCase):

    def setUp(self):
        self.sol = Solution()

    def test1(self):
        A = [[1,2,3],[4,5,6],[7,8,9]]
        self.sol.rotate(A)
        self.assertEqual(A, [[7,4,1],[8,5,2],[9,6,3]])

    def test2(self):
        A = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
        self.sol.rotate(A)
        self.assertEqual(A, [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]])


if __name__ == '__main__':
    unittest.main()
