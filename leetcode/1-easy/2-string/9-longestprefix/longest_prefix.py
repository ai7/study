# https://leetcode.com/explore/interview/card/top-interview-questions-easy/127/strings/887/
# https://leetcode.com/problems/longest-common-prefix/description/

# Longest Common Prefix
#
# Write a function to find the longest common prefix string amongst an array of strings.

import unittest


class Solution:
    
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        s = []
        for A in zip(*strs):  # process input array in parallel, fetch first chars as list
            x = set(A)  # convert list to set, should have length 1 if same char
            if len(x) == 1:
                s.append(A[0])
            else:
                break

        return ''.join(s)

        # 118 / 118 test cases passed.
        # beats 100% of python3 submission


class TestPrefix(unittest.TestCase):

    def setUp(self):
        self.sol = Solution()

    def test1(self):
        A = ["flower","flow","flight"]
        self.assertEqual(self.sol.longestCommonPrefix(A),
                         'fl')


if __name__ == '__main__':
    unittest.main()
