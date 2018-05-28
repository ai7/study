# https://leetcode.com/explore/interview/card/top-interview-questions-medium/110/sorting-and-searching/800/
# https://leetcode.com/problems/kth-largest-element-in-an-array/description/

# Kth Largest Element in an Array
#
# Find the kth largest element in an unsorted array. Note that it is
# the kth largest element in the sorted order, not the kth distinct
# element.

# Note: Hoare's partition scheme (that starts from both ends and merge
#       toward center) doesn't necessarily return the pivot index, it
#       simply breaks the input into 2 halfs. Therefore, we can't use
#       it to do order statistics.
#
#       We have to use Lomuto's partitioning scheme which grows both
#       section toward the right for order statistics which actually
#       puts the pivot in the correct final position. Damn, it took me
#       so long to realize this.

import random
import unittest


class Solution:

    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        return self.k_largest(nums, k)

    # 32 / 32 test cases passed.
    # Status: Accepted
    # Runtime: 3036 ms (beats 3.34% py3, what?)
    # Runtime: 64 ms (beats 48.68% py3 with shuffle input)
    def k_largest(self, nums, k):
        random.shuffle(nums)
        n = len(nums)
        return self.order_statistics(nums, 0, n-1, n-k+1)

    def swap(self, A, i, j):
        A[i], A[j] = A[j], A[i]

    # i and j points to begin/end element (not python slicing notation)
    def quick_sort(self, A, i, j):
        if i < j:  # stop if same element
            q = self.partition(A, i, j)
            self.quick_sort(A, i, q-1)
            self.quick_sort(A, q+1, j)

    # based on CLR 3rd ed, use last element as pivot, qs of A[s...e]
    # invariant:
    #   i: points to last element of left half (so at end, i+1 points to pivot)
    #   j: current element working on
    #       if <= pivot (need to extend left region with this element)
    #         increase i (so i points to right items)
    #         swap i and j (so i again points to end of left half, j points to right elements)
    #       if > pivot, just j++
    #
    # here are the 4 (possibily empty) regions:
    #   A[s...i] is <= pivot
    #   A[i+1 ... j-1] is > x
    #   A[j ... e-1] is unexplored region
    #   A[e] is pivot (which is swapped with i+1 at the end
    def partition(self, A, s, e):
        pv = A[e]               # last element as pivot
        i = s - 1               # end of <= pivot region
        for j in range(s, e):   # items to explore, from left to right-1
            if A[j] <= pv:      # if item <= pivot, need to grow left region
                i += 1          # increase left region (i points to > pv now)
                self.swap(A, i, j)
        self.swap(A, i + 1, e)  # finally put pivot at end of left region
        return i + 1            # return index to pivot

    # select kth element in A[i...j]
    # order statistics, similar to quicksort, but only recurse down
    # one half, not both. this results in O(n) instead of O(n log n)
    # time.
    def order_statistics(self, A, i, j, k):
        """select kth (1...n) elem from A[i:j)"""

        n = j - i + 1  # size of input
        if k < 1 or k > n:  # if k is out of bound
            return
        if n == 1:  # short circuit for one item
            return A[i]

        p = self.partition(A, i, j)
        rank = p - i + 1
        if k == rank:  # found, done
            return A[p]
        elif k < rank:  # search left half for same rank (ignore right half)
            return self.order_statistics(A, i, p-1, k)
        else:  # search right half
            return self.order_statistics(A, p+1, j, k-rank)  # k remains same


class TestQuickSort(unittest.TestCase):

    def setUp(self):
        self.sol = Solution()

    def test1(self):
        A = [3,2,4,5,6,1,8]
        self.sol.quick_sort(A, 0, len(A)-1)
        print(A)

    def test2(self):
        self.assertEqual(self.sol.findKthLargest([2, 1], 1), 2)
        self.assertEqual(self.sol.findKthLargest([3,2,1,5,6,4], 2), 5)
        self.assertEqual(self.sol.findKthLargest([3,2,3,1,2,4,5,5,6], 4), 4)


if __name__ == '__main__':
    unittest.main()
