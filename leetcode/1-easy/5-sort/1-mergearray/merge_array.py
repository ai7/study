# https://leetcode.com/explore/interview/card/top-interview-questions-easy/96/sorting-and-searching/587/
# https://leetcode.com/problems/merge-sorted-array/description/

# Merge Sorted Array
#
# Given two sorted integer arrays nums1 and nums2, merge nums2 into
# nums1 as one sorted array.


class Solution:

    # Note: copy end of A or B directly to target location
    #
    # the trick is that we know the target location based on the
    # current n and m length. So simply examine current element of A
    # or B (from end) and copy one of them directly to target
    # location.
    #
    # Don't forget to copy remaining B items if any at the end.

    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        return self.my_merge2(nums1, m, nums2, n)

    # simpler solution from discussion
    def my_merge2(self, A, m, B, n):
        while m > 0 and n > 0:
            if A[m - 1] >= B[n - 1]:  # if end of A is bigger
                A[m + n - 1] = A[m - 1]  # copy end of A to target location
                m -= 1
            else:  # if end of B is bigger
                A[m + n - 1] = B[n - 1]  # copy end of B to target location
                n -= 1
        if n > 0:  # if any remaining item in B
            A[:n] = B[:n]  # copy to final location

    # Note: copy larger of A1 or A2 from the end
    #
    # - first some special checks
    #   no input, 2nd array is empty
    #   if 1st empty, just copy 2nd, done
    #
    # - copy larger of A1/A2 elements to target until one array is
    #   exhausted.
    # - if 2nd array exhausted, done
    # - if 1st array exhausted, copy remain 2nd array items

    # my solution, kinda complicated
    def my_merge(self, nums1, m, nums2, n):

        if not nums1 and not nums2:  # if no input
            return
        if n < 1:  # if 2nd array is empty, done
            return
        size = m + n
        if size < 1:  # shouldn't happen but
            return

        if m < 1:  # if first array is empty, just copy 2nd array
            for i in range(n):
                nums1[i] = nums2[i]
            return

        # copy array1 or array2 from end until one is exhausted
        i = m-1  # end if data in array 1
        j = n-1  # end of data in array 2
        k = size - 1  # target index
        while i >= 0 and j >= 0:  # while we have something to do
            if nums1[i] <= nums2[j]:  # if same, get from 2nd array
                nums1[k] = nums2[j]
                j -= 1
            else:
                nums1[k] = nums1[i]
                i -= 1
            k -= 1

        # either i or j have been exhausted
        # if j exhausted, we are done
        # if i exhausted, we need to copy remaining j items
        while j >= 0:
            nums1[k] = nums2[j]
            j -= 1
            k -= 1

        # 59 / 59 test cases passed.
        # beats 97.69% of py3
