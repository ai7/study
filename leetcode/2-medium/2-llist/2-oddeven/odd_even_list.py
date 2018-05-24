# https://leetcode.com/explore/interview/card/top-interview-questions-medium/107/linked-list/784/
# https://leetcode.com/problems/odd-even-linked-list/description/

# Odd Even Linked List
#
# Given a singly linked list, group all odd nodes together followed by
# the even nodes. Please note here we are talking about the node
# number and not the value in the nodes.

import unittest


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:

    # 70 / 70 test cases passed.
    # Status: Accepted
    # Runtime: 56 ms (beat 80.26% of py3)
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        # if null, or 1 or 2 elements, done
        if not head or not head.next or not head.next.next:
            return head

        # first we split head into odd/even list
        odd = ListNode('odd')  # dummy head node
        even = ListNode('even')

        curr = head  # iterate through input list
        curr_o = odd  # point to end of odd list
        curr_e = even  # point to end of even list
        i = 1  # which node we are on

        while curr:

            next = curr.next  # save next node for next round
            curr.next = None  # disconnect from remaining of input

            if i % 2:  # node is odd
                curr_o.next = curr    # append node to odd list
                curr_o = curr_o.next  # advance odd pointer
            else:  # node is even
                curr_e.next = curr    # append node to even list
                curr_e = curr_e.next  # advance even pointer

            curr = next  # process next input
            i += 1  # increment count

        # next stitch even list to end of odd list
        curr_o.next = even.next

        return odd.next  # return beginning of odd list

    # accepted on first submit, yeah!


class TestOddEven(unittest.TestCase):

    def setUp(self):
        self.sol = Solution()

    def array_to_list(self, A):
        dummy = ListNode('dummy')
        c = dummy
        for x in A:
            c.next = ListNode(x)
            c = c.next
        return dummy.next

    def test1(self):
        head = self.array_to_list([1,2,3,4,5])
        result = self.sol.oddEvenList(head)
        print(result)


if __name__ == '__main__':
    unittest.main()
