"""
  @Author       : liujianhan
  @Date         : 2020/8/8 下午7:42
  @Project      : leetcode_in_python
  @FileName     : 1351.统计有序矩阵中的负数.py
  @Description  : 给你一个 m * n 的矩阵 grid，矩阵中的元素无论是按行还是按列，都以非递增顺序排列。 
    请你统计并返回 grid 中 负数 的数目。

    示例 1：

    输入：grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
    输出：8
    解释：矩阵中共有 8 个负数。
    示例 2：

    输入：grid = [[3,2],[1,0]]
    输出：0
    示例 3：

    输入：grid = [[1,-1],[-1,-1]]
    输出：3
    示例 4：

    输入：grid = [[-1]]
    输出：1
     

    提示：

    m == grid.length
    n == grid[i].length
    1 <= m, n <= 100
    -100 <= grid[i][j] <= 100
"""
from typing import List


class Solution:
    # 40ms, 14.4MB
    @staticmethod
    def count_negatives(grid: List[List[int]]) -> int:
        total = 0
        i, j = 0, len(grid[0]) - 1

        while i < len(grid) and j >= 0:
            if grid[i][j] >= 0:
                i += 1
            else:
                total += len(grid) - i
                j -= 1
        return total


if __name__ == '__main__':
    test_cases = [
        [[4, 3, 2, -1], [3, 2, 1, -1], [1, 1, -1, -2], [-1, -1, -2, -3]],
        [[3, 2], [1, 0]],
        [[1, -1], [-1, -1]],
        [[-1]]
    ]
    for tc in test_cases:
        print(Solution.count_negatives(tc))
