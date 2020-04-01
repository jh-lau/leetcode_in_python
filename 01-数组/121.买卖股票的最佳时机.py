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
