"""
  @Author       : liujianhan
  @Date         : 20/9/26 19:31
  @Project      : leetcode_in_python
  @FileName     : 778.水位上升的泳池中游泳(H).py
  @Description  : 在一个 N x N 的坐标方格 grid 中，每一个方格的值 grid[i][j] 表示在位置 (i,j) 的平台高度。
    现在开始下雨了。当时间为 t 时，此时雨水导致水池中任意位置的水位为 t 。你可以从一个平台游向四周相邻的任意一个平台，
    但是前提是此时水位必须同时淹没这两个平台。假定你可以瞬间移动无限距离，也就是默认在方格内部游动是不耗时的。
    当然，在你游泳的时候你必须待在坐标方格里面。
    你从坐标方格的左上平台 (0，0) 出发。最少耗时多久你才能到达坐标方格的右下平台 (N-1, N-1)？
    示例 1:

    输入: [[0,2],[1,3]]
    输出: 3
    解释:
    时间为0时，你位于坐标方格的位置为 (0, 0)。
    此时你不能游向任意方向，因为四个相邻方向平台的高度都大于当前时间为 0 时的水位。

    等时间到达 3 时，你才可以游向平台 (1, 1). 因为此时的水位是 3，坐标方格中的平台没有比水位 3 更高的，所以你可以游向坐标方格中的任意位置
    示例2:

    输入: [[0,1,2,3,4],[24,23,22,21,5],[12,13,14,15,16],[11,17,18,19,20],[10,9,8,7,6]]
    输出: 16
    解释:
     0  1  2  3  4
    24 23 22 21  5
    12 13 14 15 16
    11 17 18 19 20
    10  9  8  7  6

    最终的路线用加粗进行了标记。
    我们必须等到时间为 16，此时才能保证平台 (0, 0) 和 (4, 4) 是连通的
     
    提示:

    2 <= N <= 50.
    grid[i][j] 位于区间 [0, ..., N*N - 1] 内。
"""
import bisect
import sys
from typing import List


class Solution:
    # 228ms, 14MB
    @staticmethod
    def swim_in_water(grid: List[List[int]]) -> int:
        """
        并查集
        @param grid:
        @return:
        """
        n = len(grid)
        p = [[(i, j) for j in range(n)] for i in range(n)]  # 并查集二维数组初始化
        h = sorted([[grid[i][j], i, j] for j in range(n) for i in range(n)])  # 按高度对点排序

        def f(a, b):
            if (a, b) != p[a][b]:
                p[a][b] = f(*p[a][b])  # 二元并查集，元组传参要用*解包
            return p[a][b]

        k = 0
        for t in range(max(grid[0][0], grid[-1][-1]), h[-1][0]):  # 起点是两个对角的最大值，终点是整个数据里的最大高度
            while h[k][0] <= t:
                _, i, j = h[k]
                for x, y in [(i + 1, j), (i, j + 1), (i - 1, j), (i, j - 1)]:
                    if 0 <= x < n and 0 <= y < n:
                        if grid[i][j] <= t and grid[x][y] <= t:
                            (pi, pj), (px, py) = f(i, j), f(x, y)
                            if (pi, pj) != (px, py):  # 让符合时间空间条件且不相同的集合合并
                                p[px][py] = (pi, pj)
                k += 1
            if f(0, 0) == f(n - 1, n - 1):  # 首末元素属于同一个集合就返回答案
                return t
        return h[-1][0]

    # 172ms,, 13.8MB
    @staticmethod
    def swim_in_water_v2(grid: List[List[int]]) -> int:
        """
        BFS
        @param grid:
        @return:
        """
        n = len(grid)
        c = {(0, 0)}  # 访问标记
        for t in range(max(grid[0][0], grid[-1][-1]), sys.maxsize):  # 从首末元素的最大时间作为最开始的判断条件
            p = c.copy()  # 宽搜队列初始化，每个时间点的初始状态是上一轮时间访问标记过的坐标
            while p:
                q = set()  # 下一批宽搜队列
                for i, j in p:
                    if i == j == n - 1:  # 如果走到目标了就返回时间
                        return t
                    for x, y in [(i + 1, j), (i, j + 1), (i - 1, j), (i, j - 1)]:
                        if 0 <= x < n and 0 <= y < n and grid[x][y] <= t and (x, y) not in c:  # 符合时空条件就扩散地图
                            q |= {(x, y)}
                            c |= {(x, y)}
                p = q

    # 128ms, 13.8MB
    @staticmethod
    def swim_in_water_v3(grid: List[List[int]]) -> int:
        """
        升序队列
        @param grid:
        @return:
        """
        n = len(grid)
        b = {(0, 0)}  # 访问标记
        p = [[grid[0][0], 0, 0]]  # 升序队列初始化
        t = 0  # 途径最大时间标记
        while True:
            h, i, j = p.pop(0)
            t = max(t, h)
            if i == j == n - 1:  # 找到终点就就返回时间
                return t
            for x, y in [(i + 1, j), (i, j + 1), (i - 1, j), (i, j - 1)]:
                if 0 <= x < n and 0 <= y < n and (x, y) not in b:
                    bisect.insort(p, [grid[x][y], x, y])  # 二分插入
                    b |= {(x, y)}

    # 140ms, 13.7MB
    @staticmethod
    def swim_in_water_v4(grid: List[List[int]]) -> int:
        """
        双向升序队列
        @param grid:
        @return:
        """
        n = len(grid)
        b, e = {(0, 0)}, {(n - 1, n - 1)}  # 双向访问标记
        p, q = [[grid[0][0], 0, 0]], [[grid[-1][-1], n - 1, n - 1]]  # 双向升序队列初始化
        t = 0  # 途径最大时间标记
        while True:
            h, i, j = p.pop(0)
            t = max(t, h)
            if (i, j) in e:  # 如果找到的点已经存在于另一个队列里，就返回答案
                return t
            for x, y in [(i + 1, j), (i, j + 1), (i - 1, j), (i, j - 1)]:
                if 0 <= x < n and 0 <= y < n and (x, y) not in b:
                    bisect.insort(p, [grid[x][y], x, y])
                    b |= {(x, y)}
            h, i, j = q.pop(0)  # 从这里开始都是对称的，调换p，q，b，e就行。
            t = max(t, h)
            if (i, j) in b:
                return t
            for x, y in [(i + 1, j), (i, j + 1), (i - 1, j), (i, j - 1)]:
                if 0 <= x < n and 0 <= y < n and (x, y) not in e:
                    bisect.insort(q, [grid[x][y], x, y])
                    e |= {(x, y)}


if __name__ == '__main__':
    test_cases = [
        [[0, 2], [1, 3]],
        [[0, 1, 2, 3, 4], [24, 23, 22, 21, 5], [12, 13, 14, 15, 16], [11, 17, 18, 19, 20], [10, 9, 8, 7, 6]],
    ]
    for tc in test_cases:
        print(Solution.swim_in_water(tc))
        print(Solution.swim_in_water_v2(tc))
        print(Solution.swim_in_water_v3(tc))
        print(Solution.swim_in_water_v4(tc))
