"""Stock Buy And Sell

Problem Statement:
You are given an array of prices where prices[i] is the price of a given stock on an ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future
to sell that stock. Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit,
return 0.
"""
import doctest
from typing import List

"""Examples

Example 1:
Input:
 prices = [7,1,5,3,6,4]
Output:
 5
Explanation:
 Buy on day 2 (price = 1) and 
sell on day 5 (price = 6), profit = 6-1 = 5.
"""


class Solution:

    def brute_force_approach(self, prices: List[int]) -> int:
        """
        >>> prices = [7,1,5,3,6,4]
        >>> Solution().brute_force_approach(prices)
        5
        >>> prices = [7,6,4,3,1]
        >>> Solution().brute_force_approach(prices)
        0
        """
        days = len(prices)
        stock_low = stock_high = 0
        profit = 0
        for day in range(days):

            # next adjacent high, low
            stock_low = prices[day]
            for next_date in range(day + 1, days):
                if stock_low > prices[next_date]:
                    stock_low = prices[next_date]
                elif prices[next_date] > stock_high:
                    stock_high = prices[next_date]

            # print("SS", stock_high, stock_low)

            if stock_high > prices[day]:
                profit = stock_high - prices[day]
                break
            elif stock_high > stock_low:
                profit = stock_high - stock_low
                break

        return profit


if __name__ == "__main__":
    doctest.testmod()
