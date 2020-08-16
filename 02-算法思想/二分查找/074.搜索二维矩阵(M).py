"""
  @Author       : Liujianhan
  @Date         : 20/5/3 20:20
  @FileName     : 074.搜索二维矩阵(M).py
  @ProjectName  : leetcode_in_python
  @Description  : 编写一个高效的算法来判断 m x n 矩阵中，是否存在一个目标值。该矩阵具有如下特性：
    每行中的整数从左到右按升序排列。
    每行的第一个整数大于前一行的最后一个整数。
    示例 1:
    输入:
    matrix = [
      [1,   3,  5,  7],
      [10, 11, 16, 20],
      [23, 30, 34, 50]
    ]
    target = 3
    输出: true
    示例 2:
    输入:
    matrix = [
      [1,   3,  5,  7],
      [10, 11, 16, 20],
      [23, 30, 34, 50]
    ]
    target = 13
    输出: false
 """
from typing import List


class Solution:
    # 40ms, 14.4MB
    @classmethod
    def search_matrix(cls, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        if not m:
            return False
        n = len(matrix[0])

        left, right = 0, m * n - 1
        while left <= right:
            pivot_idx = (left + right) >> 1
            pivot_element = matrix[pivot_idx // n][pivot_idx % n]
            if target == pivot_element:
                return True
            else:
                if target < pivot_element:
                    right = pivot_idx - 1
                else:
                    left = pivot_idx + 1

        return False


if __name__ == '__main__':
    test_cases = [
        ([
             [1, 3, 5, 7],
             [10, 11, 16, 20],
             [23, 30, 34, 50]
         ], 3),
        ([
             [1, 3, 5, 7],
             [10, 11, 16, 20],
             [23, 30, 34, 50]
         ], 13)
    ]
    for tc in test_cases:
        print(Solution.search_matrix(*tc))
