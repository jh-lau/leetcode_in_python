"""
  @Author       : Liujianhan
  @Date         : 20/5/4 21:13
  @FileName     : 077.组合(M).py
  @ProjectName  : leetcode_in_python
  @Description  : 给定两个整数 n 和 k，返回 1 ... n 中所有可能的 k 个数的组合。
    示例:
    输入: n = 4, k = 2
    输出:
    [
      [2,4],
      [3,4],
      [2,3],
      [1,2],
      [1,3],
      [1,4],
    ]
 """
from typing import List


class Solution:
    # 516ms, 15.1MB
    @classmethod
    def combine(cls, n: int, k: int) -> List[List[int]]:
        output = []

        def backtrack(first=1, curr=[]):
            if len(curr) == k:
                nonlocal output
                output.append(curr[:])
            for i in range(first, n + 1):
                curr.append(i)
                backtrack(i + 1, curr)
                curr.pop()

        backtrack()

        return output


if __name__ == '__main__':
    test_cases = [
        (4, 2)
    ]
    for tc in test_cases:
        print(Solution.combine(*tc))
