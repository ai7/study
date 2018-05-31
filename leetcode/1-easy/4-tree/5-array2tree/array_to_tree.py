# https://leetcode.com/explore/interview/card/top-interview-questions-easy/94/trees/631/
# https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/description/

# Convert Sorted Array to Binary Search Tree
#
# Given an array where elements are sorted in ascending order, convert
# it to a height balanced BST.


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    # Note: start with middle, and recursively build left/right tree
    #
    # pick middle of array and create Node x, then recursively build
    # left child with array items to the left, and right child with
    # array items to the right.
    #
    # special case 0, 1, 2 elements for speed.
    
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        return self.build_tree(nums, 0, len(nums))

    def build_tree(self, A, s, e):
        """
        Build a tree from sorted array

        :param A: input array
        :param s: starting index
        :param e: ending index +1 (ie, python slicing)
        :return: tree
        """
        n = e - s  # number of elements

        if n <= 0:
            return
        elif n == 1:  # just return one node
            return TreeNode(A[s])
        elif n == 2:  # special case for speed
            # ideally pick one of 2 possible configurations at random
            x = TreeNode(A[s+1])  # 2nd item as root
            x.left = TreeNode(A[s])  # 1st item as left child
            return x
        else:  # 3+ nodes
            m = (s + e) / 2
            x = TreeNode(A[m])
            x.left = self.build_tree(A, s, m)
            x.right = self.build_tree(A, m+1, e)
            return x

        # 32 / 32 test cases passed.
        # beats 98.35% of submissions
