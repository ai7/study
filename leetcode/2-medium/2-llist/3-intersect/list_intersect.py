# https://leetcode.com/explore/interview/card/top-interview-questions-medium/107/linked-list/785/
# https://leetcode.com/problems/intersection-of-two-linked-lists/description/

# Intersection of Two Linked Lists
#
# Write a program to find the node at which the intersection of two
# singly linked lists begins.

import unittest


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):

    # 42 / 42 test cases passed.
    # Status: Accepted
    # Runtime: 349 ms (beats 91.75% py3, yeah)
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if not headA or not headB:  # one or both empty
            return None

        # find length of list1 and list2
        # if end element is not same, return null
        # otherwise, go back to beginning, and forward longer list
        # by their differences in length

        size_a = size_b = 1
        curr_a = headA
        curr_b = headB

        while curr_a.next:
            size_a += 1
            curr_a = curr_a.next
        # curr_a now points to last element

        while curr_b.next:
            size_b += 1
            curr_b = curr_b.next
        # curr_b now points to last element

        if curr_a != curr_b:  # if last element not same (by address)
            return None  # no intersection

        curr_a = headA if size_a >= size_b else headB  # longer list
        curr_b = headB if size_a >= size_b else headA  # shorter list

        diff = abs(size_a - size_b)
        while diff > 0:  # advance longer list by their differences
            curr_a = curr_a.next
            diff -= 1

        # now advance both until they are the same
        # this is guaranteed to succeed
        while curr_a != curr_b:
            curr_a = curr_a.next
            curr_b = curr_b.next

        return curr_a

    # accepted on first submit, yeah!


class TestIntersect(unittest.TestCase):

    def setUp(self):
        self.sol = Solution()

    def test1(self):
        common = ListNode('c1')
        common.next = ListNode('c2')
        common.next.next = ListNode('c3')

        list_a = ListNode('a1')
        list_a.next = ListNode('a2')
        list_a.next.next = common

        list_b = ListNode('b1')
        list_b.next = ListNode('b2')
        list_b.next.next = ListNode('b3')
        list_b.next.next.next = common

        list_c = ListNode('c1')
        list_c.next = ListNode('c2')
        list_c.next.next = common

        self.assertEqual(self.sol.getIntersectionNode(list_a, list_b), common)
        self.assertEqual(self.sol.getIntersectionNode(list_a, list_c), common)
        self.assertEqual(self.sol.getIntersectionNode(list_a, None), None)
        self.assertEqual(self.sol.getIntersectionNode(list_a, common), common)
        self.assertEqual(self.sol.getIntersectionNode(list_a, common.next), common.next)


if __name__ == '__main__':
    unittest.main()
