"""
  @Author       : liujianhan
  @Date         : 2020/6/5 上午9:56
  @Project      : leetcode_in_python
  @FileName     : 29.顺时针打印矩阵.py
  @Description  : 输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字。
    示例 1：
    输入：matrix = [[1,2,3],[4,5,6],[7,8,9]]
    输出：[1,2,3,6,9,8,7,4,5]
    示例 2：
    输入：matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
    输出：[1,2,3,4,8,12,11,10,9,5,6,7]
    限制：
    0 <= matrix.length <= 100
    0 <= matrix[i].length <= 100
"""
from typing import List


class Solution:
    # 48ms, 13.8MB
    @classmethod
    def spiral_order(cls, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return list()

        rows, columns = len(matrix), len(matrix[0])
        order = list()
        left, right, top, bottom = 0, columns - 1, 0, rows - 1
        while left <= right and top <= bottom:
            for column in range(left, right + 1):
                order.append(matrix[top][column])
            for row in range(top + 1, bottom + 1):
                order.append(matrix[row][right])
            if left < right and top < bottom:
                for column in range(right - 1, left, -1):
                    order.append(matrix[bottom][column])
                for row in range(bottom, top, -1):
                    order.append(matrix[row][left])
            left, right, top, bottom = left + 1, right - 1, top + 1, bottom - 1

        return order


if __name__ == '__main__':
    test_cases = [
        [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
        [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
    ]
    for tc in test_cases:
        print(Solution.spiral_order(tc))
