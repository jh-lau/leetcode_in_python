"""
  @Author       : Liujianhan
  @Date         : 20/5/31 8:59
  @FileName     : 188.买卖股票的最佳时机IV(H).py
  @ProjectName  : leetcode_in_python
  @Description  : 给定一个数组，它的第 i 个元素是一支给定的股票在第 i 天的价格。
    设计一个算法来计算你所能获取的最大利润。你最多可以完成 k 笔交易。
    注意: 你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。
    示例 1:
    输入: [2,4,1], k = 2
    输出: 2
    解释: 在第 1 天 (股票价格 = 2) 的时候买入，在第 2 天 (股票价格 = 4) 的时候卖出，这笔交易所能获得利润 = 4-2 = 2 。
    示例 2:
    输入: [3,2,6,5,0,3], k = 2
    输出: 7
    解释: 在第 2 天 (股票价格 = 2) 的时候买入，在第 3 天 (股票价格 = 6) 的时候卖出, 这笔交易所能获得利润 = 6-2 = 4 。
         随后，在第 5 天 (股票价格 = 0) 的时候买入，在第 6 天 (股票价格 = 3) 的时候卖出, 这笔交易所能获得利润 = 3-0 = 3 。
     """
from typing import List


class Solution:
    # 136ms, 14MB
    @classmethod
    def max_profit(cls, prices: List[int], k: int) -> int:
        if k > len(prices) >> 1:  # 有效的 k 可以是取任意个，即次数不限
            dp_i0, dp_i1 = 0, float('-inf')
            for price in prices:
                dp_i0_old = dp_i0
                dp_i0 = max(dp_i0, dp_i1 + price)
                dp_i1 = max(dp_i1, dp_i0_old - price)
            return dp_i0

        dp_ik0, dp_ik1 = [0] * (k + 1), [float('-inf')] * (k + 1)
        for price in prices:
            for j in range(1, k + 1):
                dp_ik0[j] = max(dp_ik0[j], dp_ik1[j] + price)
                dp_ik1[j] = max(dp_ik1[j], dp_ik0[j - 1] - price)
        return dp_ik0[k]


if __name__ == '__main__':
    test_cases = [
        ([2, 4, 1], 2),
        ([3, 2, 6, 5, 0, 3], 2)
    ]
    for tc in test_cases:
        print(Solution.max_profit(*tc))
