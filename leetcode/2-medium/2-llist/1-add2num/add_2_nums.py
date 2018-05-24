# https://leetcode.com/explore/interview/card/top-interview-questions-medium/107/linked-list/783/
# https://leetcode.com/problems/add-two-numbers/description/

# Add Two Numbers
#
# You are given two non-empty linked lists representing two
# non-negative integers. The digits are stored in reverse order and
# each of their nodes contain a single digit. Add the two numbers and
# return it as a linked list.

import unittest


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:

    # 1562 / 1562 test cases passed.
    # Status: Accepted
    # Runtime: 120 ms (beats 81.07% py3)
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        res = ListNode('dummy')
        cur = res

        carry = 0
        while l1 or l2 or carry:

            v = carry  # first add carry from last round
            if l1:
                v += l1.val
                l1 = l1.next
            if l2:
                v += l2.val
                l2 = l2.next

            if v > 9:
                carry = 1
                v %= 10
            else:
                carry = 0  # reset carry

            cur.next = ListNode(v)
            cur = cur.next

        return res.next

    # worked on first submit, yeah!


class TestAdd(unittest.TestCase):

    def setUp(self):
        self.sol = Solution()

    def test1(self):
        x = ListNode(2)
        x.next = ListNode(4)
        x.next.next = ListNode(3)
        y = ListNode(5)
        y.next = ListNode(6)
        y.next.next = ListNode(4)
        v = self.sol.addTwoNumbers(x, y)
        print(v)


if __name__ == '__main__':
    unittest.main()
