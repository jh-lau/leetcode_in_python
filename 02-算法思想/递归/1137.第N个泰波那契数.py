"""
  @Author       : liujianhan
  @Date         : 2020/11/4 19:26
  @Project      : leetcode_in_python
  @FileName     : 1137.第N个泰波那契数.py
  @Description  : 泰波那契序列 Tn 定义如下： 
    T0 = 0, T1 = 1, T2 = 1, 且在 n >= 0 的条件下 Tn+3 = Tn + Tn+1 + Tn+2
    给你整数 n，请返回第 n 个泰波那契数 Tn 的值。

    示例 1：

    输入：n = 4
    输出：4
    解释：
    T_3 = 0 + 1 + 1 = 2
    T_4 = 1 + 1 + 2 = 4
    示例 2：

    输入：n = 25
    输出：1389537

    提示：

    0 <= n <= 37
    答案保证是一个 32 位整数，即 answer <= 2^31 - 1。
"""


class Solution:
    # 40ms, 13.5MB
    @staticmethod
    def tribonacci(n: int) -> int:
        result = [0, 1, 1]
        for s in range(3, n+1):
            result.append(sum(result[s-3:s]))
        return result[n]


if __name__ == '__main__':
    test_cases = [
        1, 2, 3, 0, 4, 25
    ]
    for tc in test_cases:
        print(tc, Solution.tribonacci(tc))
