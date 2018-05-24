# https://leetcode.com/explore/interview/card/top-interview-questions-medium/108/trees-and-graphs/790/
# https://leetcode.com/problems/kth-smallest-element-in-a-bst/description/

# Kth Smallest Element in a BST
#
# Given a binary search tree, write a function kthSmallest to find the
# kth smallest element in it.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:

    # k range is [1....n]
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        return self.kth_smallest2(root, k)

    # walk the tree in-order, keep a count of node visited
    # when count == k, return item
    #
    # 91 / 91 test cases passed.
    # Status: Accepted
    # Runtime: 68 ms
    def kth_smallest2(self, root, k):
        stack = []
        x = root
        counter = 0
        while True:
            while x:
                stack.append(x)
                x = x.left
            if not stack:
                break
            x = stack.pop()
            counter += 1  # 'visiting node'
            if counter == k:
                return x.val
            x = x.right

    # 91 / 91 test cases passed.
    # Status: Accepted (on first submit, yeah!)
    # Runtime: 72 ms (beats 68.30% of py3)
    def kth_smallest(self, root, k):
        if not root:
            return

        self.set_count(root)  # annotate tree with size info
        return self.select_kth(root, k)  # select the kth element

    # walk the tree and set size attribute at each node
    def set_count(self, x):
        if not x:
            return 0
        x.size = self.set_count(x.left) + self.set_count(x.right) + 1
        return x.size

    def select_kth(self, x, k):
        """Select the kth element assume tree is annotated and k is valid"""
        if not x:
            return

        left_size = x.left.size if x.left else 0
        curr_rank = left_size + 1  # rank of current node

        if k == curr_rank:  # I am it
            return x.val
        elif k < curr_rank:  # earlier than current index, find kth in left subtree
            return self.select_kth(x.left, k)
        else:  # k > curr_idx, after current index, find k-size th in right subtree
            return self.select_kth(x.right, k - curr_rank)
