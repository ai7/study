# https://leetcode.com/explore/interview/card/top-interview-questions-easy/97/dynamic-programming/572/
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/

# Best Time to Buy and Sell Stock
#
# Say you have an array for which the ith element is the price of a
# given stock on day i.
#
# If you were only permitted to complete at most one transaction
# (i.e., buy one and sell one share of the stock), design an algorithm
# to find the maximum profit.


class Solution:

    # Note: track lowest price and best deal at each step.
    #
    # if x > low, update best deal if higher
    # if x < low, update low
    
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        A = prices
        if not A or len(A) < 2:
            return 0

        low = A[0]
        profit = 0
        for x in A[1:]:
            if x > low:  # if current is higher than lowest
                profit = max(profit, x - low)  # update profit
            elif x < low:  # if current is lower than lowest
                low = x  # update lowest, can't update profit yet

        return profit

    # 200 / 200 test cases passed.
    # beats 98.44% of py3, yeah!
