# https://leetcode.com/explore/interview/card/top-interview-questions-easy/127/strings/882/
# https://leetcode.com/problems/valid-anagram/description/

# Valid Anagram
#
# Given two strings s and t , write a function to determine if t is an
# anagram of s.

import collections


class Solution:

    # Note: check sorted version or compare histogram.
    #
    # If anagram, then string sorted will be the same. Histogram if
    # char counts will also be the same.
    
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # return self.via_sort(s, t)
        return self.via_hist(s, t)

    def via_sort(self, s, t):

        if len(s) != len(t):
            return False

        a = ''.join(sorted(s))
        b = ''.join(sorted(t))

        return a == b

        # beats 52%

    def via_hist(self, s, t):

        h1 = collections.Counter(s)
        h2 = collections.Counter(t)
        return h1 == h2

        # beats 98.98%
