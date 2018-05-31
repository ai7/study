# https://leetcode.com/explore/interview/card/top-interview-questions-easy/96/sorting-and-searching/774/
# https://leetcode.com/problems/first-bad-version/description/

# First Bad Version
#
# You are given an API bool isBadVersion(version) which will return
# whether version is bad. Implement a function to find the first bad
# version. You should minimize the number of calls to the API.

# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool

def isBadVersion(version):
    return False


class Solution(object):
    
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        return self.search(1, n+1)

    # Note: non symmetrical binary search
    #
    # if middle is bad, check left half
    #   if none, return middle, otherwise return left search result.
    # if middle is not bad, recurse on right half
    
    # s: starting pos
    # e: ending pos+1 (easier if using python slicing notation)
    def search(self, s, e):
        n = e - s
        if n <= 0:  # nothing to search
            return 0
        elif n == 1:  # only one element
            if isBadVersion(s):
                return s
            else:
                return 0
        else:
            m = int((s + e)/2)
            if isBadVersion(m):  # middle is bad, search left half
                left = self.search(s, m)
                if not left:  # nothing in left, so m is first one
                    return m
                else:
                    return left
            else:  # middle is not bad, search right half
                return self.search(m+1, e)

    # 21 / 21 test cases passed.
    # beats 95.75% of py3
