# https://leetcode.com/explore/learn/card/n-ary-tree/130/traversal/926/

# N-ary Tree Postorder Traversal
#
# Given an n-ary tree, return the postorder traversal of its nodes'
# values.


# Definition for a Node.
class Node(object):

    def __init__(self, val, children):
        self.val = val
        self.children = children


# Note: for iterative, add to front of result array
#
# For iterative, same as preorder, but add to front of result array.
#
# Another option is like binary tree post-order, but visit current
# node if no children, or last visited node is my children.

class Solution(object):

    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        return self.my_postorder(root)

    # 36 / 36 test cases passed.
    # Status: Accepted
    # Runtime: 249 ms
    def my_postorder(self, root):

        def walk(x):
            if x:
                for c in x.children:
                    walk(c)
                A.append(x.val)

        A = []
        walk(root)

        return A

    # 36 / 36 test cases passed.
    # Status: Accepted (on 1st try, yeah!)
    # Runtime: 217 ms (beats 44.68% py3)
    def my_postorder_iter(self, root):

        # same as preorder, but insert at beginning of result array.
        def walk2(x):
            s = [x]
            while s:
                x = s.pop()
                A.insert(0, x.val)
                for c in x.children:  # in order, not reverse
                    s.append(c)

        # visit current node if it has no children, or the last
        # visited node is our children
        def walk(x):
            s = [x]  # initial stack
            last = None
            while s:  # while stack is not empty
                x = s[-1]  # peek top of stack
                if not x.children or last in x.children:
                    x = s.pop()  # pop node from stack
                    A.append(x.val)  # visit(x)
                    last = x  # save last visited
                else:
                    for c in reversed(x.children):  # add all children to stack
                        s.append(c)

        A = []
        if root:
            walk2(root)

        return A
