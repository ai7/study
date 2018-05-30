# https://leetcode.com/explore/interview/card/top-interview-questions-easy/127/strings/885/
# https://leetcode.com/problems/implement-strstr/description/

# Implement strStr()
#
# Return the index of the first occurrence of needle in haystack, or
# -1 if needle is not part of haystack.


class Solution:

    # Note: simply check each possible substring.
    #
    # Some optimization with no needle or no haystack, or needle >
    # haystack. and can check substr with python slicing and compare
    # such as: haystack[i:i+len] == needle
    
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if not needle:  # no search string, same as c's strstr()
            return 0

        if not haystack:  # no haystack but have needle, -1
            return -1

        len1 = len(haystack)
        len2 = len(needle)

        if len2 > len1:  # if needle longer than haystack
            return -1

        # obviously this is cheating ;)
        # return haystack.find(needle)

        for i in range(0, len1-len2+1):
            if haystack[i:i+len2] == needle:
                return i

        return -1

        # 74 / 74 test cases passed.
        # beats 90% of python
