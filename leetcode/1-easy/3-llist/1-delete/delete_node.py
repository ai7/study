# https://leetcode.com/explore/interview/card/top-interview-questions-easy/93/linked-list/553/
# https://leetcode.com/problems/delete-node-in-a-linked-list/description/

# Delete Node in a Linked List
#
# Write a function to delete a node (except the tail) in a singly
# linked list, given only access to that node.

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):

    # beats 38.43% of submissions
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        if node.next:
            node.val = node.next.val
            node.next = node.next.next