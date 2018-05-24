# https://leetcode.com/explore/interview/card/top-interview-questions-medium/103/array-and-strings/778/
# https://leetcode.com/problems/group-anagrams/description/

# Group Anagrams
#
# Given an array of strings, group anagrams together.

import collections


class Solution:

    # 101 / 101 test cases passed.
    # Status: Accepted
    # Runtime: 152 ms (beat 44.48% py3)
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        ana = collections.defaultdict(list)
        for s in strs:
            s2 = ''.join(sorted(s))  # sort string
            ana[s2].append(s)
        return list(ana.values())
