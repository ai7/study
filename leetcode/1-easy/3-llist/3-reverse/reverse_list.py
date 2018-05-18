# https://leetcode.com/explore/interview/card/top-interview-questions-easy/93/linked-list/560/
# https://leetcode.com/problems/reverse-linked-list/description/

# Reverse Linked List
#
# Reverse a singly linked list.


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:

    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        return self.reverse_recursive(head)

    def reverse_recursive(self, head):

        # if not head:  # if nothing, return nothing
        #     return
        # if not head.next:  # if one element, return
        #     return head

        if not head or not head.next:  # simpler version, phew
            return head

        # reverse remaining of the list
        second = head.next  # upon reverse, this will be LAST ELEMENT!
        first = self.reverse_recursive(second)

        # finally append head to end of list (which is second)
        second.next = head
        head.next = None

        return first

        # beats 68.56% of python3 submission

        # alternatively, can simply do
        # first = self.reverse_recursive(head.next)  # reverse remaining items
        # head.next.next = head  # head.next points to last element, phew!
        # head.next = None

    def reverse_iter(self, head):

        if not head or not head.next:
            return head

        # basically:
        # set curr->next to curr-> prev

        curr = head
        prev = None
        while curr:
            next = curr.next  # save next node
            curr.next = prev  # set next to previous node, if any
            prev = curr
            curr = next

        return prev

        # beats 99.86% of submission!
