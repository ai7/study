# https://leetcode.com/explore/interview/card/top-interview-questions-medium/111/dynamic-programming/807/
# https://leetcode.com/problems/jump-game/description/

# Jump Game
#
# Given an array of non-negative integers, you are initially
# positioned at the first index of the array. Each element in the
# array represents your maximum jump length at that position.
# Determine if you are able to reach the last index.

import functools
import unittest


class Solution:

    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        return self.my_jump3(nums)

    # Note: can we jump to the last success position from here?
    #
    # Scan backwards from end, at each position, see if pos+jump can
    # reach the last success position. If so, update last successful
    # position to current pos. At the end, check if last_good is 0.
    #
    # Figured out all these by myself, yeah. ;)

    # 75 / 75 test cases passed.
    # Status: Accepted
    # Runtime: 44 ms (beats 99.09% py3)
    def my_jump3(self, A):

        n = len(A)
        last_good = n-1

        for j in reversed(range(n-1)):  # from 2nd last down to 1st position
            v = A[j]
            if j + v >= last_good:  # if can reach earliest success
                last_good = j  # current node is success

        return last_good == 0  # is starting position a success?

    # Note: use an array to keep track of earliest success position
    #
    # for each index. Scan backwards from end, at each position, see
    # if pos+jump can reach the last success position. If so, current
    # pos is success, otherwise, re-use previous last-succcess
    # position in current position.
    #
    # Probably don't need an array, as we simply need to track a
    # value..

    # start from end, goes backward, proper dynamic programming?
    # 75 / 75 test cases passed.
    # Status: Accepted (after several tries)
    # Runtime: 52 ms (beats 80.88% py3)
    def my_jump2(self, A):

        n = len(A)
        t_index = n-1  # target index

        # track the last success position
        result = [None] * n
        result[t_index] = t_index  # last pos is success

        for j in reversed(range(n-1)):  # from 2nd last down to 1st position
            v = A[j]
            if j + v >= result[j+1]:  # if can reach earliest success
                result[j] = j  # current node is success
            else:
                result[j] = result[j+1]  # copy previous value

        return result[0] == 0  # is starting position a success?

    # this is memorization, should work, but, one test case with all
    # 1's exceed maximum recursion depth, hehe.
    def my_jump(self, A):

        @functools.lru_cache()
        def check_pos(i):
            if i >= target:  # if already reached target, success
                return True
            steps = A[i]
            if steps <= 0:  # if no available steps, done
                return False
            for x in range(1, steps+1):  # for each 1...x step, try it
                if check_pos(i+x):
                    return True
            return False

        if not A:
            return
        target = len(A)-1  # last position

        return check_pos(0)


class TestJump(unittest.TestCase):

    def setUp(self):
        self.sol = Solution()

    def test1(self):
        self.assertTrue(self.sol.canJump([2,3,1,1,4]))
        self.assertFalse(self.sol.canJump([3,2,1,0,4]))


if __name__ == '__main__':
    unittest.main()
