# https://leetcode.com/explore/interview/card/top-interview-questions-medium/103/array-and-strings/776/
# https://leetcode.com/problems/3sum/description/

# 3Sum
#
# Given an array nums of n integers, are there elements a, b, c in
# nums such that a + b + c = 0? Find all unique triplets in the array
# which gives the sum of zero.

import collections
import unittest


class Solution:
    
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        return self.three_sum3(nums)

    # Note: for each num, do 2sum (from left/right) for remaining data.
    #
    # - sort A first
    # - for each starting position i, do 2sum 2 pointer (left/right)
    #   search from i+1 to end of array.
    # - since array is sorted, we can do the 2sum in O(n) time by
    #   scanning left/right to the center until they meet.
    #     left++ if 3sum is < target
    #     right-- if 3sum is > target
    #     if equal, add result, and skip any left/right that are the same.
    # - no need to use a set/etc to track the return result, if we can
    #   ensure we only add unique data.
    #
    # Don't need to search prior to i, since any found match would've
    # been found earlier (when i was at that position).

    # based on a guy's java solution, damn it damn it damn it!
    # more optimized/easier to read based on a python guy's post.
    #
    # don't need to create a set/hashtable, just use 2 pointer 2sum search
    # 313 / 313 test cases passed.
    # Status: Accepted
    # Runtime: 1076 ms (beats 40.01% of py3)
    # Runtime: 1004 ms (beats 48.81% of py3)
    def three_sum3(self, A):
        n = len(A)
        A.sort()
        res = []
        for i in range(0, n-2):  # i: starting pos of all 3-tuple
            if i > 0 and A[i] == A[i-1]:  # skip if same as last one
                continue
            l, r = i+1, n-1  # left/right pointer (all after i)
            while l < r:
                s = A[i] + A[l] + A[r]  # calculate current sum of 3 items
                if s < 0:  # if less, advance left pointer (i remains unchanged)
                    l += 1
                elif s > 0:  # if more, advance right pointer (i remains unchanged)
                    r -= 1
                else:  # equals target 0, add tuplet, and skip left/right that are the same
                    res.append([A[i], A[l], A[r]])  # sorted so unique
                    while l < r and A[l] == A[l+1]:  # advance left if same
                        l += 1
                    while l < r and A[r] == A[r-1]:  # decrease right if same
                        r -= 1
                    l += 1  # advance left/right pointer for next round
                    r -= 1
        return res


# what I came up with... for each i, 2sum remaining items
class SolutionMe:

    # still time limited exceeded??
    def three_sum2(self, A):

        if not A:  # if no input
            return []
        n = len(A)
        if n < 3:  # or less than 3 elements
            return []
        retval = set()

        # A.sort()  # we sort A first
        counter = collections.Counter(A)  # build freq chart

        # create new array
        B = []
        for c in counter:
            for i in range(counter[c]):
                B.append(c)

        for i in range(n):
            for j in range(i+1, n):
                a = B[i]
                b = B[j]
                counter[a] -= 1
                counter[b] -= 1
                x = a + b
                y = 0 - x
                if y in counter and counter[y] > 0:
                    retval.add(tuple(sorted([a, b, y])))
                counter[a] += 1
                counter[b] += 1
        return list(retval)

    # 123 / 313 test cases passed, wrong answer, hmmm
    # 311 / 313 test cases passed, time limit exceeded, hehe
    # still time limit exceeded after not creating sets each time
    def three_sum1(self, A):

        if not A:  # if no input
            return []
        n = len(A)
        if n < 3:  # or less than 3 elements
            return []

        A.sort()  # we sort A first
        counter = collections.Counter(A)  # build freq chart

        retval = set()
        last = None

        # for each element, reduce to 2 sum
        for i in range(n):
            v = A[i]
            if v == last:  # skip if same as last one looked at
                continue
            last = v
            # rest = A[:i] + A[i+1:]  # array without this element
            rest = A[i+1:]  # rest of array, no need to look prior
            counter[v] -= 1  # remove v from frequency table
            pairs = self.two_sum(rest, 0-v, counter)
            for p in pairs:
                retval.add(tuple(sorted([v, p[0], p[1]])))
            counter[v] += 1  # restore v in frequency table

        return list(retval)

    def two_sum(self, A, target, counter):
        """Return ALL the tuple that sums to target"""
        if not A or len(A) < 2:
            return []

        retval = []
        for x in A:  # for each value in A
            counter[x] -= 1  # remove x from counter temporarily
            v = target - x  # calc the complement
            if v in counter and counter[v] > 0:  # if have complement
                retval.append([x, v])  # add tuple
            counter[x] += 1  # remove x from counter temporarily

        return retval


class Test3Sum(unittest.TestCase):

    def setUp(self):
        self.sol = Solution()

    def test1(self):
        A = [-1, 0, 1, 2, -1, -4]
        v = self.sol.threeSum(A)
        print(v)

    def test2(self):
        A = [-4,-2,-2,-2,0,1,2,2,2,3,3,4,4,6,6]
        v = self.sol.threeSum(A)
        print(v)


if __name__ == '__main__':
    unittest.main()
