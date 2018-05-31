# https://leetcode.com/explore/interview/card/top-interview-questions-easy/99/others/601/
# https://leetcode.com/problems/pascals-triangle/description/

# Pascal's Triangle
#
# Given a non-negative integer numRows, generate the first numRows of
# Pascal's triangle.

import unittest
import pprint


class Solution:

    # Note: 1 for 1st/last, and sum for every pair in previous.
    #
    # for each row
    #   first add '1'
    #   then for each pair in previous row
    #     add sum of said pair
    #   finally add '1' (and add array to answer)

    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows < 1:
            return []

        A = [[1]]  # start with 1st row filled in

        for r in range(1, numRows):  # for the remaining n-1 rows

            prev = A[r-1]  # previous row data
            v = [1]  # start with 1 in current row
            for i in range(len(prev) - 1):  # for every pair in prev list
                v.append(prev[i]+prev[i+1])
            v.append(1)  # finally end with another one

            A.append(v)  # add row i to answer

        return A

    # 15 / 15 test cases passed.
    # Status: Accepted
    # Runtime: 36 ms (beat 98.45% py3)


class TestPascal(unittest.TestCase):

    def setUp(self):
        self.sol = Solution()

    def test1(self):
        pprint.pprint(self.sol.generate(5))


if __name__ == '__main__':
    unittest.main()
