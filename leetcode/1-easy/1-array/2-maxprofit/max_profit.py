# https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/564/
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/description/

# Best Time to Buy and Sell Stock II
#
# Say you have an array for which the ith element is the price of a
# given stock on day i. Design an algorithm to find the maximum
# profit. You may complete as many transactions as you like (i.e., buy
# one and sell one share of the stock multiple times).


class Solution:

    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        A = prices  # shorthand
        n = len(prices)

        # find the longest decreasing sequence

        profit = 0
        i = 1
        while i < n:
            diff = A[i] - A[i-1]
            if diff > 0:
                profit += diff
            i += 1
        return profit

    # 198 / 198 test cases passed.
    # beats 84.63%
