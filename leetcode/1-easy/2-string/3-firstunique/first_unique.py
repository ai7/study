# https://leetcode.com/explore/interview/card/top-interview-questions-easy/127/strings/881/
# https://leetcode.com/problems/first-unique-character-in-a-string/description/

# First Unique Character in a String
#
# Given a string, find the first non-repeating character in it and
# return it's index. If it doesn't exist, return -1.

import collections


class Solution:

    # Note: build histogram, scan string and return first char with cnt==1.
    #
    # The problem is to return the first char in string that have only
    # one occurance in the whole string. (not returning b in
    # 'aaaaab...'). So to solve this we need 2 pass. One to build
    # histogram, and 2nd pass iterate through the string and return
    # the first char having counter value of 1.
    #
    # easiest way to build histogram is
    #   collections.Counter(s)
    
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        return self.unique3(s)

    # manually using array as histogram
    def unique1(self, s):

        if not s:
            return -1
        n = len(s)

        hist = [0] * 32  # input only lower case chars
        base = ord('a')

        # first build histogram
        for i in range(n):
            v = s[i]
            idx = ord(v) - base
            hist[idx] += 1

        for i in range(n):
            v = s[i]
            idx = ord(v) - base
            if hist[idx] == 1:
                return i

        return -1

        # 104 / 104 test cases passed.
        # beats 23% only?

    # manually using dist as histogram
    def unique2(self, s):

        hist = {}
        for v in s:
            if v not in hist:
                hist[v] = 1
            else:
                hist[v] += 1

        for i in range(len(s)):
            if hist[s[i]] == 1:
                return i

        return -1

        # beats 56%, still?

    # using collections.Counter
    def unique3(self, s):

        hist = collections.Counter(s)
        for i in range(len(s)):
            if hist[s[i]] == 1:
                return i

        return -1

        # beats 71%, wow
