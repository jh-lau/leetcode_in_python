"""
  @Author       : liujianhan
  @Date         : 2020/4/20 下午2:13
  @Project      : leetcode_in_python
  @FileName     : 892.三维形体的表面积.py
  @Description  : 在 N * N 的网格上，我们放置一些 1 * 1 * 1  的立方体。
    每个值 v = grid[i][j] 表示 v 个正方体叠放在对应单元格 (i, j) 上。
    请你返回最终形体的表面积。
    示例 1：
    输入：[[2]]
    输出：10
    示例 2：
    输入：[[1,2],[3,4]]
    输出：34
    示例 3：
    输入：[[1,0],[0,2]]
    输出：16
    示例 4：
    输入：[[1,1,1],[1,0,1],[1,1,1]]
    输出：32
    示例 5：
    输入：[[2,2,2],[2,1,2],[2,2,2]]
    输出：46
    提示：
    1 <= N <= 50
    0 <= grid[i][j] <= 50
"""
from typing import List


class Solution:
    # 164ms, 13.8MB
    @classmethod
    def surface_area(cls, grid: List[List[int]]) -> int:
        length = len(grid)

        ans = 0
        for r in range(length):
            for c in range(length):
                if grid[r][c]:
                    ans += 2
                    for nr, nc in ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)):
                        if 0 <= nr < length and 0 <= nc < length:
                            value = grid[nr][nc]
                        else:
                            value = 0

                        ans += max(grid[r][c] - value, 0)

        return ans


if __name__ == '__main__':
    test_cases = [
        [[2]],
        [[1, 2], [3, 4]],
        [[1, 0], [0, 2]],
        [[1, 1, 1], [1, 0, 1], [1, 1, 1]],
        [[2, 2, 2], [2, 1, 2], [2, 2, 2]]
    ]
    for tc in test_cases:
        print(Solution.surface_area(tc))
