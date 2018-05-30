# https://leetcode.com/explore/interview/card/top-interview-questions-easy/93/linked-list/773/
# https://leetcode.com/problems/linked-list-cycle/description/

# Linked List Cycle
#
# Given a linked list, determine if it has a cycle in it.

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):

    # Note: use slow/fast pointer
    #
    # while fast have 2 more nodes:
    #   advance slow/fast pointer
    #   if ever same, return True
    # return False
    
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head or not head.next:
            return False

        slow = head
        fast = head

        while fast.next and fast.next.next:

            slow = slow.next  # advance slow pointer by one
            fast = fast.next.next  # advance fast by two

            if slow == fast:
                return True

        return False

        # 16 / 16 test cases passed.
        # beats 82.65% of python solution
