# https://leetcode.com/explore/interview/card/top-interview-questions-medium/111/dynamic-programming/809/
# https://leetcode.com/problems/coin-change/description/

# Coin Change
#
# You are given coins of different denominations and a total amount of
# money amount. Write a function to compute the fewest number of coins
# that you need to make up that amount. If that amount of money cannot
# be made up by any combination of the coins, return -1.

import unittest
import functools


class Solution:
    
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        return self.my_change3(coins, amount)

    # Note: this can be solved either top down with memoization, or
    # bottom up using a memo/dp array.
    #
    # For top down or bottom up, the sub problem is simply the amount
    # less ONE specific coin (not x multiplier [or highest multiplier]
    # of said coin). This is crucial. For each round, we return the
    # minimum of trying all x coins.
    #
    # To see why this is true:
    # - for top down, if we start with the highest multiplier, we are
    #   sort of jumping ahead in our recursion tree (so later answers
    #   may be better and it's hard for us to revise our previously
    #   calculated answer.
    # - For bottom up, we only need to try amount less 1-coin, since
    #   amount less multiple of said coin would've been analyzed in
    #   previous rounds (since we assume all previous data are optimal).

    # Note from discussion:
    #   Assume dp[i] is the fewest number of coins making up amount i,
    #   then for every coin in coins, dp[i] = min(dp[i - coin] + 1).

    # let's try bottom up, simplified solution
    # 182 / 182 test cases passed.
    # Status: Accepted (after multiple failed ones. ;)
    # Runtime: 1476 ms (beats 46.99% of py3)
    def my_change3(self, A, k):

        if not A:  # if no coin
            return -1
        if k <= 0:  # if invalid amount
            return 0

        # fill array with max possible value + 1 so our code is simpler
        memo = [k+1] * (k+1)  # fill array (size k+1) with k+1 (max value)
        memo[0] = 0

        for v in range(1, k+1):  # for value from [1...k]
            for c in A:  # for each coin
                if c <= v:  # if coin less than amount
                    # no need to check if memo has 'data' or not, or track
                    # a local minimum and update after innermost for loop.
                    memo[v] = min(memo[v], memo[v - c] + 1)

        return memo[k] if memo[k] <= k else -1

    # top down with memorization.
    def my_change2(self, A, k):

        # can we make change for amount x, starting from ith coin
        @functools.lru_cache(k+1)
        def make_change(x):

            if x < 0:  # invalid change, return false
                return -1
            if x == 0:  # done
                return 0
            if x < smallest_coin:  # not possible
                return -1

            min_coin = float('inf')  # local minimum
            for c in A:  # for each coin [type]
                res = make_change(x - c)  # simply subtract this coin, and recurse
                if res >= 0:  # if valid path
                    min_coin = min(min_coin, res+1)  # update local min

            # return the minimum we have, after trying all x coins
            return min_coin if min_coin != float('inf') else -1

        if not A:
            return -1
        if k <= 0:
            return 0

        A.sort(reverse=True)  # sort in desending order
        smallest_coin = A[-1]

        return make_change(k)


class SolutionX:

    # my simple greedy algorithm, didn't work.
    # worked for simple cases, but fails for other inputs.
    def my_change(self, A, k):
        if not A:
            return -1
        if k <= 0:
            return 0

        A.sort(reverse=True)  # sort in desending order

        retval = 0
        for c in A:  # for each coin in list
            if c > k:  # if larger than what we need, skip
                continue
            retval += k // c  # how many coins
            k %= c
            if k == 0:
                return retval

        return -1


class TestCoin(unittest.TestCase):

    def setUp(self):
        self.sol = Solution()

    def test2(self):
        self.assertEqual(self.sol.coinChange([70,177,394,428,427,437,176,145,83,370], 7582), 18)

    # @unittest.skip
    def test1(self):
        self.assertEqual(self.sol.coinChange([1, 2, 5], 11), 3)
        self.assertEqual(self.sol.coinChange([2], 3), -1)
        self.assertEqual(self.sol.coinChange([3,7,405,436], 8839), 25)
        self.assertEqual(self.sol.coinChange([186, 419, 83, 408], 6249), 20)


if __name__ == '__main__':
    unittest.main()
