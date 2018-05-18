# https://leetcode.com/explore/interview/card/top-interview-questions-easy/93/linked-list/771/
# https://leetcode.com/problems/merge-two-sorted-lists/description/

# Merge Two Sorted Lists
#
# Merge two sorted linked lists and return it as a new list. The new
# list should be made by splicing together the nodes of the first two
# lists.


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        dummy = ListNode(None)
        curr = dummy

        while l1 or l2:  # while have some remaining items

            if not l1:  # if list 1 is empty
                curr.next = l2  # append list 2 to end
                break
            elif not l2:  # if list 2 is empty
                curr.next = l1  # append list 1 to end
                break

            if l1.val <= l2.val:  # if list 1 is smaller
                curr.next = l1  # add item in list1 to end
                curr = curr.next  # advance end to next item
                l1 = l1.next  # advance list1
            else:
                curr.next = l2
                curr = curr.next
                l2 = l2.next

        return dummy.next

        # 208 / 208 test cases passed.
        # beats 76.63%
