"""
  @Author       : liujianhan
  @Date         : 2020/4/20 下午2:36
  @Project      : leetcode_in_python
  @FileName     : 329.矩阵中的最长递增路径(H).py
  @Description  : 给定一个整数矩阵，找出最长递增路径的长度。
    对于每个单元格，你可以往上，下，左，右四个方向移动。 你不能在对角线方向上移动或移动到边界外（即不允许环绕）。
    示例 1:

    输入: nums =
    [
      [9,9,4],
      [6,6,8],
      [2,1,1]
    ]
    输出: 4
    解释: 最长递增路径为 [1, 2, 6, 9]。
    示例 2:

    输入: nums =
    [
      [3,4,5],
      [3,2,6],
      [2,2,1]
    ]
    输出: 4
    解释: 最长递增路径是 [3, 4, 5, 6]。注意不允许在对角线方向上移动。
"""
import itertools
from functools import lru_cache
from typing import List


class Solution:
    # 944ms, 14.3MB
    @classmethod
    def longest_increasing_path(cls, matrix: List[List[int]]) -> int:
        if not matrix:
            return 0

        m = len(matrix)
        n = len(matrix[0])
        paths = [[0 for _ in range(n)] for _ in range(m)]
        directions = [[-1, 0], [1, 0], [0, 1], [0, -1]]

        def dfs(i, j):
            if paths[i][j] != 0:
                return paths[i][j]

            ans = 1
            for direction in directions:
                new_i = i + direction[0]
                new_j = j + direction[1]
                if 0 <= new_i < m and 0 <= new_j < n and matrix[i][j] < matrix[new_i][new_j]:
                    ans = max(ans, dfs(new_i, new_j) + 1)
            paths[i][j] = ans

            return paths[i][j]

        res = 0
        for i in range(m):
            for j in range(n):
                res = max(res, dfs(i, j))

        return res

    # 684ms, 20.1MB
    @classmethod
    def longest_increasing_path_v2(cls, matrix: List[List[int]]) -> int:
        if not matrix:
            return 0
        r, c, d = len(matrix), len(matrix[0]), ((0, 1), (0, -1), (1, 0), (-1, 0))

        @lru_cache(None)
        def f(i, j):
            t = 0
            for di, dj in d:
                x, y = i + di, j + dj
                if 0 <= x < r and 0 <= y < c and matrix[x][y] > matrix[i][j]:
                    t = max(t, f(x, y))
            return t + 1

        return max(f(i, j) for i, j in itertools.product(range(r), range(c)))


if __name__ == '__main__':
    test_cases = [
        [
            [9, 9, 4],
            [6, 6, 8],
            [2, 1, 1]
        ],
        [
            [3, 4, 5],
            [3, 2, 6],
            [2, 2, 1]
        ]
    ]
    for tc in test_cases:
        print(Solution.longest_increasing_path(tc))
        print(Solution.longest_increasing_path_v2(tc))
