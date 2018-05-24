# some helper functions


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
