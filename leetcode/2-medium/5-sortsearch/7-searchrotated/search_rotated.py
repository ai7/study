# https://leetcode.com/explore/interview/card/top-interview-questions-medium/110/sorting-and-searching/804/

# Search in Rotated Sorted Array
#
# Suppose an array sorted in ascending order is rotated at some pivot
# unknown to you beforehand. You are given a target value to search.
# If found in the array return its index, otherwise return -1.
#
# You may assume no duplicate exists in the array. Your algorithm's
# runtime complexity must be in the order of O(log n).

import unittest


class Solution:
    
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        return self.my_search2(nums, target)

    # Note: when array is rotated, we have a good half, and a bad
    #   half. Modified binary search checks if k is in range of the
    #   good half, if so, search the good half, otherwise, search the
    #   other half.

    # same as 1, but no special/regular search.
    # 196 / 196 test cases passed.
    # Status: Accepted
    # Runtime: 44 ms (beats 85.02% of py3)
    def my_search2(self, A, k):

        # use good half to determine which half go to
        def bsearch(i, j):
            left_ok = right_ok = True
            while i <= j:
                m = (i + j) // 2  # middle, left bias
                v = A[m]
                if k == v:  # if found, done
                    return m
                # check which side is bad
                if A[i] > v:
                    left_ok = False
                if A[j] < v:
                    right_ok = False
                assert left_ok or right_ok

                if left_ok:  # left side ok
                    if A[i] <= k <= v:  # k within left bound
                        return bsearch(i, m-1)
                    else:  # search other half
                        return bsearch(m+1, j)

                if right_ok:  # right side ok
                    if v <= k <= A[j]:  # k within right bound
                        return bsearch(m+1, j)
                    else:  # search other half
                        return bsearch(i, m-1)
            return -1

        if not A:
            return -1
        return bsearch(0, len(A)-1)

    #   probably the same bs would work (without good/special), but I
    #   had 2 separate version to simplify the thinking a bit.

    # figured this one out myself, hehe. ;)
    # 196 / 196 test cases passed.
    # Status: Accepted
    # Runtime: 44 ms (beats 85.02% of py3)
    def my_search(self, A, k):

        def bs_regular(i, j):
            """Regular binary search, return index or -1 if not found"""
            while i <= j:
                m = (i + j) // 2  # biased left
                if A[m] == k:  # found
                    return m
                elif A[m] < k:  # in right half
                    i = m + 1
                else:  # > k, in left half
                    j = m - 1
            return -1

        # use good half to determine which half go to
        def bs_special(i, j):
            left_ok = right_ok = True
            while i <= j:
                m = (i + j) // 2  # biased left
                v = A[m]
                if k == v:  # if found, done
                    return m
                # check which side is bad
                if A[i] > v:
                    left_ok = False
                if A[j] < v:
                    right_ok = False
                assert left_ok or right_ok

                if left_ok:  # left side ok
                    if A[i] <= k <= v:  # k within left bound
                        return bs_regular(i, m-1)
                    else:  # search other half
                        return bs_special(m+1, j)

                if right_ok:  # right side ok
                    if v <= k <= A[j]:  # k within right bound
                        return bs_regular(m+1, j)
                    else:  # search other half
                        return bs_special(i, m-1)
            return -1

        if not A:
            return -1
        return bs_special(0, len(A)-1)


class TestSearch(unittest.TestCase):

    def setUp(self):
        self.sol = Solution()

    def test1(self):
        self.assertEqual(self.sol.search([4,5,6,7,0,1,2], 0),
                         4)
        self.assertEqual(self.sol.search([4,5,6,7,0,1,2], 3),
                         -1)


if __name__ == '__main__':
    unittest.main()
