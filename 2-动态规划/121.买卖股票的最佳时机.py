"""
  User: Liujianhan
 """
__author__ = 'liujianhan'


class Solution:
    @staticmethod
    def max_profit(prices):
        result, buy = 0, float('inf')
        for price in prices:
            if buy > price:
                buy = price
            if result < price - buy:
                result = price - buy
        return result

    @staticmethod
    def dp_method(prices):
        mini, maxi = float('inf'), 0
        for i in range(len(prices)):
            mini = min(mini, prices[i])
            maxi = max(maxi, prices[i] - mini)
        return maxi
