# https://leetcode.com/explore/interview/card/top-interview-questions-easy/98/design/670/
# https://leetcode.com/problems/shuffle-an-array/description/

# Shuffle an Array
#
# Shuffle a set of numbers without duplicates.

# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()

import random


class Solution:

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.save = nums

    def reset(self):
        """
        Resets the array to its original configuration and return it.
        :rtype: List[int]
        """
        return self.save

    def shuffle(self):
        """
        Returns a random shuffling of the array.
        :rtype: List[int]
        """
        if not self.save:
            return self.save

        A = self.save[:]  # make a copy
        # A = list(self.save)

        n = len(A)
        for i in range(n):
            # swap current element with an item no earlier than current
            k = random.randint(i, n-1)
            A[i], A[k] = A[k], A[i]

        return A

        # 10 / 10 test cases passed.
        # beats 52.76%

        # grading tests all permutations, so may fail sometimes even though
        # solution is correct


# someone posted just for fun, haha
class Solution2(object):
    def __init__(self, nums):
        self.reset = lambda: nums
        self.shuffle = lambda: random.sample(nums, len(nums))
