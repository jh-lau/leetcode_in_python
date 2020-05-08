"""
  @Author       : Liujianhan
  @Date         : 20/5/8 22:02
  @FileName     : 221.最大正方形(M).py
  @ProjectName  : leetcode_in_python
  @Description  : 在一个由 0 和 1 组成的二维矩阵内，找到只包含 1 的最大正方形，并返回其面积。
    示例:
    输入:
    1 0 1 0 0
    1 0 1 1 1
    1 1 1 1 1
    1 0 0 1 0
    输出: 4
 """
from typing import List


class Solution:
    # 92ms, 14.3MB
    @classmethod
    def maximal_square(cls, matrix: List[List[str]]) -> int:
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return 0

        max_side = 0
        rows, columns = len(matrix), len(matrix[0])
        dp = [[0] * columns for _ in range(rows)]
        for i in range(rows):
            for j in range(columns):
                if matrix[i][j] == '1':
                    if i == 0 or j == 0:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
                    max_side = max(max_side, dp[i][j])

        res = max_side * max_side
        return res


if __name__ == '__main__':
    print(Solution.maximal_square(
        [['1', '0', '1', '0', '0'],
         ['1', '0', '1', '1', '1'],
         ['1', '1', '1', '1', '1'],
         ['1', '0', '0', '1', '0']]
    ))
