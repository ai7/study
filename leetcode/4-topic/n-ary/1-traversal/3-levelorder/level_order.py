# https://leetcode.com/explore/learn/card/n-ary-tree/130/traversal/915/

# N-ary Tree Level Order Traversal
#
# Given an n-ary tree, return the level order traversal of its nodes'
# values. (ie, from left to right, level by level).

import collections

# Definition for a Node.
class Node(object):

    def __init__(self, val, children):
        self.val = val
        self.children = children


class Solution(object):

    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        return self.my_levelorder(root)

    # Note: BFS and process all element in Q each time
    #
    # use BFS, and process all element in queue each loop. Keep in
    # mind that queue will be added new element while we process, so
    # easiest to use [initial] Q size for the loop.

    # 36 / 36 test cases passed.
    # Status: Accepted (on 1st try!)
    # Runtime: 226 ms (beats 39.02% py)
    def my_levelorder(self, root):

        def walk(x):
            q = collections.deque()  # create queue
            q.append(x)
            while q:  # while queue is not empty
                t = []  # result for this level
                for i in range(len(q)):  # process all element in queue
                    x = q.popleft()
                    t.append(x.val)  # aka visit(x)
                    for c in x.children:  # add all children to queue
                        q.append(c)
                A.append(t)  # append level list to result

        A = []  # our answer array
        if root:
            walk(root)

        return A
