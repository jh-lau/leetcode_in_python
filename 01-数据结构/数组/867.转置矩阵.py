"""
  @Author       : liujianhan
  @Date         : 2020/12/14 10:02
  @Project      : leetcode_in_python
  @FileName     : 867.转置矩阵.py
  @Description  : 给定一个矩阵 A， 返回 A 的转置矩阵。
    矩阵的转置是指将矩阵的主对角线翻转，交换矩阵的行索引与列索引。

    示例 1：
    输入：[[1,2,3],[4,5,6],[7,8,9]]
    输出：[[1,4,7],[2,5,8],[3,6,9]]

    示例 2：
    输入：[[1,2,3],[4,5,6]]
    输出：[[1,4],[2,5],[3,6]]

    提示：

    1 <= A.length <= 1000
    1 <= A[0].length <= 1000
"""
from typing import List


class Solution:
    # 92ms, 15.4MB
    @staticmethod
    def transpose(A: List[List[int]]) -> List[List[int]]:
        row, col = len(A), len(A[0])
        res = [[0] * row for _ in range(col)]
        for i in range(row):
            for j in range(col):
                res[j][i] = A[i][j]
        return res


if __name__ == '__main__':
    test_cases = [
        [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
        [[1, 2, 3], [4, 5, 6]]
    ]
    for tc in test_cases:
        print(Solution.transpose(tc))
