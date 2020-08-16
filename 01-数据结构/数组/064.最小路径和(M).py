"""
  @Author       : Liujianhan
  @Date         : 20/4/23 22:28
  @FileName     : 064.最小路径和(M).py
  @ProjectName  : leetcode_in_python
  @Description  : 给定一个包含非负整数的 m x n 网格，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。
    说明：每次只能向下或者向右移动一步。
    示例:
    输入:
    [
      [1,3,1],
      [1,5,1],
      [4,2,1]
    ]
    输出: 7
    解释: 因为路径 1→3→1→1→1 的总和最小。
 """
from typing import List


class Solution:
    # 60ms, 14.7MB
    @classmethod
    def min_path_sum(cls, grid: List[List[int]]) -> int:
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if i == j == 0:
                    continue
                elif i == 0:
                    grid[i][j] = grid[i][j - 1] + grid[i][j]
                elif j == 0:
                    grid[i][j] = grid[i - 1][j] + grid[i][j]
                else:
                    grid[i][j] = min(grid[i - 1][j], grid[i][j - 1]) + grid[i][j]

        return grid[-1][-1]


if __name__ == '__main__':
    test_cases = [
        [[1, 3, 1], [1, 5, 1], [4, 2, 1]]
    ]
    for tc in test_cases:
        print(Solution.min_path_sum(tc))

