# https://leetcode.com/explore/interview/card/top-interview-questions-easy/93/linked-list/603/
# https://leetcode.com/problems/remove-nth-node-from-end-of-list/

# Remove Nth Node From End of List
#
# Given a linked list, remove the n-th node from the end of list and
# return its head.


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:

    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        return self.remove2(head, n)

    def remove1(self, head, n):
        # using slow/fast pointer
        first = head
        second = head
        prev = None

        # advance 2nd pointer n-1 steps ahead
        for i in range(n-1):
            second = second.next

        # advance both until 2nd pointer points to last node
        while second.next:
            prev = first  # save previous location
            first = first.next
            second = second.next

        # now delete node pointed by first
        if prev:  # if we have node before first
            prev.next = first.next  # just skip first
            return head
        else:  # no prev pointer (first is head)
            assert(first == head)
            return first.next

        # 208 / 208 test cases passed.
        # beats 17.3% of python3 (what happened?)
        # 2nd time beats 95.56%, hmmmm

        # official solution calls for using a dummy node before head, to
        # save on corner cases, interesting...

    # this is a bit tricky to understand, I don't quite like it, but the dummy idea is neat
    def remove2(self, head, n):

        # create dummy
        dummy = ListNode(0)
        dummy.next = head

        first = dummy  # 1st pointer (before second pointer)
        second = dummy  # second pointer (to the right of first pointer)

        # advance 2nd pointer so it is n+1 away from dummy (n away from head).
        # if we assume value n is valid, then 2nd should point to a valid node,
        # or None if exhausted the list.
        for i in range(n+1):
            second = second.next  # could be null

        # advance both until 2nd pointer is null
        # at this point, first.next point to the node we want to delete.
        while second:
            first = first.next
            second = second.next

        # now delete node pointed by first.
        # ie, first is before the node we want to delete, which could be dummy.
        # this allows us to easily delete the head if needed.
        first.next = first.next.next

        return dummy.next

        # this beats 68.32% of python3 submission
