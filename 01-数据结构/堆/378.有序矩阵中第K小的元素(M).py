"""
  @Author       : liujianhan
  @Date         : 2020/7/2 下午8:21
  @Project      : leetcode_in_python
  @FileName     : 378.有序矩阵中第K小的元素(M).py
  @Description  : 给定一个 n x n 矩阵，其中每行和每列元素均按升序排序，找到矩阵中第 k 小的元素。
请注意，它是排序后的第 k 小元素，而不是第 k 个不同的元素。
    示例：
    matrix = [
       [ 1,  5,  9],
       [10, 11, 13],
       [12, 13, 15]
    ],
    k = 8,
    返回 13。
    提示：
    你可以假设 k 的值永远是有效的，1 ≤ k ≤ n2 。
"""
from typing import List


class Solution:
    # 200ms, 19.5MB
    @staticmethod
    def kth_smallest(matrix: List[List[int]], k: int) -> int:
        n = len(matrix)

        def check(mid):
            i, j = n - 1, 0
            num = 0
            while i >= 0 and j < n:
                if matrix[i][j] <= mid:
                    num += i + 1
                    j += 1
                else:
                    i -= 1
            return num >= k

        left, right = matrix[0][0], matrix[-1][-1]
        while left < right:
            mid = (left + right) // 2
            if check(mid):
                right = mid
            else:
                left = mid + 1

        return left


if __name__ == '__main__':
    print(Solution.kth_smallest([
        [1, 5, 9],
        [10, 11, 13],
        [12, 13, 15]], 8))
