# https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/674/
# https://leetcode.com/problems/intersection-of-two-arrays-ii/description/

# Intersection of Two Arrays II
#
# Given two arrays, write a function to compute their intersection.

import collections
import unittest


class Solution:

    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        return self.my_inter3(nums1, nums2)

    # Note: sort 2 both array, then scan both and add common elements.
    #
    # while both have remain elements
    #   if i == j: add to intersection
    #   while i < j: i++
    #   while i > j: j++
    #
    # Alternatively, build counter from A, for each in B, if in
    # counter and counter > 0, add to res and decrease corresponding
    # counter.

    def my_inter(self, nums1, nums2):

        if not nums1 or not nums2:
            return []
        nums1.sort()
        nums2.sort()

        size1 = len(nums1)
        size2 = len(nums2)
        i = 0
        j = 0
        A = []

        while i < size1 and j < size2:
            if nums1[i] == nums2[j]:
                A.append(nums1[i])
                i += 1
                j += 1

            elif nums1[i] < nums2[j]:
                while i < size1 and nums1[i] < nums2[j]:  # size check first or index error
                    i += 1

            else:  # >
                while j < size2 and nums1[i] > nums2[j]:
                    j += 1

        return A

    # using counter methods
    def my_inter2(self, A, B):
        a = collections.Counter(A)
        b = collections.Counter(B)
        return (a & b).elements()

    def my_inter3(self, A, B):
        a = collections.defaultdict(int)
        for x in A:
            a[x] += 1
        res = []
        for x in B:
            if x in a and a[x] > 0:
                res.append(x)
                a[x] -= 1
        return res


class TestIntersection(unittest.TestCase):

    def setUp(self):
        self.sol = Solution()

    def test1(self):
        A = [1, 2, 2, 1]
        B = [2, 2]
        self.assertEqual(self.sol.intersect(A, B),
                         [2, 2])

    def test2(self):
        A = [1, 2]
        B = [1, 1]
        self.assertEqual(self.sol.intersect(A, B),
                         [1])


if __name__ == '__main__':
    unittest.main()
