"""
  @Author       : liujianhan
  @Date         : 2020/3/16 上午9:27
  @Project      : leetcode_in_python
  @FileName     : 10-2.青蛙跳台阶问题.py
  @Description  : 一只青蛙一次可以跳上1级台阶，也可以跳上2级台阶。求该青蛙跳上一个 n 级的台阶总共有多少种跳法。
  答案需要取模 1e9+7（1000000007），如计算初始结果为：1000000008，请返回 1。
  n = 2 --> 2
  n = 7 --> 21
  0 <= n <= 100
"""


class Solution:
    # 40ms, 13.6MB  --> 54.47%, 100%
    @classmethod
    def num_ways(cls, n: int) -> int:
        a, b = 1, 1
        for _ in range(n):
            a, b = b, a + b
        return a % 1000000007


if __name__ == '__main__':
    print(Solution.num_ways(7))
