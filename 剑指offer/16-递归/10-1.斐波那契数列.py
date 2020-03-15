"""
  @Author       : Liujianhan
  @Date         : 20/3/15 12:37
  @FileName     : 10-1.斐波那契数列.py
  @ProjectName  : leetcode_in_python
  @Description  : Placeholder
  执行用时 :36 ms, 在所有 Python3 提交中击败了71.87%的用户
  内存消耗 :13.5 MB, 在所有 Python3 提交中击败了100.00%的用户
 """


class Solution:
    @classmethod
    def fib(cls, n: int) -> int:
        a, b = 0, 1
        for _ in range(n):
            a, b = b, a + b
        return a % 1000000007


if __name__ == '__main__':
    print(Solution.fib(45))
