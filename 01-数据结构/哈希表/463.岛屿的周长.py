"""
  @Author       : liujianhan
  @Date         : 2020/10/30 9:56
  @Project      : leetcode_in_python
  @FileName     : 463.岛屿的周长.py
  @Description  : 给定一个包含 0 和 1 的二维网格地图，其中 1 表示陆地 0 表示水域。
    网格中的格子水平和垂直方向相连（对角线方向不相连）。整个网格被水完全包围，但其中恰好有一个岛屿（或者说，一个或多个表示陆地的格子相连组成的岛屿）。
    岛屿中没有“湖”（“湖” 指水域在岛屿内部且不和岛屿周围的水相连）。格子是边长为 1 的正方形。网格为长方形，且宽度和高度均不超过 100 。计算这个岛屿的周长。
    示例 :

    输入:
    [[0,1,0,0],
     [1,1,1,0],
     [0,1,0,0],
     [1,1,0,0]]

    输出: 16
"""
from typing import List
from pprint import pprint as print


class Solution:
    # 204ms, 14.5MB
    @staticmethod
    def island_perimeter(grid: List[List[int]]) -> int:
        lookup = {}
        for row_index, row in enumerate(grid):
            for index, num in enumerate(row):
                if num:
                    lookup[(row_index, index)] = 4

        for key, value in lookup.items():
            row_index, index = key
            left = (row_index, index - 1)
            right = (row_index, index + 1)
            up = (row_index + 1, index)
            down = (row_index - 1, index)
            for neighbour in [left, right, up, down]:
                if neighbour in lookup:
                    lookup[neighbour] -= 1

        return sum(lookup.values())

    # 108ms, 13.6MB
    @staticmethod
    def island_perimeter_v2(grid: List[List[int]]) -> int:
        res = 0
        for i, row in enumerate(grid):
            for j, num in enumerate(row):
                if num:
                    res += 4
                    if i > 0 and grid[i-1][j]:
                        res -= 2
                    if j > 0 and grid[i][j-1]:
                        res -= 2
        return res


if __name__ == '__main__':
    test_cases = [
        [[0, 1, 0, 0],
         [1, 1, 1, 0],
         [0, 1, 0, 0],
         [1, 1, 0, 0]]
    ]
    for tc in test_cases:
        print(Solution.island_perimeter(tc))
        print(Solution.island_perimeter_v2(tc))
