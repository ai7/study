# https://leetcode.com/explore/interview/card/top-interview-questions-medium/108/trees-and-graphs/788/
# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/description/

# Construct Binary Tree from Preorder and Inorder Traversal
#
# Given preorder and inorder traversal of a tree, construct the binary
# tree.

import unittest


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# Note: The tree is a binary tree, not a binary-search-tree (BST), so
#       the nodes are not sorted in some particular order.
#
# The inorder array gives us information in the ordering of the nodes
# (which is before/after which in the tree), but it doesn't give us
# information on which one is the parent of which one.
#
# The preorder lists parents before children, but doesn't tell us
# whether the children is left/right, etc.


class Solution:

    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        # return self.build1(preorder, inorder)
        return self.build2(preorder, inorder)

    # Note: use preorder for Nodes, in-order for recursion.
    #
    # The idea is to go through elements in the preorder list, and use
    # its position in the inorder list (and the remaining left/right
    # sublist) for the recursion step for left/right subtree.
    #
    # since we process left subtree first, the order we process those
    # items should corresponds exactly to the order they appear in the
    # preorder list (as we pop them off the list). So when we get to
    # the right subtree, the top of preorder should be the root of
    # right subtree.

    # short and concise solution from discussion, hmmmm
    # slower, beats 24.86% py3 (but perhaps easier to understand)
    def build2(self, preorder, inorder):
        if inorder:  # preorder should empty first
            v = preorder.pop(0)  # pop first element in preorder
            i = inorder.index(v)  # find item in inorder list
            x = TreeNode(v)  # create node, obviously ;)
            x.left = self.build2(preorder, inorder[:i])  # build left subtree
            x.right = self.build2(preorder, inorder[i+1:])  # build right subtree
            return x

    # 203 / 203 test cases passed.
    # Status: Accepted (on first submit, yeah!)
    # Runtime: 212 ms (beats 55.64% of py3)
    def build1(self, preorder, inorder):
        root, cnt = self.build_tree(preorder, inorder, 0)
        return root

    # precess each item in preorder list (from index p_idx), use the
    # inorder as reference to figure out what the remaining left and
    # right half are, and recursively process those.
    #
    # if the current item in preorder is not in my inorder list, this
    # means the item is in the other subtree of my parent, and should
    # be picked up by them, so we simply return here.
    #
    # code could be shorter if I simply remove item from preorder
    # list, so don't need to pass idx and calculate idx.
    def build_tree(self, preorder, inorder, p_idx):
        """Return tuple (node, count)"""

        if not inorder:  # if nothing left to process
            return None, 0
        if p_idx >= len(preorder):  # if exhausted preorder, also done
            return None, 0

        v = preorder[p_idx]  # get next item from preorder list
        if v not in inorder:  # if not in in-order list
            return None, 0  # then done (must be in other half)

        x = TreeNode(v)  # create current node
        cnt = 1  # processed one item in preorder

        i = inorder.index(v)  # locate item in in-order list
        left = inorder[:i]  # remaining item on left side of me
        right = inorder[i+1:]  # remaining item on right side of me

        if left:
            x.left, item_cnt = self.build_tree(preorder, left, p_idx+cnt)
            cnt += item_cnt  # include items from left tree
        if right:
            x.right, item_cnt = self.build_tree(preorder, right, p_idx+cnt)
            cnt += item_cnt  # include items from left tree

        return x, cnt  # return node and number of items in preorder processed


class TestBuildTree(unittest.TestCase):

    def setUp(self):
        self.sol = Solution()

    def test1(self):
        pre = [3,9,20,15,7]
        ino = [9,3,15,20,7]
        root = self.sol.buildTree(pre, ino)
        print(root)


if __name__ == '__main__':
    unittest.main()
