"""
  @Author       : liujianhan
  @Date         : 2020/7/29 上午11:27
  @Project      : leetcode_in_python
  @FileName     : 013.寻宝(H).py
  @Description  : 我们得到了一副藏宝图，藏宝图显示，在一个迷宫中存在着未被世人发现的宝藏。
    迷宫是一个二维矩阵，用一个字符串数组表示。它标识了唯一的入口（用 'S' 表示），和唯一的宝藏地点（用 'T' 表示）。
    但是，宝藏被一些隐蔽的机关保护了起来。在地图上有若干个机关点（用 'M' 表示），只有所有机关均被触发，才可以拿到宝藏。
    要保持机关的触发，需要把一个重石放在上面。迷宫中有若干个石堆（用 'O' 表示），每个石堆都有无限个足够触发机关的重石。
    但是由于石头太重，我们一次只能搬一个石头到指定地点。迷宫中同样有一些墙壁（用 '#' 表示），我们不能走入墙壁。
    剩余的都是可随意通行的点（用 '.' 表示）。石堆、机关、起点和终点（无论是否能拿到宝藏）也是可以通行的。
    我们每步可以选择向上/向下/向左/向右移动一格，并且不能移出迷宫。搬起石头和放下石头不算步数。
    那么，从起点开始，我们最少需要多少步才能最后拿到宝藏呢？如果无法拿到宝藏，返回 -1 。

    示例 1：

    输入： ["S#O", "M..", "M.T"]

    输出：16

    解释：最优路线为： S->O, cost = 4, 去搬石头 O->第二行的M, cost = 3, M机关触发 第二行的M->O, cost = 3, 我们需要继续回去 O 搬石头。 O->第三行的M, cost = 4, 此时所有机关均触发 第三行的M->T, cost = 2，去T点拿宝藏。 总步数为16。

    示例 2：

    输入： ["S#O", "M.#", "M.T"]

    输出：-1

    解释：我们无法搬到石头触发机关

    示例 3：

    输入： ["S#O", "M.T", "M.."]

    输出：17

    解释：注意终点也是可以通行的。

    限制：

    1 <= maze.length <= 100
    1 <= maze[i].length <= 100
    maze[i].length == maze[j].length
    S 和 T 有且只有一个
    0 <= M的数量 <= 16
    0 <= O的数量 <= 40，题目保证当迷宫中存在 M 时，一定存在至少一个 O 。
"""
from collections import deque
from typing import List


class Solution:
    # 4792ms, 46.9MB
    @staticmethod
    def minimal_steps(maze: List[str]) -> int:
        def neighbors(i, j):
            for ni, nj in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                if 0 <= ni < M and 0 <= nj < N:
                    yield ni, nj

        def calc_dist(i, j):
            dist = [[float('inf')] * N for _ in range(M)]
            dist[i][j] = 0
            q = deque([(i, j, 0)])
            while q:
                x, y, d = q.popleft()
                for ni, nj in neighbors(x, y):
                    if maze[ni][nj] != '#' and d + 1 < dist[ni][nj]:
                        dist[ni][nj] = d + 1
                        q.append((ni, nj, d + 1))
            return dist

        M, N = len(maze), len(maze[0])
        stones = []
        machines = []
        for i in range(M):
            for j in range(N):
                ch = maze[i][j]
                if ch == 'S':
                    start = (i, j)
                elif ch == 'T':
                    end = (i, j)
                elif ch == 'O':
                    stones.append((i, j))
                elif ch == 'M':
                    machines.append((i, j))

        # regard start as a normal machine
        machines = [start] + machines
        dists = [calc_dist(i, j) for i, j in machines]
        end_dist = calc_dist(*end)

        machine_num = len(machines)

        # shortest path between machines
        edges = [[float('inf')] * machine_num for _ in range(machine_num)]
        for cur, cur_md in enumerate(dists):
            for nxt in range(cur + 1, machine_num):
                nxt_md = dists[nxt]
                ci, cj = machines[cur]
                ni, nj = machines[nxt]

                nd = float('inf')
                for si, sj in stones:
                    nd = min(nd, cur_md[si][sj] + nxt_md[si][sj])

                edges[cur][nxt] = edges[nxt][cur] = nd

        state_num = 1 << machine_num
        dp = [[float('inf')] * state_num for _ in range(machine_num)]
        dp[0][1] = 0

        for s in range(1, state_num):
            for cur in range(machine_num):
                if dp[cur][s] == float('inf'):
                    continue
                for nxt in range(machine_num):
                    if s >> nxt & 1:
                        continue
                    dp[nxt][s | 1 << nxt] = min(dp[nxt][s | 1 << nxt],
                                                dp[cur][s] + edges[cur][nxt])

        ans = min(end_dist[i][j] + dp[cur][state_num - 1]
                  for cur, (i, j) in enumerate(machines))
        return -1 if ans == float('inf') else ans


if __name__ == '__main__':
    test_cases = [
        ["S#O", "M..", "M.T"],
        ["S#O", "M.#", "M.T"],
        ["S#O", "M.T", "M.."]
    ]
    for tc in test_cases:
        print(Solution.minimal_steps(tc))
