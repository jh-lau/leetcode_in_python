"""
  @Author       : liujianhan
  @Date         : 2020/9/28 17:55
  @Project      : leetcode_in_python
  @FileName     : 375.猜数字大小II(M).py
  @Description  : 我们正在玩一个猜数游戏，游戏规则如下：
    我从 1 到 n 之间选择一个数字，你来猜我选了哪个数字。
    每次你猜错了，我都会告诉你，我选的数字比你的大了或者小了。
    然而，当你猜了数字 x 并且猜错了的时候，你需要支付金额为 x 的现金。直到你猜到我选的数字，你才算赢得了这个游戏。
    示例:

    n = 10, 我选择了8.

    第一轮: 你猜我选择的数字是5，我会告诉你，我的数字更大一些，然后你需要支付5块。
    第二轮: 你猜是7，我告诉你，我的数字更大一些，你支付7块。
    第三轮: 你猜是9，我告诉你，我的数字更小一些，你支付9块。

    游戏结束。8 就是我选的数字。

    你最终要支付 5 + 7 + 9 = 21 块钱。
    给定 n ≥ 1，计算你至少需要拥有多少现金才能确保你能赢得这个游戏。
"""
import functools


class Solution:
    # 2368ms, 13.8MB
    @staticmethod
    def get_money_amount(n: int) -> int:
        dp = [[0] * (n + 1) for _ in range(n + 1)]
        for i in range(1, n):
            dp[i][i + 1] = i
        for low in range(n - 1, 0, -1):
            for high in range(low + 1, n + 1):
                dp[low][high] = min(x + max(dp[low][x - 1], dp[x + 1][high]) for x in range(low, high))
        return dp[1][n]

    @functools.lru_cache(None)
    def solve(self, l, r):
        if l == r: return 0
        if r - l == 1: return l
        if r - l == 2: return l + 1
        ans = sum(range(r))
        for x in range(l+r>>1, r):
            ans = min(max(self.solve(l, x-1), self.solve(x+1, r))+x, ans)
        return ans

    # 780ms, 22.1MB
    def get_money_amount_v2(self, n: int) -> int:
        return self.solve(1, n)


if __name__ == '__main__':
    test_cases = [
        10
    ]
    for tc in test_cases:
        print(Solution.get_money_amount(tc))
        print(Solution().get_money_amount_v2(tc))
