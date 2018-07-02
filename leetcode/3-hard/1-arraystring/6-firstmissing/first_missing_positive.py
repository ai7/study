# https://leetcode.com/explore/interview/card/top-interview-questions-hard/116/array-and-strings/832/
# https://leetcode.com/problems/first-missing-positive/description/

# First Missing Positive
#
# Given an unsorted integer array, find the smallest missing positive
# integer.


class Solution:

    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return self.my_missing(nums)

    # Note: 1st pass, put v in A[v], 2nd pass, find first anomaly.
    #
    # kind of like counting sort, but we only care about number from
    # [1..n] (leave the other number alone). On the 2nd pass, find the
    # first index with number that's out of place. This is our first
    # missing number (since number within our range should all be in
    # the correct index position).

    # for n elements, the missing number must be in [1 to n+1].
    #
    # ie, if I have 100 elements, the largest possible missing first
    # number will be between 1-101.

    # 157 / 157 test cases passed.
    # Status: Accepted
    # Runtime: 40 ms (beats 95.01% py3)
    def my_missing(self, A):

        def swap(i, j):
            A[i], A[j] = A[j], A[i]

        n = len(A)

        for i in range(n):  # for each index

            # while A[i] is within my consider range, and not in its
            # final position, swap with element in its final position
            while 0 < A[i] <= n and A[A[i]-1] != A[i]:
                swap(i, A[i] - 1)

            # don't care about negative number?

        # return first index that is not 'right'.
        for i in range(n):
            if A[i] != i+1:
                return i+1

        # looked at whole array (which must be all within care range),
        # answer must be n+1, the next higher number.
        return n+1
