"""
  @Author       : Liujianhan
  @Date         : 20/4/25 16:18
  @FileName     : 048.旋转图像(M).py
  @ProjectName  : leetcode_in_python
  @Description  : 给定一个 n × n 的二维矩阵表示一个图像。
    将图像顺时针旋转 90 度。
    说明：
    你必须在原地旋转图像，这意味着你需要直接修改输入的二维矩阵。请不要使用另一个矩阵来旋转图像。
    示例 1:
    给定 matrix =
    [
      [1,2,3],
      [4,5,6],
      [7,8,9]
    ],
    原地旋转输入矩阵，使其变为:
    [
      [7,4,1],
      [8,5,2],
      [9,6,3]
    ]
    示例 2:
    给定 matrix =
    [
      [ 5, 1, 9,11],
      [ 2, 4, 8,10],
      [13, 3, 6, 7],
      [15,14,12,16]
    ],
    原地旋转输入矩阵，使其变为:
    [
      [15,13, 2, 5],
      [14, 3, 4, 1],
      [12, 6, 8, 9],
      [16, 7,10,11]
    ]
 """
from typing import List


class Solution:
    # 44ms, 13.7MB
    @classmethod
    def rotate(cls, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        # 水平上下翻转
        for i in range(n // 2):
            for j in range(n):
                matrix[i][j], matrix[n-i-1][j] = matrix[n-i-1][j], matrix[i][j]

        # 主对角线翻转
        for i in range(n):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # 40ms, 13.8MB
    @classmethod
    def rotate_v2(cls, matrix: List[List[int]]) -> None:
        n = len(matrix)
        r = list(zip(*matrix[::-1]))
        for i in range(n):
            for j in range(n):
                matrix[i][j] = r[i][j]


if __name__ == '__main__':
    test_cases = [
        [
            [5, 1, 9, 11],
            [2, 4, 8, 10],
            [13, 3, 6, 7],
            [15, 14, 12, 16]
        ],
        [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]
    ]
    for tc in test_cases:
        Solution.rotate(tc)
        print(tc)
