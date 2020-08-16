"""
  @Author       : liujianhan
  @Date         : 2020/7/30 上午10:01
  @Project      : leetcode_in_python
  @FileName     : 343.整数拆分(M).py
  @Description  : 给定一个正整数 n，将其拆分为至少两个正整数的和，并使这些整数的乘积最大化。 返回你可以获得的最大乘积。

    示例 1:

    输入: 2
    输出: 1
    解释: 2 = 1 + 1, 1 × 1 = 1。
    示例 2:

    输入: 10
    输出: 36
    解释: 10 = 3 + 3 + 4, 3 × 3 × 4 = 36。
    说明: 你可以假设 n 不小于 2 且不大于 58。

    通过次数38,757提交次数67,402
"""


class Solution:
    # 40ms, 13.6MB
    @staticmethod
    def integer_break(n: int) -> int:
        if n < 4:
            return n - 1
        dp = [0] * (n + 1)
        dp[2] = 1
        for i in range(3, n + 1):
            dp[i] = max(2 * (i - 2), 2 * dp[i - 2], 3 * (i - 3), 3 * dp[i - 3])

        return dp[n]

    # 36ms, 13.7MB
    @staticmethod
    def integer_break_v2(n: int) -> int:
        if n <= 3:
            return n - 1

        quotient, remainder = divmod(n, 3)
        if remainder == 0:
            return 3 ** quotient
        elif remainder == 1:
            return 3 ** (quotient - 1) * 4
        else:
            return 3 ** quotient * 2


if __name__ == '__main__':
    for s in [2, 10, 12]:
        print(Solution.integer_break(s))
        print(Solution.integer_break_v2(s))
