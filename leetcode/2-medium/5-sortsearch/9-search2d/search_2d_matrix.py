# https://leetcode.com/explore/interview/card/top-interview-questions-medium/110/sorting-and-searching/806/
# https://leetcode.com/problems/search-a-2d-matrix-ii/description/

# Search a 2D Matrix II
#
# Write an efficient algorithm that searches for a value in an m x n
# matrix. This matrix has the following properties:
#
# - Integers in each row are sorted in ascending from left to right.
# - Integers in each column are sorted in ascending from top to bottom.


class Solution:

    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        return self.my_search(matrix, target)

    # Note: start from top/right, go left or down.
    #
    # start from the top right corner
    #   go down if > k,
    #   go left if < k.
    # this allow us to advance by 1 step in each round.
    # runtime will be O(m+n).
    #
    # we can also start from bottom left, the situation is
    # symmetrical.
    #   go right if > k
    #   go up if < k

    # amazon phone screen question.

    # 129 / 129 test cases passed.
    # Status: Accepted
    # Runtime: 56 ms
    def my_search(self, A, k):
        if not A:
            return False
        rows = len(A)
        cols = len(A[0])

        i, j = 0, cols-1  # start from top right
        while i < rows and j >= 0:

            v = A[i][j]
            if k == v:  # found
                return True
            elif k > v:  # higher, go down
                i += 1
            else:  # lower, go left
                j -= 1

        return False
