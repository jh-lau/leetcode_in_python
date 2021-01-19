"""
  @Author       : liujianhan
  @Date         : 2021/1/19 16:16
  @Project      : leetcode_in_python
  @FileName     : 1584.连接所有点的最小费用(M).py
  @Description  : 给你一个points 数组，表示 2D 平面上的一些点，其中 points[i] = [xi, yi] 。
    连接点 [xi, yi] 和点 [xj, yj] 的费用为它们之间的 曼哈顿距离 ：|xi - xj| + |yi - yj| ，其中 |val| 表示 val 的绝对值。
    请你返回将所有点连接的最小总费用。只有任意两点之间 有且仅有 一条简单路径时，才认为所有点都已连接。
     
    示例 1：
    输入：points = [[0,0],[2,2],[3,10],[5,2],[7,0]]
    输出：20
    解释：
    我们可以按照上图所示连接所有点得到最小总费用，总费用为 20 。
    注意到任意两个点之间只有唯一一条路径互相到达。

    示例 2：
    输入：points = [[3,12],[-2,5],[-4,1]]
    输出：18

    示例 3：
    输入：points = [[0,0],[1,1],[1,0],[-1,1]]
    输出：4

    示例 4：
    输入：points = [[-1000000,-1000000],[1000000,1000000]]
    输出：4000000

    示例 5：
    输入：points = [[0,0]]

    输出：0

    提示：
    1 <= points.length <= 1000
    -106 <= xi, yi <= 106
    所有点 (xi, yi) 两两不同。
"""
import bisect
from typing import List, Tuple


class DisjointSetUnion:
    def __init__(self, n):
        self.n = n
        self.rank = [1] * n
        self.f = list(range(n))

    def find(self, x: int) -> int:
        if self.f[x] == x:
            return x
        self.f[x] = self.find(self.f[x])
        return self.f[x]

    def unionSet(self, x: int, y: int) -> bool:
        fx, fy = self.find(x), self.find(y)
        if fx == fy:
            return False

        if self.rank[fx] < self.rank[fy]:
            fx, fy = fy, fx

        self.rank[fx] += self.rank[fy]
        self.f[fy] = fx
        return True


class BIT:
    def __init__(self, n):
        self.n = n
        self.tree = [float("inf")] * n
        self.idRec = [-1] * n
        self.lowbit = lambda x: x & (-x)

    def update(self, pos: int, val: int, identity: int):
        while pos > 0:
            if self.tree[pos] > val:
                self.tree[pos] = val
                self.idRec[pos] = identity
            pos -= self.lowbit(pos)

    def query(self, pos: int) -> int:
        minval, j = float("inf"), -1
        while pos < self.n:
            if minval > self.tree[pos]:
                minval = self.tree[pos]
                j = self.idRec[pos]
            pos += self.lowbit(pos)
        return j


class Solution:
    # 176ms, 15.9MB
    @staticmethod
    def min_cost_connection_points(points: List[List[int]]) -> int:
        n = len(points)
        edges = list()

        def build(pos: List[Tuple[int, int, int]]):
            pos.sort()
            a = [y - x for (x, y, _) in pos]
            b = sorted(set(a))
            num = len(b)

            bit = BIT(num + 1)
            for i in range(n - 1, -1, -1):
                poss = bisect.bisect(b, a[i])
                j = bit.query(poss)
                if j != -1:
                    dis = abs(pos[i][0] - pos[j][0]) + abs(pos[i][1] - pos[j][1])
                    edges.append((dis, pos[i][2], pos[j][2]))
                bit.update(poss, pos[i][0] + pos[i][1], i)

        def solve():
            pos = [(x, y, i) for i, (x, y) in enumerate(points)]
            build(pos)
            pos = [(y, x, i) for i, (x, y) in enumerate(points)]
            build(pos)
            pos = [(-y, x, i) for i, (x, y) in enumerate(points)]
            build(pos)
            pos = [(x, -y, i) for i, (x, y) in enumerate(points)]
            build(pos)

        solve()
        dsu = DisjointSetUnion(n)
        edges.sort()

        ret, num = 0, 1
        for length, x, y in edges:
            if dsu.unionSet(x, y):
                ret += length
                num += 1
                if num == n:
                    break

        return ret


if __name__ == '__main__':
    test_cases = [
        [[0, 0], [2, 2], [3, 10], [5, 2], [7, 0]],
        [[3, 12], [-2, 5], [-4, 1]],
        [[0, 0], [1, 1], [1, 0], [-1, 1]],
        [[-1000000, -1000000], [1000000, 1000000]],
        [[0, 0]]
    ]
    for tc in test_cases:
        print(Solution.min_cost_connection_points(tc))