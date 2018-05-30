# https://leetcode.com/explore/interview/card/top-interview-questions-easy/127/strings/879/
# https://leetcode.com/problems/reverse-string/description/

# Reverse String
#
# Write a function that takes a string as input and returns the string
# reversed.


class Solution(object):

    # Note: classic question. swap i/j from both end until meet.
    #
    # For python, slicing backward is a nice trick.
    
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        return s[::-1]
    
        # beats 85.25 percent
