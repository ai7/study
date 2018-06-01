# https://leetcode.com/explore/interview/card/top-interview-questions-medium/108/trees-and-graphs/792/
# https://leetcode.com/problems/number-of-islands/description/

# Number of Islands
#
# Given a 2d grid map of '1's (land) and '0's (water), count the
# number of islands. An island is surrounded by water and is formed by
# connecting adjacent lands horizontally or vertically. You may assume
# all four edges of the grid are all surrounded by water.

import unittest


class Solution:

    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        return self.check_island(grid)

    # Note: number of BFS runs is the number of islands in grid.
    #
    # - go through matrix, and build a graph as simple set of (x,y)
    #   coordinates (that have matrix value '1').
    # - then run DFS on graph set (no need to build neighbor list
    #   since we know what the neighbors are).
    # - number of island is number of DFS run we do at top level.
    #
    # This is a read-only solution that don't touch input data.
    # Alternatively, we can run BFS directly on matrix by marking
    # visited node.

    # 47 / 47 test cases passed.
    # Status: Accepted
    # Runtime: 124 ms (beats 26.50% of py3)
    # again: Runtime: 68 ms (beats 93.70% py3, hmmmm)
    #
    # can also work by directly modifying the array, likely faster
    # but I like my read-only solution, does not touch input.
    def check_island(self, M):

        if not M:
            return
        rows = len(M)
        cols = len(M[0])

        # first build the list of nodes (coordinate of islands)
        nodes = set()  # coordinates of islands
        for i in range(rows):
            for j in range(cols):
                if M[i][j] == '1':  # islands
                    nodes.add((i, j))

        # now run dfs
        count = 0
        while nodes:
            x = next(iter(nodes))  # get a random node
            self.dfs2(x, nodes, rows, cols)  # run dfs on G from this node
            count += 1

        return count

    # this is recursive dfs, easy
    # maybe iterative would be faster?
    def dfs2(self, x, nodes, rows, cols):

        # visit this node, which is basically remove it from graph
        nodes.remove(x)

        row, col = x[0], x[1]  # generate the coordinate of 4 neighbors
        x1 = (row, col+1)  # next
        x2 = (row, col-1)  # prev
        x3 = (row-1, col)  # up
        x4 = (row+1, col)  # down

        if x1 in nodes:
            self.dfs2(x1, nodes, rows, cols)
        if x2 in nodes:
            self.dfs2(x2, nodes, rows, cols)
        if x3 in nodes:
            self.dfs2(x3, nodes, rows, cols)
        if x4 in nodes:
            self.dfs2(x4, nodes, rows, cols)


class TestIslands(unittest.TestCase):

    def setUp(self):
        self.sol = Solution()

    def test1(self):
        grid = [
            list('11110'),
            list('11010'),
            list('11000'),
            list('00000')
        ]
        self.assertEqual(self.sol.numIslands(grid), 1)

    def test2(self):
        grid = [
            list('11000'),
            list('11000'),
            list('00100'),
            list('00011')
        ]
        self.assertEqual(self.sol.numIslands(grid), 3)


if __name__ == '__main__':
    unittest.main()
