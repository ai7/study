# https://leetcode.com/explore/interview/card/top-interview-questions-medium/110/sorting-and-searching/801/
# https://leetcode.com/problems/find-peak-element/description/

# Find Peak Element
#
# A peak element is an element that is greater than its neighbors.
#
# Given an input array nums, where nums[i] != nums[i+1], find a peak
# element and return its index. Your solution should be in logarithmic
# complexity.

# kind of a strange problem. don't really like this.
#   on a rising edge, peak is on my right
#   on a falling edge, peak is on my left.
# it's either rising/falling (since every element is different), so
# binary search simply picks a half based on this.

class Solution:
    
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        self.find_peak2(nums)

    # linear scan.
    # as soon as we find an element that < prev, we've found a peak
    # don't need to compare element with prior
    def find_peak(self, nums):
        n = len(nums)
        for i in range(n-1):
            if nums[i] > nums[i+1]:  # as soon as next element is smaller, done.
                return i
        return n - 1  # return last element

    # use binary search. on rising slope, go right
    # on falling slope, go left. when we reach single element, done.
    #
    # 59 / 59 test cases passed.
    # Status: Accepted
    # Runtime: 36 ms (beats 99.34% py3)
    def find_peak2(self, nums):

        # recursive search
        def search(l, r):  # left and right index
            if l == r:
                return l
            m = (l + r) // 2
            if nums[m] > nums[m+1]:
                return search(l, m)
            else:  # don't need to check for equal
                return search(m+1, r)

        # iterative search
        def search2(l, r):
            while l < r:
                m = (l + r) // 2
                if nums[m] > nums[m+1]:
                    r = m
                else:
                    l = m+1
            return l

        if not nums:
            return

        return search2(0, len(nums) - 1)
