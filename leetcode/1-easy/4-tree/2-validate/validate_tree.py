# https://leetcode.com/explore/interview/card/top-interview-questions-easy/94/trees/625/
# https://leetcode.com/problems/validate-binary-search-tree/description/

# Validate Binary Search Tree

# Given a binary tree, determine if it is a valid binary search tree
# (BST).

import sys

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:

    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        int_min = - sys.maxsize - 1
        int_max = sys.maxsize
        return self.validate(root, int_min, int_max)

    def validate(self, x, min_val, max_val):

        if x.val <= min_val or x.val >= max_val:  # validate self
            return False

        if x.left:
            if not self.validate(x.left, min_val, x.val):
                return False
        if x.right:
            if not self.validate(x.right, x.val, max_val):
                return False

        return True

    # 75 / 75 test cases passed.
    # beats 100% of py3 submission
