# https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/559/
# https://leetcode.com/problems/plus-one/description/

# Plus One
#
# Given a non-empty array of digits representing a non-negative
# integer, plus one to the integer.


class Solution:

    # start from last digit, add 1 and carry over until no carry over.
    # if still carry over when end, prepend one
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        A = digits
        n = len(digits)
        carryover = 1  # hack for adding one to last digit
        for i in reversed(range(n)):
            v = A[i] + carryover
            if v < 10:
                A[i] = v  # fit, done
                carryover = 0
                break
            else:
                A[i] = v % 10
                carryover = 1
        if carryover:
            A.insert(0, 1)

        return A
