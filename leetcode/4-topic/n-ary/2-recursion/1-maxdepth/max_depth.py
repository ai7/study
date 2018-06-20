# https://leetcode.com/explore/learn/card/n-ary-tree/131/recursion/919/

# Maximum Depth of N-ary Tree
#
# Given a n-ary tree, find its maximum depth.


"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""


class Solution(object):
    
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """
        return self.my_depth(root)

    # Note: return max of children plus one

    def my_depth(self, root):

        # 36 / 36 test cases passed.
        # Status: Accepted
        # Runtime: 182 ms
        def depth(x):
            if not x:
                return 0
            if not x.children:
                return 1
            return 1 + max([depth(d) for d in x.children])

        if not root:
            return 0
        return depth(root)
