# https://leetcode.com/explore/interview/card/top-interview-questions-medium/108/trees-and-graphs/787/
# https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/description/

# Binary Tree Zigzag Level Order Traversal
#
# Given a binary tree, return the zigzag level order traversal of its
# nodes' values. (ie, from left to right, then right to left for the
# next level and alternate between).

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

import collections


class Solution:

    # Note: create level arrays, then reverse every other array.
    #
    # Can also do this using a BFS walk of tree. The important thing
    # is to remember to process all elements in queue in each round.
    # This corresponds to one level in the tree. The trick is to
    # remember that while we process a node, we are also adding more
    # data to the queue at the same time.
    #
    # This can be easily done with a for loop with the initial size of
    # the queue before more elements are added.
    
    # 33 / 33 test cases passed.
    # Status: Accepted (on first submit, yeah)
    # Runtime: 40 ms (beats 98.04% of py3)
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        return self.zigzag_recursive(root)
        # return self.zigzag_iterative(root)

    def zigzag_recursive(self, root):

        # pre-order traversal (in-order also works but pre is probably cleaner)
        def walk(x, n):
            if x:
                if n >= len(res):
                    res.append([])
                res[n].append(x.val)
                walk(x.left, n+1)
                walk(x.right, n+1)

        res = []
        walk(root, 0)
        for i in range(len(res)):  # reverse every other row of data
            if i % 2:
                res[i].reverse()

        return res

    # iterative version, BFS using queue, from discussion
    # good way to see how to process trees in level order
    def zigzag_iterative(self, x):

        queue = collections.deque()
        queue.append(x)  # start with root node

        res, temp, flag = [], [], 1
        while queue:  # while queue is not empty

            # for each round, go through all items in queue.
            # items added to queue in this round will be processed next round.
            for i in range(len(queue)):
                node = queue.popleft()
                temp.append(node.val)
                if node.left:
                    queue.append(node.left)  # add left child for next round
                if node.right:
                    queue.append(node.right)  # add right child for next round

            res.append(temp[::flag])  # add result (normal or reverse depend on flag)

            temp = []  # get read for next round
            flag *= -1  # toggle flag for next round

        return res
