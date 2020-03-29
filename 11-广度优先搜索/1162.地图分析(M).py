"""
  @Author       : Liujianhan
  @Date         : 20/3/29 15:28
  @FileName     : 1162.地图分析(M).py
  @ProjectName  : leetcode_in_python
  @Description  : 你现在手里有一份大小为 N x N 的『地图』（网格） grid，上面的每个『区域』（单元格）都用 0 和 1 标记好了。其中 0 代表海洋，1 代表陆地，你知道距离陆地区域最远的海洋区域是是哪一个吗？请返回该海洋区域到离它最近的陆地区域的距离。
我们这里说的距离是『曼哈顿距离』（ Manhattan Distance）：(x0, y0) 和 (x1, y1) 这两个区域之间的距离是 |x0 - x1| + |y0 - y1| 。
如果我们的地图上只有陆地或者海洋，请返回 -1。

输入：[[1,0,1],[0,0,0],[1,0,1]]
输出：2
解释：
海洋区域 (1, 1) 和所有陆地区域之间的距离都达到最大，最大距离为 2。
输入：[[1,0,0],[0,0,0],[0,0,0]]
输出：4
解释：
海洋区域 (2, 2) 和所有陆地区域之间的距离都达到最大，最大距离为 4。
 """
from collections import deque
from typing import List


class Solution:
    # 720ms, 14.3MB
    @classmethod
    def max_distance(cls, grid: List[List[int]]) -> int:
        n = len(grid)
        steps = -1
        queue = deque([(i, j) for i in range(n) for j in range(n) if grid[i][j] == 1])
        if not len(queue) or len(queue) == n ** 2:
            return steps
        while len(queue) > 0:
            for _ in range(len(queue)):
                x, y = queue.popleft()
                for xi, yj in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
                    if 0 <= xi < n and n > yj >= 0 and not grid[xi][yj]:
                        queue.append((xi, yj))
                        grid[xi][yj] = -1
            steps += 1

        return steps


if __name__ == '__main__':
    test_cases = [
        [[1, 0, 1], [0, 0, 0], [1, 0, 1]],
        [[1, 0, 0], [0, 0, 0], [0, 0, 0]]
    ]
    for tc in test_cases:
        print(Solution.max_distance(tc))