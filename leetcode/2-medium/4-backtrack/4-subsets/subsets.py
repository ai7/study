# https://leetcode.com/explore/interview/card/top-interview-questions-medium/109/backtracking/796/
# https://leetcode.com/problems/subsets/description/

# Subsets
#
# Given a set of distinct integers, nums, return all possible subsets
# (the power set). The solution set must not contain duplicate subsets.

import unittest


class Solution:
    
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # return self.build_powerset(nums)
        return self.build_powerset2(nums)

    # Note: start with the empty set [], for each item in input array,
    #   add to all items in previous powerset. Repeat for next item.
    #   Total 2^n items in powerset for n items (since each time it
    #   doubles).
    
    # 10 / 10 test cases passed.
    # Status: Accepted
    # Runtime: 44 ms (beats 93.67% py3)
    def build_powerset(self, A):

        res = [[]]
        for x in A:  # for each item x in nums array
            s2 = []
            for v in res:  # for each item in previous powerset
                v2 = v + [x]  # create new item by add x to it
                s2.append(v2)  # add new item to temp list
            res.extend(s2)  # add items s2 to result
        return res

        # shorter version from discussion, damn it
        # res = [[]]
        # for num in sorted(nums):
        #     res += [item + [num] for item in res]
        # return res

    # Note: powerset can also be built using bit masks. For n items,
    #   the powerset can be simply viewed as all unique sequences of
    #   selections (of size n). ie, ([no, no], [no, yes], [yes, no],
    #   [yes, yes]) where yes/no indicates whether nth item is in the
    #   list or not.
    #
    #   This means we can also build the powerset by iterate through
    #   all the numbers between 0 to 2^n (for n items), and using the
    #   number's binary representation to select whether an item is in
    #   it or not.
    def build_powerset2(self, A):

        def map_to_set(k):  # map integer k to a set of elements
            val = []  # return set
            idx = 0  # index into element list A
            while k:  # while k has bits set
                if k & 1:  # if LSB is set
                    val.append(A[idx])  # add ith element to set
                idx += 1
                k >>= 1  # shift right by 1
            return val

        n = 1 << len(A)  # calc 2^n
        res = []
        for i in range(n):
            res.append(map_to_set(i))
        return res


class TestSubsets(unittest.TestCase):

    def setUp(self):
        self.sol = Solution()

    def test1(self):
        print(self.sol.subsets([1,2,3]))
        print(self.sol.subsets([1,2,3, 4]))


if __name__ == '__main__':
    unittest.main()
