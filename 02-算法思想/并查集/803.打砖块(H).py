"""
  @Author       : liujianhan
  @Date         : 21/1/16 14:43
  @Project      : leetcode_in_python
  @FileName     : 803.打砖块(H).py
  @Description  : 有一个 m x n 的二元网格，其中 1 表示砖块，0 表示空白。砖块 稳定（不会掉落）的前提是：
    一块砖直接连接到网格的顶部，或者
    至少有一块相邻（4 个方向之一）砖块 稳定 不会掉落时
    给你一个数组 hits ，这是需要依次消除砖块的位置。每当消除 hits[i] = (rowi, coli) 位置上的砖块时，对应位置的砖块（若存在）会消失，
    然后其他的砖块可能因为这一消除操作而掉落。一旦砖块掉落，它会立即从网格中消失（即，它不会落在其他稳定的砖块上）。
    返回一个数组 result ，其中 result[i] 表示第 i 次消除操作对应掉落的砖块数目。
    注意，消除可能指向是没有砖块的空白位置，如果发生这种情况，则没有砖块掉落。

    示例 1：
    输入：grid = [[1,0,0,0],[1,1,1,0]], hits = [[1,0]]
    输出：[2]
    解释：
    网格开始为：
    [[1,0,0,0]，
     [1,1,1,0]]
    消除 (1,0) 处加粗的砖块，得到网格：
    [[1,0,0,0]
     [0,1,1,0]]
    两个加粗的砖不再稳定，因为它们不再与顶部相连，也不再与另一个稳定的砖相邻，因此它们将掉落。得到网格：
    [[1,0,0,0],
     [0,0,0,0]]
    因此，结果为 [2] 。

    示例 2：
    输入：grid = [[1,0,0,0],[1,1,0,0]], hits = [[1,1],[1,0]]
    输出：[0,0]
    解释：
    网格开始为：
    [[1,0,0,0],
     [1,1,0,0]]
    消除 (1,1) 处加粗的砖块，得到网格：
    [[1,0,0,0],
     [1,0,0,0]]
    剩下的砖都很稳定，所以不会掉落。网格保持不变：
    [[1,0,0,0],
     [1,0,0,0]]
    接下来消除 (1,0) 处加粗的砖块，得到网格：
    [[1,0,0,0],
     [0,0,0,0]]
    剩下的砖块仍然是稳定的，所以不会有砖块掉落。
    因此，结果为 [0,0] 。

    提示：

    m == grid.length
    n == grid[i].length
    1 <= m, n <= 200
    grid[i][j] 为 0 或 1
    1 <= hits.length <= 4 * 104
    hits[i].length == 2
    0 <= xi <= m - 1
    0 <= yi <= n - 1
    所有 (xi, yi) 互不相同
"""
from typing import List


class Solution:
    # 508ms, 20.7MB
    @staticmethod
    def hit_bricks(grid: List[List[int]], hits: List[List[int]]) -> List[int]:
        drop = []
        current = 0
        for hit in hits:
            grid[hit[0]][hit[1]] = grid[hit[0]][hit[1]] - 1
        for j in range(len(grid[0])):
            current = current + visit(0, j, grid)
        total = current
        for i in range(len(hits) - 1, -1, -1):
            x, y = hits[i][0], hits[i][1]
            grid[x][y] = grid[x][y] + 1
            if not grid[x][y]:
                drop.append(0)
                continue
            if x != 0 and not judge(x - 1, y, grid) + judge(x + 1, y, grid) + \
                              judge(x, y - 1, grid) + judge(x, y + 1, grid):
                drop.append(0)
                continue
            current = visit(x, y, grid)
            total = total + current
            drop.append(current - 1)
        drop.reverse()
        return drop


def visit(i, j, grid) -> int:
    if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] != 1:
        return 0
    grid[i][j] = grid[i][j] + 1
    return visit(i - 1, j, grid) + visit(i + 1, j, grid) + \
           visit(i, j - 1, grid) + visit(i, j + 1, grid) + 1


def judge(i, j, grid) -> int:
    if 0 <= i < len(grid) and 0 <= j < len(grid[0]) and grid[i][j] == 2:
        return 1
    return 0


if __name__ == '__main__':
    test_cases = [
        ([[1, 0, 0, 0], [1, 1, 1, 0]], [[1, 0]]),
        ([[1, 0, 0, 0], [1, 1, 0, 0]], [[1, 1], [1, 0]])
    ]
    for tc in test_cases:
        print(Solution.hit_bricks(*tc))
