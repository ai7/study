# https://leetcode.com/explore/interview/card/top-interview-questions-medium/110/sorting-and-searching/799/
# https://leetcode.com/problems/top-k-frequent-elements/description/

# Top K Frequent Elements
#
# Given a non-empty array of integers, return the k most frequent
# elements. (time must be better than O(n log n)

import collections
import unittest


class Solution:
    
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        return self.top_freq2(nums, k)

    # Note: create counter, and sort/return first k elements
    #
    # We can create a counter manually using a dict. The trick is to
    # get a sorted view of the data. For that, we can do
    #   sorted(freq, key=freq.get)
    # basically using the value of dict as sorting key.
    # finally return the first k elements using slice.
    #
    # alternatively, we can just do collections.Counter(A) and call
    # the most_common(k) function on the resulting data.
    def top_freq2(self, A, k):

        freq = collections.defaultdict(int)
        for v in A:
            freq[v] += 1

        # get sorted view of freq in decreasing order
        freq_sorted = sorted(freq, key=freq.get, reverse=True)
        return freq_sorted[:k]


    # using python counter, kinda cheating huh.. ;)
    #
    # 20 / 20 test cases passed.
    # Status: Accepted
    # Runtime: 52 ms (beats 94.43%)
    def top_freq(self, A, k):
        # use counter to get the most common k
        result = collections.Counter(A).most_common(k)
        return list(zip(*result))[0]


class TestTopFreq(unittest.TestCase):

    def setUp(self):
        self.sol = Solution()

    def test1(self):
        v = self.sol.topKFrequent([1,1,1,2,2,3], 2)
        print(v)


if __name__ == '__main__':
    unittest.main()
