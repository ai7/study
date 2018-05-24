# https://leetcode.com/explore/interview/card/top-interview-questions-medium/103/array-and-strings/780/
# https://leetcode.com/problems/longest-palindromic-substring/description/

# Longest Palindromic Substring
#
# Given a string s, find the longest palindromic substring in s. You
# may assume that the maximum length of s is 1000.

import collections
import unittest


class Solution:

    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s or len(s) < 2:
            return s
        return self.longest2(s)

    # came up with this after looking at the hints.. expand around center
    # for each pos, there are 2 cases: (i, i), and (i, i+1). (even/odd length palindrome)
    #
    # 94 / 94 test cases passed.
    # Status: Accepted
    # Runtime: 1004 ms (beats 63.56% py3)
    def longest2(self, s):
        # ok, new idea, for each pos, 'grow' as big as we can
        n = len(s)
        max_so_far = ''
        for i in range(0, n-1):
            # 2 cases, left/right point to same, or left/right point to
            max1 = self.grow_palindrome(s, i, i+1)  # even length palindrome, s[i], s[i+1] is center
            max2 = self.grow_palindrome(s, i, i)  # odd length, s[i] is center
            local_max = max(max1, max2, key=len)
            max_so_far = max(max_so_far, local_max, key=len)
        return max_so_far

    def grow_palindrome(self, s, x, y):
        """Grow palindrome from s[x...y] to as large as possible"""
        n = len(s)
        while x >= 0 and y < n and s[x] == s[y]:
            x -= 1; y += 1
        # one size smaller, either mismatch, or out of bound
        return s[x+1:y]


# what I came up with, build a char table and optimize search a bit
class SolutionMe:

    # 94 / 94 test cases passed.
    # Status: Accepted
    # Runtime: 7464 ms (beats 8.76%, haha)
    def longest1(self, s):
        n = len(s)
        chars = collections.defaultdict(list)  # map of chars to their positions
        for i in range(n):
            chars[s[i]].append(i)  # list of pos is sorted, since i goes up

        longest = 1  # shortest palindrome by default
        pa_pos = [0, 0]  # default answer (1st char)

        for k, v in chars.items():
            if len(v) < 2:  # single char, can't be start of longest
                continue
            if v[-1] - v[0] + 1 <= longest:  # if range is too small, ignore
                continue
            pos = self.check_positions(s, v, longest)
            if pos:
                cur_size = pos[1] - pos[0] + 1
                if cur_size > longest:
                    longest = cur_size
                    pa_pos = pos

        return s[pa_pos[0]:pa_pos[1]+1]

    def is_palindrome(self, s, i, j):
        """Is string from pos [i...j] a palindrome"""
        while i < j:  # while point to distinct position
            if s[i] != s[j]:
                return False
            i += 1; j -= 1
        return True

    def check_positions(self, s, pos_list, longest):
        """Check possible palindrome starting from both ends"""
        n = len(pos_list)
        local_max = 0
        local_range = []
        for i in range(n-1):  # i from beginning to 2nd last
            for j in reversed(range(i+1, n)):  # j from end to before i
                a, b = pos_list[i], pos_list[j]
                cur_size = b - a + 1
                if cur_size <= longest or cur_size <= local_max:
                    break  # no need to continue this loop
                if self.is_palindrome(s, a, b):
                    local_max = cur_size
                    local_range = [a, b]
        return local_range


class TestLongest(unittest.TestCase):

    def setUp(self):
        self.sol = Solution()

    def test1(self):
        self.assertIn(self.sol.longestPalindrome('babad'),
                      ['bab', 'aba'])
        self.assertIn(self.sol.longestPalindrome('cbbd'),
                      ['bb'])
        self.assertIn(self.sol.longestPalindrome('babadada'),
                      ['adada'])
        self.assertIn(self.sol.longestPalindrome('bb'),
                      ['bb'])


if __name__ == '__main__':
    unittest.main()
