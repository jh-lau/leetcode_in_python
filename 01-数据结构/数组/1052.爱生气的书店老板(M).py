"""
  @Author       : liujianhan
  @Date         : 21/2/23 18:51
  @Project      : leetcode_in_python
  @FileName     : 1052.爱生气的书店老板(M).py
  @Description  : 今天，书店老板有一家店打算试营业 customers.length 分钟。每分钟都有一些顾客（customers[i]）会进入书店，
    所有这些顾客都会在那一分钟结束后离开。在某些时候，书店老板会生气。 如果书店老板在第 i 分钟生气，那么 grumpy[i] = 1，
    否则 grumpy[i] = 0。 当书店老板生气时，
    那一分钟的顾客就会不满意，不生气则他们是满意的。
    书店老板知道一个秘密技巧，能抑制自己的情绪，可以让自己连续 X 分钟不生气，但却只能使用一次。
    请你返回这一天营业下来，最多有多少客户能够感到满意的数量。

    示例：
    输入：customers = [1,0,1,2,1,1,7,5], grumpy = [0,1,0,1,0,1,0,1], X = 3
    输出：16
    解释：
    书店老板在最后 3 分钟保持冷静。
    感到满意的最大客户数量 = 1 + 1 + 1 + 1 + 7 + 5 = 16.
    提示：

    1 <= X <= customers.length == grumpy.length <= 20000
    0 <= customers[i] <= 1000
    0 <= grumpy[i] <= 1
"""
from typing import List


class Solution:
    # 300ms, 16.6MB
    @staticmethod
    def max_satisfied(customers: List[int], grumpy: List[int], X: int) -> int:
        t = 0
        for i in range(len(grumpy)):  # 记录下一定满意的顾客数，并把不影响的地方去掉
            if grumpy[i] == 0:
                t += customers[i]
                customers[i] = 0

        n = sum(customers[:X])  # 滑动窗口找连续X个的最大值
        m = n
        for i in range(1, len(customers) - X + 1):
            m = m + customers[i + X - 1] - customers[i - 1]
            n = max(m, n)
        return n + t


if __name__ == '__main__':
    test_cases = [
        ([1, 0, 1, 2, 1, 1, 7, 5], [0, 1, 0, 1, 0, 1, 0, 1], 3),
    ]
    for test_case in test_cases:
        print(Solution.max_satisfied(*test_case))
