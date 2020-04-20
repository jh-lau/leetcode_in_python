"""
  @Author       : liujianhan
  @Date         : 2020/4/20 上午10:56
  @Project      : leetcode_in_python
  @FileName     : 200.岛屿数量(M).py
  @Description  : 给你一个由 '1'（陆地）和 '0'（水）组成的的二维网格，请你计算网格中岛屿的数量。
    岛屿总是被水包围，并且每座岛屿只能由水平方向和/或竖直方向上相邻的陆地连接形成。
    此外，你可以假设该网格的四条边均被水包围。
    示例 1:

    输入:
    11110
    11010
    11000
    00000
    输出: 1
    示例 2:

    输入:
    11000
    11000
    00100
    00011
    输出: 3
    解释: 每座岛屿只能由水平和/或竖直方向上相邻的陆地连接而成。
"""
import collections
from typing import List


class Solution:
    # 80ms, 14.6MB
    @classmethod
    def num_is_island(cls, grid: List[List[str]]) -> int:
        def dfs(gird: List[List[str]], r: int, c: int):
            grid[r][c] = 0
            nr, nc = len(gird), len(gird[0])
            for x, y in [(r-1, c), (r+1, c), (r, c-1), (r, c+1)]:
                if nr > x >= 0 and nc > y >= 0 and grid[x][y] == '1':
                    dfs(grid, x, y)

        row_num = len(grid)
        if not row_num:
            return 0
        col_num = len(grid[0])

        num_islands = 0
        for row in range(row_num):
            for col in range(col_num):
                if grid[row][col] == '1':
                    num_islands += 1
                    dfs(grid, row, col)

        return num_islands

    # 68ms, 14.1MB
    @classmethod
    def num_is_island_v2(cls, grid: List[List[str]]) -> int:
        nr = len(grid)
        if nr == 0:
            return 0
        nc = len(grid[0])

        num_islands = 0
        for r in range(nr):
            for c in range(nc):
                if grid[r][c] == "1":
                    num_islands += 1
                    grid[r][c] = "0"
                    neighbors = collections.deque([(r, c)])
                    while neighbors:
                        row, col = neighbors.popleft()
                        for x, y in [(row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)]:
                            if 0 <= x < nr and 0 <= y < nc and grid[x][y] == "1":
                                neighbors.append((x, y))
                                grid[x][y] = "0"

        return num_islands

    # 11ms, 15.9MB
    @classmethod
    def num_is_island_v3(cls, grid: List[List[str]]) -> int:
        nr = len(grid)
        if nr == 0:
            return 0
        nc = len(grid[0])

        uf = UnionFind(grid)
        for r in range(nr):
            for c in range(nc):
                if grid[r][c] == "1":
                    grid[r][c] = "0"
                    for x, y in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]:
                        if 0 <= x < nr and 0 <= y < nc and grid[x][y] == "1":
                            uf.union(r * nc + c, x * nc + y)

        return uf.get_count()


class UnionFind:
    def __init__(self, grid):
        m, n = len(grid), len(grid[0])
        self.count = 0
        self.parent = [-1] * (m * n)
        self.rank = [0] * (m * n)
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    self.parent[i * n + j] = i * n + j
                    self.count += 1

    def find(self, i):
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, x, y):
        rootx = self.find(x)
        rooty = self.find(y)
        if rootx != rooty:
            if self.rank[rootx] < self.rank[rooty]:
                rootx, rooty = rooty, rootx
            self.parent[rooty] = rootx
            if self.rank[rootx] == self.rank[rooty]:
                self.rank[rootx] += 1
            self.count -= 1

    def get_count(self):
        return self.count


if __name__ == '__main__':
    test_cases = [
        [['1', '1', '1', '1', '0'], ['1', '1', '0', '1', '0'], ['1', '1', '0', '0', '0'], ['0', '0', '0', '0', '0']],
        [['1', '1', '0', '0', '0'], ['1', '1', '0', '0', '0'], ['0', '0', '1', '0', '0'], ['0', '0', '0', '1', '1']]
    ]
    for tc in test_cases:
        # print(Solution.num_is_island(tc))
        # print(Solution.num_is_island_v2(tc))
        print(Solution.num_is_island_v3(tc))
