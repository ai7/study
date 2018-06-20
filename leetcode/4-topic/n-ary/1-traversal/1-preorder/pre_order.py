# https://leetcode.com/explore/learn/card/n-ary-tree/130/traversal/925/

# N-ary Tree Preorder Traversal
#
# Given an n-ary tree, return the preorder traversal of its nodes'
# values.


# Definition for a Node.
class Node(object):

    def __init__(self, val, children):
        self.val = val
        self.children = children


# Note: for iterative, simply add all children to stack
#
# in reverse order so order matches leetcode check. Technically this
# is not required as the children can be processed in any order.

class Solution(object):

    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        return self.my_preorder(root)

    # recursive, simple
    def my_preorder(self, root):

        def walk(x):
            if x:
                A.append(x.val)
                for c in x.children:
                    walk(c)

        A = []
        walk(root)

        return A

    # 36 / 36 test cases passed.
    # Status: Accepted
    # Runtime: 217 ms
    def my_preorder_iter(self, root):

        # add node, then process children in reverse (reverse not
        # technically required but needed so our answer matches
        # leetcode check).
        def walk(x):
            s = [x]  # initial stack
            while s:  # while stack is not empty
                x = s.pop()
                A.append(x.val)  # visit(x)
                for c in reversed(x.children):  # add all children to stack
                    s.append(c)

        A = []
        if root:
            walk(root)

        return A
