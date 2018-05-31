# https://leetcode.com/explore/interview/card/top-interview-questions-easy/94/trees/627/
# https://leetcode.com/problems/symmetric-tree/description/

# Symmetric Tree
#
# Given a binary tree, check whether it is a mirror of itself (ie,
# symmetric around its center).

import collections
import unittest


# Definition for a binary tree node.
class TreeNode:

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    @staticmethod
    def build_tree(A, i, n):
        """Build a tree from level array in leetcode"""
        if i < n:
            if A[i] is None:  # return if null
                return
            x = TreeNode(A[i])
            x.left = TreeNode.build_tree(A, 2 * i + 1, n)
            x.right = TreeNode.build_tree(A, 2 * i + 2, n)
            return x


class Solution:

    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        # return self.is_mirror(root, root)
        return self.is_mirror_iter(root)

    # Note: recursive solution, simple, but tricky to come up with.
    #
    # this helper function takes 2 node as input
    # - check null status matches
    # - check .val matches
    # - recursively check t1.left == t2.right, and t1.right == t2.left
    #
    # and finally start with is_mirror(root, root), a nice trick.

    def is_mirror(self, t1, t2):

        if not t1 and not t2:  # if both empty
            return True
        if not t1 or not t2:  # if only one is empty
            return False

        return t1.val == t2.val and \
            self.is_mirror(t1.left, t2.right) and \
            self.is_mirror(t1.right, t2.left)

        # 193 / 193 test cases passed.
        # beats 97.77% of py3 submissions

    # Note: iterative solution, add/pop 2 things at a time in Q.
    #
    # start with [root, root] on stack.
    # each time, pop 2 items off stack.
    #   compare item null status and value, same as recursive version.
    #   then add 1.left and 2.right as a set, and
    #            1.right and 2.left as another set
    def is_mirror_iter(self, root):
        q = collections.deque()
        q.append(root)
        q.append(root)
        while q:
            t1 = q.popleft()  # pop 2 elements from queue
            t2 = q.popleft()
            if not t1 and not t2:  # this is how we stop on null node
                continue
            if not t1 or not t2:
                return False
            if t1.val != t2.val:
                return False
            q.append(t1.left)  # add both sets (left, right) (right, left)
            q.append(t2.right)
            q.append(t1.right)
            q.append(t2.left)
        return True

        # 193 / 193 test cases passed.
        # beats 97.77% of py3 submissions (strange, same as recursive)


# this solution, which builds an in-order walk, and checks for palindrome,
# does not work. there are cases where it actually fails. I think it has
# to do with empty branches (that are not reflected in the result list).
# since I only write None if one child is not empty.
# keeping it here as amusement.
class SolutionX:

    def is_symmetric_bad(self, root):
        if not root:
            return True
        A = []
        self.walk(root, A)
        return A == A[::-1]

    # in order
    def walk(self, x, A):

        # if leaf node, just append val
        if not x.left and not x.right:
            A.append(x.val)
            return

        # not leaf node
        if x.left:
            self.walk(x.left, A)
        else:
            A.append(None)

        A.append(x.val)

        if x.right:
            self.walk(x.right, A)
        else:
            A.append(None)


class TestSymmetric(unittest.TestCase):

    def setUp(self):
        self.sol = Solution()

    # [1,2,3,3,null,2,null]
    def test1(self):
        data = [1, 2, 3, 3, None, 2, None]
        tree = TreeNode.build_tree(data, 0, len(data))
        self.assertFalse(self.sol.isSymmetric(tree))

    def test2(self):
        data = [5, 4, 1, None, 1, None, 4, 2, None, 2, None]
        tree = TreeNode.build_tree(data, 0, len(data))
        self.assertFalse(self.sol.isSymmetric(tree))


if __name__ == '__main__':
    unittest.main()
