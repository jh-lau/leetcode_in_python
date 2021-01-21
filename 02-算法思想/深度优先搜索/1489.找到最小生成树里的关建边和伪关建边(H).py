"""
  @Author       : liujianhan
  @Date         : 2021/1/21 9:35
  @Project      : leetcode_in_python
  @FileName     : 1489.找到最小生成树里的关建边和伪关建边(H).py
  @Description  : 给你一个 n 个点的带权无向连通图，节点编号为 0 到 n-1 ，同时还有一个数组 edges ，
    其中 edges[i] = [fromi, toi, weighti] 表示在 fromi 和 toi 节点之间有一条带权无向边。最小生成树 (MST) 是给定图中边的一个子集，
    它连接了所有节点且没有环，而且这些边的权值和最小。
    请你找到给定图中最小生成树的所有关键边和伪关键边。如果从图中删去某条边，会导致最小生成树的权值和增加，那么我们就说它是一条关键边。
    伪关键边则是可能会出现在某些最小生成树中但不会出现在所有最小生成树中的边。
    请注意，你可以分别以任意顺序返回关键边的下标和伪关键边的下标。

    示例 1：
    输入：n = 5, edges = [[0,1,1],[1,2,1],[2,3,2],[0,3,2],[0,4,3],[3,4,3],[1,4,6]]
    输出：[[0,1],[2,3,4,5]]
    解释：上图描述了给定图。
    下图是所有的最小生成树。

    注意到第 0 条边和第 1 条边出现在了所有最小生成树中，所以它们是关键边，我们将这两个下标作为输出的第一个列表。
    边 2，3，4 和 5 是所有 MST 的剩余边，所以它们是伪关键边。我们将它们作为输出的第二个列表。
    示例 2 ：
    输入：n = 4, edges = [[0,1,1],[1,2,1],[2,3,1],[0,3,1]]
    输出：[[],[0,1,2,3]]
    解释：可以观察到 4 条边都有相同的权值，任选它们中的 3 条可以形成一棵 MST 。所以 4 条边都是伪关键边。

    提示：
    2 <= n <= 100
    1 <= edges.length <= min(200, n * (n - 1) / 2)
    edges[i].length == 3
    0 <= fromi < toi < n
    1 <= weighti <= 1000
    所有 (fromi, toi) 数对都是互不相同的。
"""

# 并查集模板
import collections
from typing import List


class UnionFind:
    def __init__(self, n: int):
        self.parent = list(range(n))
        self.size = [1] * n
        self.n = n
        # 当前连通分量数目
        self.setCount = n

    def findset(self, x: int) -> int:
        if self.parent[x] == x:
            return x
        self.parent[x] = self.findset(self.parent[x])
        return self.parent[x]

    def unite(self, x: int, y: int) -> bool:
        x, y = self.findset(x), self.findset(y)
        if x == y:
            return False
        if self.size[x] < self.size[y]:
            x, y = y, x
        self.parent[y] = x
        self.size[x] += self.size[y]
        self.setCount -= 1
        return True

    def connected(self, x: int, y: int) -> bool:
        x, y = self.findset(x), self.findset(y)
        return x == y


# Tarjan 算法求桥边模版
class TarjanSCC:
    def __init__(self, n: int, edges: List[List[int]], edgesId: List[List[int]]):
        self.n = n
        self.edges = edges
        self.edgesId = edgesId
        self.low = [-1] * n
        self.dfn = [-1] * n
        self.ans = list()
        self.ts = -1

    def getCuttingEdge(self) -> List[int]:
        for i in range(self.n):
            if self.dfn[i] == -1:
                self.pGetCuttingEdge(i, -1)
        return self.ans

    def pGetCuttingEdge(self, u: int, parentEdgeId: int):
        self.ts += 1
        self.low[u] = self.dfn[u] = self.ts
        for v, iden in zip(self.edges[u], self.edgesId[u]):
            if self.dfn[v] == -1:
                self.pGetCuttingEdge(v, iden)
                self.low[u] = min(self.low[u], self.low[v])
                if self.low[v] > self.dfn[u]:
                    self.ans.append(iden)
            elif iden != parentEdgeId:
                self.low[u] = min(self.low[u], self.dfn[v])


class Solution:
    #
    @staticmethod
    def find_critical_and_pseudo_critical_edges(n: int, edges: List[List[int]]) -> List[List[int]]:
        m = len(edges)
        for i, edge in enumerate(edges):
            edge.append(i)
        edges.sort(key=lambda x: x[2])

        uf = UnionFind(n)
        ans0 = list()
        label = [0] * m

        i = 0
        while i < m:
            # 找出所有权值为 w 的边，下标范围为 [i, j)
            w = edges[i][2]
            j = i
            while j < m and edges[j][2] == edges[i][2]:
                j += 1

            # 存储每个连通分量在图 G 中的编号
            compToId = dict()
            # 图 G 的节点数
            gn = 0

            for k in range(i, j):
                x = uf.findset(edges[k][0])
                y = uf.findset(edges[k][1])
                if x != y:
                    if x not in compToId:
                        compToId[x] = gn
                        gn += 1
                    if y not in compToId:
                        compToId[y] = gn
                        gn += 1
                else:
                    # 将自环边标记为 -1
                    label[edges[k][3]] = -1

            # 图 G 的边
            gm = collections.defaultdict(list)
            gmid = collections.defaultdict(list)

            for k in range(i, j):
                x = uf.findset(edges[k][0])
                y = uf.findset(edges[k][1])
                if x != y:
                    idx, idy = compToId[x], compToId[y]
                    gm[idx].append(idy)
                    gmid[idx].append(edges[k][3])
                    gm[idy].append(idx)
                    gmid[idy].append(edges[k][3])

            bridges = TarjanSCC(gn, gm, gmid).getCuttingEdge()
            # 将桥边（关键边）标记为 1
            ans0.extend(bridges)
            for iden in bridges:
                label[iden] = 1

            for k in range(i, j):
                uf.unite(edges[k][0], edges[k][1])

            i = j

        # 未标记的边即为非桥边（伪关键边）
        ans1 = [i for i in range(m) if label[i] == 0]

        return [ans0, ans1]


if __name__ == '__main__':
    test_cases = [
        (5, [[0, 1, 1], [1, 2, 1], [2, 3, 2], [0, 3, 2], [0, 4, 3], [3, 4, 3], [1, 4, 6]]),
        (4, [[0, 1, 1], [1, 2, 1], [2, 3, 1], [0, 3, 1]])
    ]
    for tc in test_cases:
        print(Solution.find_critical_and_pseudo_critical_edges(*tc))
