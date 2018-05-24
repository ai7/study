# https://leetcode.com/explore/interview/card/top-interview-questions-medium/108/trees-and-graphs/786/
# https://leetcode.com/problems/binary-tree-inorder-traversal/description/

# Binary Tree Inorder Traversal
#
# Given a binary tree, return the inorder traversal of its nodes'
# values. (Recursive solution is trivial, could you do it
# iteratively?)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        # self.inorder_recursive(res, root)
        self.inorder_iter(res, root)

        return res

    # 68 / 68 test cases passed.
    # Status: Accepted (on first submit, yeah)
    # Runtime: 36 ms (beats 99.45% of py3)
    def inorder_iter(self, A, x):
        S = []  # stack
        while True:
            while x:
                S.append(x)
                x = x.left
            if not S:
                break
            x = S.pop()
            A.append(x.val)
            x = x.right

    def inorder_recursive(self, A, x):
        if x:
            self.inorder_recursive(A, x.left)
            A.append(x.val)
            self.inorder_recursive(A, x.right)
