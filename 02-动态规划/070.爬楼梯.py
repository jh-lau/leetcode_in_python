"""
  @Author       : liujianhan
  @Date         : 2020/3/20 上午11:06
  @Project      : leetcode_in_python
  @FileName     : 070.爬楼梯.py
  @Description  : 假设你正在爬楼梯。需要 n 阶你才能到达楼顶。
    每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？
    注意：给定 n 是一个正整数。
"""


class Solution:
    # 40ms, 13.7MB
    @classmethod
    def climb_stairs(cls, n: int) -> int:
        a, b = 1, 1
        for _ in range(n):
            a, b = b, a + b
        return a


if __name__ == '__main__':
    for s in range(10):
        print(s, Solution.climb_stairs(s))
