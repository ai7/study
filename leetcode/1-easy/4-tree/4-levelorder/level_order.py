# https://leetcode.com/explore/interview/card/top-interview-questions-easy/94/trees/628/
# https://leetcode.com/problems/binary-tree-level-order-traversal/description/

# Binary Tree Level Order Traversal
#
# Given a binary tree, return the level order traversal of its nodes'
# values. (ie, from left to right, level by level).

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        A = []
        if root:
            self.level(A, root, 0)
        return A

    def level(self, A, x, n):

        if len(A) <= n:  # if level x does not exist in answer
            A.append([x.val])  # add list with item in it
        else:
            A[n].append(x.val)  #

        if x.left:
            self.level(A, x.left, n+1)
        if x.right:
            self.level(A, x.right, n+1)

        # 34 / 34 test cases passed.
        # beat 97.03% of submission

    # if have time to an iterative approach
