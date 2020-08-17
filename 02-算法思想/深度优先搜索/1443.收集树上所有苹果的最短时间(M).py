"""
  @Author       : liujianhan
  @Date         : 2020/8/17 13:52
  @Project      : leetcode_in_python
  @FileName     : 1443.收集树上所有苹果的最短时间(M).py
  @Description  : 给你一棵有 n 个节点的无向树，节点编号为 0 到 n-1 ，它们中有一些节点有苹果。通过树上的一条边，需要花费 1 秒钟。你从 节点 0 出发，请你返回最少需要多少秒，可以收集到所有苹果，并回到节点 0 。
    无向树的边由 edges 给出，其中 edges[i] = [fromi, toi] ，表示有一条边连接 from 和 toi 。除此以外，还有一个布尔数组 hasApple ，其中 hasApple[i] = True 代表节点 i 有一个苹果，否则，节点 i 没有苹果。
    示例 1：
    输入：n = 7, edges = [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]], hasApple = [False,False,True,False,True,True,False]
    输出：8
    解释：上图展示了给定的树，其中红色节点表示有苹果。一个能收集到所有苹果的最优方案由绿色箭头表示。
    示例 2：

    输入：n = 7, edges = [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]], hasApple = [False,False,True,False,False,True,False]
    输出：6
    解释：上图展示了给定的树，其中红色节点表示有苹果。一个能收集到所有苹果的最优方案由绿色箭头表示。
    示例 3：
    输入：n = 7, edges = [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]], hasApple = [False,False,False,False,False,False,False]
    输出：0

    提示：

    1 <= n <= 10^5
    edges.length == n-1
    edges[i].length == 2
    0 <= fromi, toi <= n-1
    fromi < toi
    hasApple.length == n
"""
import collections
from typing import List


class Solution:
    # 264ms, 43.7MB
    @staticmethod
    def min_time(n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        e = [[] for _ in range(n)]
        for x in edges:
            e[x[0]].append(x[1])
            e[x[1]].append(x[0])
        vis = [False] * n
        rec = set()
        path = []

        def dfs(i):
            if hasApple[i]:
                for y in path:
                    if y not in rec:
                        rec.add(y)
            for x in e[i]:
                if not vis[x]:
                    vis[x] = True
                    path.append(x)
                    dfs(x)
                    path.pop()
                    vis[x] = False

        rec.add(0)
        vis[0] = True
        path.append(0)
        dfs(0)
        return (len(rec) - 1) * 2


if __name__ == '__main__':
    test_cases = [
        (7, [[0, 1], [0, 2], [1, 4], [1, 5], [2, 3], [2, 6]], [False, False, True, False, True, True, False]),
        (7, [[0, 1], [0, 2], [1, 4], [1, 5], [2, 3], [2, 6]], [False, False, True, False, False, True, False]),
        (7, [[0, 1], [0, 2], [1, 4], [1, 5], [2, 3], [2, 6]], [False, False, False, False, False, False, False]),
        (4, [[0, 2], [0, 3], [1, 2]], [False, True, False, False])
    ]
    for tc in test_cases:
        print(Solution.min_time(*tc))
