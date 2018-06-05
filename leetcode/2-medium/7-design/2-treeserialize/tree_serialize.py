# https://leetcode.com/explore/interview/card/top-interview-questions-medium/112/design/812/
# https://leetcode.com/problems/serialize-and-deserialize-binary-tree/description/

# Serialize and Deserialize Binary Tree
#
# Design an algorithm to serialize and deserialize a binary tree.

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))

import json
import unittest


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:

    # Note: preorder and write None for terminator
    #
    # Use preorder walk, and when encounter a null pointer, write a
    # corresponding terminator value in output. I used None, but I
    # also see solutions using '#' char. As long as its unique.
    #
    # Got stuck initially on memory limit exceeded during decode. Have
    # to use iterator or walk Array without creating any more data
    # structures such as Queue.

    # 48 / 48 test cases passed.
    # Status: Accepted
    # Runtime: 185 ms (beat 91.32% of py3)
    def serialize(self, root):

        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        return self.my_encode2(root)

    # encode using preorder walk
    def my_encode2(self, root):

        def encode_tree(x):
            if x:
                A.append(x.val)
                encode_tree(x.left)
                encode_tree(x.right)
            else:
                A.append(None)

        if not root:
            return ''

        A = []
        encode_tree(root)
        return json.dumps(A)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        return self.my_decode2(data)

    def my_decode2(self, data):

        def decode_tree():
            val = next(vals)  # get next value in array A
            if val is None:  # if None, don't create any node
                return
            x = TreeNode(val)  # create self
            x.left = decode_tree()  # build left subtree
            x.right = decode_tree()  # build right subtree
            return x  # return node

        if not data:
            return

        A = json.loads(data)  # decode JSON string into python objects
        if not A:
            return

        vals = iter(A)  # iter for fetching each element of A
        return decode_tree()  # build tree from array A


# my way of building a full tree, leetcode level order.
# 47 / 48 test cases passed.
# Memory Limit Exceeded
# I think it's due to the queue usage.
class CodecX:

    # encode full trees like leetcode.
    def my_encode(self, root):

        def tree_depth(x):  # returns tree depth
            if not x:
                return 0
            return max(tree_depth(x.left), tree_depth(x.right)) + 1

        # encode using heap tree order
        def encode_tree(x, i):
            if x:
                A[i] = x.val
                encode_tree(x.left, i * 2 + 1)
                encode_tree(x.right, i * 2 + 2)

        if not root:
            return ''

        depth = tree_depth(root)
        max_size = int(2 ** depth - 1)  # tree size is 2^n - 1
        A = [None] * max_size

        encode_tree(root, 0)
        res = json.dumps(A)

        return res

    def my_decode(self, data):

        def decode_tree(i):
            if i < n:  # if within range of array
                if A[i] is None:  # if no data, return null
                    return
                x = TreeNode(A[i])  # create self
                x.left = decode_tree(2 * i + 1)  # build left subtree
                x.right = decode_tree(2 * i + 2)  # build right subtree
                return x  # return node

        if not data:
            return

        A = json.loads(data)  # decode JSON string into python objects
        if not A:
            return

        n = len(A)
        return decode_tree(0)  # build tree from array A


def build_tree(A, i, n):
    """
    Build a tree from level array in leetcode

    :param A:  input array
    :param i:  start index
    :param n:  size of array
    :return: TreeNode
    """
    if i < n:

        if A[i] is None:  # return if null
            return

        x = TreeNode(A[i])
        x.left = build_tree(A, 2 * i + 1, n)
        x.right = build_tree(A, 2 * i + 2, n)

        return x


class TestCodec(unittest.TestCase):

    def setUp(self):
        self.codec = Codec()

    @unittest.skip
    def test1(self):
        root = TreeNode('abc')
        s = self.codec.serialize(root)
        root2 = self.codec.deserialize(s)

    def test2(self):
        A = [1,2,3,None,None,4,5]
        root = build_tree(A, 0, len(A))
        s = self.codec.serialize(root)
        print(s)
        root2 = self.codec.deserialize(s)


if __name__ == '__main__':
    unittest.main()
