# https://leetcode.com/problems/inorder-successor-in-bst/

# Does node have link to parent?


class Solution:

    def successor(self, node):
        return self.my_successor(node)

    def my_successor(self, node):

        def tree_min(x):
            while x.left:
                x = x.left
            return x

        if node.right:  # if have right subtree
            return tree_min(node.right)  # return the min of that tree

        # go up until we hit a left edge
        y = node.parent
        while y and node == y.right:
            node = y
            y = y.parent

        return y
