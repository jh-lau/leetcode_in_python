"""
  @Author       : liujianhan
  @Date         : 2021/1/29 10:04
  @Project      : leetcode_in_python
  @FileName     : 1631.最小体力消耗路径(M).py
  @Description  : 你准备参加一场远足活动。给你一个二维 rows x columns 的地图 heights ，其中 heights[row][col] 
    表示格子 (row, col) 的高度。一开始你在最左上角的格子 (0, 0) ，且你希望去最右下角的格子 (rows-1, columns-1) 
    （注意下标从 0 开始编号）。你每次可以往 上，下，左，右 四个方向之一移动，你想要找到耗费 体力 最小的一条路径。
    一条路径耗费的 体力值 是路径上相邻格子之间 高度差绝对值 的 最大值 决定的。
    请你返回从左上角走到右下角的最小 体力消耗值 。

    示例 1：
    输入：heights = [[1,2,2],[3,8,2],[5,3,5]]
    输出：2
    解释：路径 [1,3,5,3,5] 连续格子的差值绝对值最大为 2 。
    这条路径比路径 [1,2,2,2,5] 更优，因为另一条路径差值最大值为 3 。

    示例 2：
    输入：heights = [[1,2,3],[3,8,4],[5,3,5]]
    输出：1
    解释：路径 [1,2,3,4,5] 的相邻格子差值绝对值最大为 1 ，比路径 [1,3,5,3,5] 更优。

    示例 3：
    输入：heights = [[1,2,1,1,1],[1,2,1,2,1],[1,2,1,2,1],[1,2,1,2,1],[1,1,1,2,1]]
    输出：0
    解释：上图所示路径不需要消耗任何体力。

    提示：
    rows == heights.length
    columns == heights[i].length
    1 <= rows, columns <= 100
    1 <= heights[i][j] <= 106
"""

# 并查集模板
from typing import List


class UnionFind:
    def __init__(self, n: int):
        self.parent = list(range(n))
        self.size = [1] * n
        self.n = n
        # 当前连通分量数目
        self.setCount = n

    def find_set(self, x: int) -> int:
        if self.parent[x] == x:
            return x
        self.parent[x] = self.find_set(self.parent[x])
        return self.parent[x]

    def unite(self, x: int, y: int) -> bool:
        x, y = self.find_set(x), self.find_set(y)
        if x == y:
            return False
        if self.size[x] < self.size[y]:
            x, y = y, x
        self.parent[y] = x
        self.size[x] += self.size[y]
        self.setCount -= 1
        return True

    def connected(self, x: int, y: int) -> bool:
        x, y = self.find_set(x), self.find_set(y)
        return x == y


class Solution:
    # 584ms, 18.4MB
    @staticmethod
    def minimum_effort_path(heights: List[List[int]]) -> int:
        m, n = len(heights), len(heights[0])
        edges = list()
        for i in range(m):
            for j in range(n):
                iden = i * n + j
                if i > 0:
                    edges.append((iden - n, iden, abs(heights[i][j] - heights[i - 1][j])))
                if j > 0:
                    edges.append((iden - 1, iden, abs(heights[i][j] - heights[i][j - 1])))

        edges.sort(key=lambda e: e[2])

        uf = UnionFind(m * n)
        ans = 0
        for x, y, v in edges:
            uf.unite(x, y)
            if uf.connected(0, m * n - 1):
                ans = v
                break

        return ans


if __name__ == '__main__':
    test_cases = [
        [[1, 2, 2], [3, 8, 2], [5, 3, 5]],
        [[1, 2, 3], [3, 8, 4], [5, 3, 5]],
        [[1, 2, 1, 1, 1], [1, 2, 1, 2, 1], [1, 2, 1, 2, 1], [1, 2, 1, 2, 1], [1, 1, 1, 2, 1]]
    ]
    for tc in test_cases:
        print(Solution.minimum_effort_path(tc))
