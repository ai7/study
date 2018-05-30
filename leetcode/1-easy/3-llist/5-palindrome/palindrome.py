# https://leetcode.com/explore/interview/card/top-interview-questions-easy/93/linked-list/772/
# https://leetcode.com/problems/palindrome-linked-list/description/

# Palindrome Linked List
#
# Given a singly linked list, determine if it is a palindrome.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:

    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        return self.check_via_stack(head)

    # Note: check via stack
    #
    # for each item, push onto stack
    # compare from head each element of stack
    
    def check_via_stack(self, head):

        if not head or not head.next:
            return True

        s = []  # stack
        c = head

        # push list into stack
        while c:
            s.append(c)
            c = c.next

        c = head
        while c:
            v = s.pop()
            if c.val != v.val:
                return False
            c = c.next

        return True

        # 26 / 26 test cases passed.
        # beats 100% of python3 submissions
