# https://leetcode.com/explore/interview/card/top-interview-questions-easy/94/trees/555/
# https://leetcode.com/problems/maximum-depth-of-binary-tree/description/

# Maximum Depth of Binary Tree
#
# Given a binary tree, find its maximum depth.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # return self.depth1(root)
        # return self.depth2(root)
        return self.depth_iter(root)

    # Note: track max depth while doing a walk of tree
    #
    # 2. preorder walk and simply return max of left/right children
    #    +1. This is simpler to get correct.
    #
    # 1. preorder walk and pass depth+1 down the chain. return max of
    #    left/right back up the chain.
    #
    # 3. iterative POST-ORDER walk, and track maximum stack length
    #    (post-order since we need current node on stack before we
    #    branch to right side).
    
    # what I came up with, passing depth down
    # 39 / 39 test cases passed.
    # beats 95.78%
    def depth1(self, root):
        if not root:
            return 0
        d = self.walk(root, 1)
        return d

    def walk(self, x, level):
        # visit
        size1 = self.walk(x.left, level + 1) if x.left else level
        size2 = self.walk(x.right, level + 1) if x.right else level
        return max(size1, size2)

    # discussion forum solution, cleaner
    # but only 77.46%? if check before recurse should be better
    def depth2(self, x):
        if not x:
            return 0
        left = self.depth2(x.left)
        right = self.depth2(x.right)
        return max(left, right) + 1  # this is where return value increments

    # only beats 77%
    def depth_iter(self, x):
        # can't do an pre or in order, post order does work.
        # the reason is in pre/in order, we pop the current node
        # before going to right side, so the stack length is off by one.
        # where as in post-order, the current node is still on the stack,
        # so when we examine the length it is correct.
        depth = 0
        s = []
        last = None
        while True:
            while x:
                s.append(x)
                depth = max(depth, len(s))
                x = x.left
            if not s:
                break
            x = s[-1]  # peek
            if x.right and x.right != last:
                x = x.right
            else:
                x = s.pop()
                # visit(x)
                last = x
                x = None
        return depth
