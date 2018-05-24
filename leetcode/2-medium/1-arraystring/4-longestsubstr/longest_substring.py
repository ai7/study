# https://leetcode.com/explore/interview/card/top-interview-questions-medium/103/array-and-strings/779/
# https://leetcode.com/problems/longest-substring-without-repeating-characters/

# Longest Substring Without Repeating Characters
#
# Given a string, find the length of the longest substring without
# repeating characters.

import unittest


class Solution:

    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        return self.substr2(s)

    # similar to my substr2 below, but simplified/optimized further, as we
    # don't need to delete hashmap, we can check whether i's position
    # is before or after the duplicate position, hmmmm.
    def substr3(self, s):
        start = max_length = 0
        used_char = {}  # dict of char and their index

        for i in range(len(s)):  # for each char in string

            # if char is a repeat, and my current start is
            # before the repeat location
            if s[i] in used_char and start <= used_char[s[i]]:
                # advance start to after the repeat location
                start = used_char[s[i]] + 1
            else:
                # not a repeat, or repeat before start pos (can ignore)
                # update max length
                max_length = max(max_length, i - start + 1)

            # regardless, update char index (will clobber previous value)
            used_char[s[i]] = i

        return max_length

    # figured this out on my own (Sliding Window Optimized)
    # 983 / 983 test cases passed.
    # Runtime: 104 ms (beat 58.04%, yeah hehe)
    def substr2(self, s):
        if not s:
            return 0
        n = len(s)

        longest = 0
        data = {}

        i = j = 0
        while i + longest < n:  # while possible longer str

            repeat = False
            while j < n:
                if s[j] in data:  # if found repeat char
                    repeat = True
                    break
                data[s[j]] = j  # add char to set
                j += 1
            # after loop, either found repeat, or reach end

            longest = max(longest, j - i)

            if not repeat:  # j must've reached end
                assert(j == n)
                break

            # found a repeat, forward i to repeat char
            pos = data[s[j]]  # find repeat char position
            for t in range(i, pos+1):
                del data[s[t]]  # remove all char up to and including dup
            i = pos+1  # set i to next position

        return longest


    # 982 / 983 test cases passed.
    # Time Limit Exceeded
    def substr1(self, s):
        if not s:
            return 0
        n = len(s)

        longest = []
        last_j = 0

        for i in range(n):  # for each starting char

            current_str = [s[i]]
            for j in range(i + 1, n):
                if s[j] not in current_str:  # if unique
                    current_str.append(s[j])  # update local max
                else:
                    break  # done
            if len(current_str) > len(longest):  # update longest
                longest = current_str
            if i + len(current_str) >= n:
                # no point going further as remaining can only be shorter substrs
                break

        return len(longest)


class TestLongest(unittest.TestCase):

    def setUp(self):
        self.sol = Solution()

    def test1(self):
        self.assertEqual(self.sol.lengthOfLongestSubstring('abcabcbb'),
                         3)
        self.assertEqual(self.sol.lengthOfLongestSubstring('bbbbb'),
                         1)
        self.assertEqual(self.sol.lengthOfLongestSubstring('pwwkew'),
                         3)
        self.assertEqual(self.sol.lengthOfLongestSubstring('dvdf'),
                         3)


if __name__ == '__main__':
    unittest.main()
