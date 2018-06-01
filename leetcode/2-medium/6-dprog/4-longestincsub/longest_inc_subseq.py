# https://leetcode.com/explore/interview/card/top-interview-questions-medium/111/dynamic-programming/810/
# https://leetcode.com/problems/longest-increasing-subsequence/solution/

# Longest Increasing Subsequence
#
# Given an unsorted array of integers, find the length of longest increasing subsequence.

import bisect


class Solution:

    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        if len(nums) < 2:
            return 1
        return self.lis2(nums)

    # Note: replace in tail if smaller, or extend tail if larger.
    #
    # hard to understand algorithm from discussion, god damn it.
    # simplified further based on py posts
    #
    # 24 / 24 test cases passed.
    # Status: Accepted
    # Runtime: 36 ms (beats 100% of py3, damn)
    def lis2(self, A):
        # tail[i] contains smallest tail of all increase sub seq with
        # length i+1.
        tails = []  # initially empty
        for x in A:  # for each value in array
            pos = bisect.bisect_left(tails, x)  # find pos no larger than x
            if pos == len(tails):  # if end of array, just append
                tails.append(x)
            else:  # otherwise update element value to x
                tails[pos] = x
        return len(tails)

    def binary_search(self, A, low, high, x):
        """Find pos in A[low...high] that matches x

        if x is not found, return pos that is left of where x should be,
        same as bisect.bisect_left()
        """
        while low <= high:  # <= (not <) since need to search size 1 seq
            m = low + (high-low) // 2
            if A[m] == x:  # if match, done
                return m
            elif A[m] < x:  # smaller, search right half
                low = m + 1
            else:  # A[m] > x, larger, search left half
                high = m - 1
        return low

    # Note: dp[n] tracks LIS ending at this position.
    #
    # O(n^2) solution, based on youtube video and solution.
    #
    # fill dp array with 1 (shortest LIS). for each position starting
    # from 2nd item, scan all previous loc, and +1 for any index that
    # is smaller than current, take max of those and assign to dp[n].
    # repeat for next pos.
    #
    # Essentially for each position, try to extend any previous LIS
    # and increment its length by one. pick the highest and use it
    # here.
    #
    # initialize an array (size n) with 1 (smallest subseq is 1)
    # for each element in 2nd position to last  (a[i])
    #   compare A[i] with each of A[0:i]  (a[j])
    #     if a[i] is bigger than a[j]
    #       take dp[j] and +1, track a max of these
    #   dp[i] = max of above value
    
    # 21 / 24 test cases passed.
    # time limit exceeded, hehe.
    def lis1(self, A):
        """Assume more than 1 elements"""
        n = len(A)
        dp = [1] * n
        longest = 1
        for i in range(1, n):  # for each pos from [1...n)
            maxval = 0
            for j in range(0, i):  # for each previous location
                if A[j] < A[i]:  # if current is larger than it
                    maxval = max(maxval, dp[j])  # update local max
            dp[i] = maxval + 1  # set dp value now
            longest = max(longest, dp[i])  # update longest if needed

        return longest
