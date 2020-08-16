"""
  @Author       : Liujianhan
  @Date         : 20/5/9 21:44
  @FileName     : 120.三角形最小路径和(M).py
  @ProjectName  : leetcode_in_python
  @Description  : 给定一个三角形，找出自顶向下的最小路径和。每一步只能移动到下一行中相邻的结点上。
    例如，给定三角形：
    [
         [2],
        [3,4],
       [6,5,7],
      [4,1,8,3]
    ]
    自顶向下的最小路径和为 11（即，2 + 3 + 5 + 1 = 11）。
    说明：
    如果你可以只使用 O(n) 的额外空间（n 为三角形的总行数）来解决这个问题，那么你的算法会很加分。
 """
from typing import List


class Solution:
    # 68ms, 14.2MB
    @classmethod
    def minimum_total(cls, triangle: List[List[int]]) -> int:
        m = len(triangle)
        for i in range(1, m):
            for j in range(i + 1):
                if j == 0:
                    triangle[i][j] += triangle[i - 1][j]
                if j > 0 and j == i:
                    triangle[i][j] += triangle[i - 1][j - 1]
                elif 0 < j < i:
                    triangle[i][j] += min(triangle[i - 1][j - 1], triangle[i - 1][j])
        return min(triangle[m - 1])


if __name__ == '__main__':
    print(Solution.minimum_total(
        [
            [2],
            [3, 4],
            [6, 5, 7],
            [4, 1, 8, 3]
        ]
    ))