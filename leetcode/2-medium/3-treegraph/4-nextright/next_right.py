# https://leetcode.com/explore/interview/card/top-interview-questions-medium/108/trees-and-graphs/789/
# https://leetcode.com/problems/populating-next-right-pointers-in-each-node/description/

# Populating Next Right Pointers in Each Node
#
# Given a binary tree, Populate each next pointer to point to its next
# right node. If there is no next right node, the next pointer should
# be set to NULL.

import collections
import unittest


# Definition for binary tree with next pointer.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None


class Solution:

    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        # self.connect_right1(root)
        self.connect_right2(root)

    # Note: use the next link we created to traverse a level.
    #
    # When we go through elements at level i, we are setting the next
    # pointer for elements in level i+1. For example, when we are at
    # root, we are creating the next pointer for our left child.
    # Therefore, the next level will always already have its next
    # pointers all set when we finish a level.
    #
    # We can use this fact to easily traverse the entire tree in level
    # order by simply following our next pointers, and set the next
    # level next pointers.
    #
    # since the tree is a perfect tree, we simply save the first node
    # at each level, and can go down a level by doing x.left.

    # iterative O(1) space solution
    # hint: make use of the next link we are creating (in parent)
    # we can assume the tree is a perfect binary tree (full and complete)
    #
    # 14 / 14 test cases passed.
    # Status: Accepted
    # Runtime: 116 ms (beat 14.86%, don't know why this would be slower)
    def connect_right2(self, x):
        if not x:
            return

        # for each level i, create the next pointer all child nodes at level i+1
        #   after process one node, use node's next pointer to go to next node.
        # then go to level i+1, repeat.
        while x.left:  # while we have a next level (remember perfect tree)

            curr = x  # used for walking current level
            while curr and curr.left:  # if have children, set their next pointers

                curr.left.next = curr.right  # left child's next => right child
                curr.right.next = curr.next.left if curr.next else None  # right child's next => next's left

                curr = curr.next  # go to next node on same level

            x = x.left  # go one level down

    # build a level list by doing a bfs walk of the tree
    # then process through each level and add the next pointer
    # ops, this doesn't satisfy the O(1) space requirement.
    #
    # 14 / 14 test cases passed.
    # Status: Accepted
    # Runtime: 82 ms (beats 73.28% of py3)
    def connect_right1(self, root):
        if not root:
            return
        A = self.level_bfs(root)
        for level in A:  # for each level
            for i in range(0, len(level)-1):
                level[i].next = level[i+1]

    def level_bfs(self, root):
        """Do a level walk of tree, return list of levels"""
        A = []  # result list
        q = collections.deque()  # queue for bfs search
        q.append(root)  # start with root

        while q:

            data = []  # list for this level

            for i in range(len(q)):  # for all item, which should be one level
                v = q.popleft()  # deque operation
                data.append(v)
                if v.left:  # add child (for next round/level)
                    q.append(v.left)
                if v.right:  # add child (for next round/level)
                    q.append(v.right)

            A.append(data)  # append level list to answer list

        return A


class TestConnect(unittest.TestCase):

    def setUp(self):
        self.sol = Solution()

    # not a complete tree
    @unittest.skip
    def test1(self):
        A = [3, 9, 20, None, None, 15, 7]
        root = build_tree(A, 0, len(A))
        self.sol.connect(root)
        print(root)

    def test_full_tree(self):
        A = [1, 2, 3, 4, 5, 6, 7]
        root = build_tree(A, 0, len(A))
        self.sol.connect(root)
        print(root)

def build_tree(A, i, n):
    """
    Build a tree from level array in leetcode

    :param A:  input array
    :param i:  start index
    :param n:  size of array
    :return: TreeNode
    """
    if i < n:

        if A[i] is None:  # return if null
            return

        x = TreeNode(A[i])
        x.left = build_tree(A, 2 * i + 1, n)
        x.right = build_tree(A, 2 * i + 2, n)

        return x


if __name__ == '__main__':
    unittest.main()
