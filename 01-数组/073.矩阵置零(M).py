"""
  @Author       : Liujianhan
  @Date         : 20/5/3 20:00
  @FileName     : 073.矩阵置零(M).py
  @ProjectName  : leetcode_in_python
  @Description  : 给定一个 m x n 的矩阵，如果一个元素为 0，则将其所在行和列的所有元素都设为 0。请使用原地算法。
 """
from pprint import pprint
from typing import List


class Solution:
    # 60ms, 14.1MB
    @classmethod
    def set_zeroes(cls, matrix: List[List[int]]) -> None:
        row = len(matrix)
        col = len(matrix[0])
        row_zero = set()
        col_zero = set()
        for i in range(row):
            for j in range(col):
                if matrix[i][j] == 0:
                    row_zero.add(i)
                    col_zero.add(j)
        for i in range(row):
            for j in range(col):
                if i in row_zero or j in col_zero:
                    matrix[i][j] = 0

    # 72ms, 14.1MB
    @classmethod
    def set_zeroes_v2(cls, matrix: List[List[int]]) -> None:
        flag_col = False
        row = len(matrix)
        col = len(matrix[0])
        for i in range(row):
            if matrix[i][0] == 0:
                flag_col = True
            for j in range(1, col):
                if matrix[i][j] == 0:
                    matrix[i][0] = matrix[0][j] = 0

        for i in range(row - 1, -1, -1):
            for j in range(col - 1, 0, -1):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

            if flag_col:
                matrix[i][0] = 0


if __name__ == '__main__':
    test_cases = [
        [
            [1, 1, 1],
            [1, 0, 1],
            [1, 1, 1]
        ],
        [
            [0, 1, 2, 0],
            [3, 4, 5, 2],
            [1, 3, 1, 5]
        ]
    ]
    for tc in test_cases:
        # Solution.set_zeroes(tc)
        Solution.set_zeroes_v2(tc)
        pprint(tc)
