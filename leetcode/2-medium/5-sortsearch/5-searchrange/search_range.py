# https://leetcode.com/explore/interview/card/top-interview-questions-medium/110/sorting-and-searching/802/
# https://leetcode.com/problems/search-for-a-range/description/

# Search for a Range
#
# Given an array of integers nums sorted in ascending order, find the
# starting and ending position of a given target value.
#
# Your algorithm's runtime complexity must be in the order of O(log n).

import bisect
import unittest


class Solution:

    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        return self.my_search2b(nums, target)

    # Note: use 2 binary search to find begin/end point.
    #
    # The binary search is not quite symmetrical.
    # For left point
    #   if A[m] >= k, drop high to mid (not mid-1)
    #   if A[m] < k, raise low to mid+1
    # For right point:
    #   if A[m] <=k, raise low to mid
    #   if A[m] > k, drop high to mid-1
    #
    # also remember to check if item found after search left point,
    # since we did not explicitly check equality, but rather >=.
    #
    # The two endpoint can also be done via bisect_left() and bisect()
    #   lo = bisect.bisect_left(A, k)
    #   hi = bisect.bisect(A, k) - 1
    # remember bisect returns where to insert item, so for right edge
    # it will point to beyond last element of array, so need -1.

    # 88 / 88 test cases passed.
    # Status: Accepted
    # Runtime: 40 ms (beat 99.63% of py3)
    def my_search2(self, A, k):

        retval = [-1, -1]
        if not A:
            return retval

        low = 0
        high = len(A)-1

        # search for left point, if any
        i, j = low, high
        while i < j:  # while they point to different
            m = (i + j) // 2
            v = A[m]
            if v >= k:
                j = m  # drop high to same as mid (since >=, not >)
            else:  # v < k
                i = m + 1  # raise low to mid (+1, since <, not <=)

        # since we didn't check for equality in loop, we need to do it afterwards
        if A[i] == k:  # i points to starting point, if match
            retval[0] = i
        else:  # k not found, done
            return [-1, -1]

        j = high  # search for right point  (i can remain the same)
        while i < j:  # while they point to different
            m = (i + j) // 2 + 1  # make mid biased to the right, brilliant!
            v = A[m]
            if v <= k:
                i = m  # raise low to same as mid (since <=, not simply <)
            else:  # v > k
                j = m - 1  # drop high to mid (-1, since >, not >=)

        # now j i point to end point
        retval[1] = i

        return retval

    # TLDR: bisect_left() find first occurrence of k,
    #       bisect()/bisect_right() finds the first pos after k.
    #   both gives you the position to insert element x to main sorted order.
    #   if we don't have bisect_right(), then can search for next char and -1
    #       hi = bisect_left(A, k+1) - 1
    def my_search2b(self, A, k):

        retval = [-1, -1]  # need this or bisect will error out.
        if not A:
            return retval

        # find the point where k could be inserted if not in A. if k
        # is in A, lo points to first k, ie, it breaks A into A[0:lo],
        # A[lo:n].
        lo = bisect.bisect_left(A, k)
        if k not in A[lo:lo+1]:  # can't do "A[lo] != k" since lo may be out of bound.
            return [-1, -1]
        hi = bisect.bisect(A, k) - 1  # -1 so point to last k

        return [lo, hi]

    # Note: use regular binary search to find the target, then expand
    # on both sides. The expand might be linear so not ideal in worst
    # case.

    # 88 / 88 test cases passed.
    # Status: Accepted
    # Runtime: 40 ms (beats 99.63% of py3)
    def my_search(self, A, k):

        # regular binary search A[low...high]
        def bsearch(low, high):
            while low <= high:
                m = (low + high) // 2
                if A[m] < k:  # m is small, search right half
                    low = m + 1
                elif A[m] > k:  # m is big, search left half
                    high = m - 1
                else:  # match, expand region to max
                    return m
            return None

        def expand(i, low, high):
            left = right = i
            while left > low and A[left - 1] == k:
                left -= 1
            while right < high and A[right + 1] == k:
                right += 1
            return [left, right]

        if not A:
            return [-1, -1]

        v = bsearch(0, len(A)-1)  # first regular binary search
        if v is None:  # if not found
            return [-1, -1]

        return expand(v, 0, len(A)-1)  # expand to both ends


class TestSearch(unittest.TestCase):

    def setUp(self):
        self.sol = Solution()

    def test1(self):
        self.assertEqual(self.sol.searchRange([2,2], 3),
                         [-1, -1])
        self.assertEqual(self.sol.searchRange([5,7,7,8,8,10], 8),
                         [3, 4])
        self.assertEqual(self.sol.searchRange([5,7,7,8,8,10], 6),
                         [-1, -1])
        self.assertEqual(self.sol.searchRange([1, 4], 4),
                         [1, 1])


if __name__ == '__main__':
    unittest.main()
