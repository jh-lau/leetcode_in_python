"""
  @Author       : Liujianhan
  @Date         : 20/5/17 17:02
  @FileName     : 210.课程表II(M).py
  @ProjectName  : leetcode_in_python
  @Description  : 现在你总共有 n 门课需要选，记为 0 到 n-1。
    在选修某些课程之前需要一些先修课程。 例如，想要学习课程 0 ，你需要先完成课程 1 ，我们用一个匹配来表示他们: [0,1]
    给定课程总量以及它们的先决条件，返回你为了学完所有课程所安排的学习顺序。
    可能会有多个正确的顺序，你只要返回一种就可以了。如果不可能完成所有课程，返回一个空数组。

    示例 1:

    输入: 2, [[1,0]]
    输出: [0,1]
    解释: 总共有 2 门课程。要学习课程 1，你需要先完成课程 0。因此，正确的课程顺序为 [0,1] 。
    示例 2:

    输入: 4, [[1,0],[2,0],[3,1],[3,2]]
    输出: [0,1,2,3] or [0,2,1,3]
    解释: 总共有 4 门课程。要学习课程 3，你应该先完成课程 1 和课程 2。并且课程 1 和课程 2 都应该排在课程 0 之后。
         因此，一个正确的课程顺序是 [0,1,2,3] 。另一个正确的排序是 [0,2,1,3] 。
    说明:

    输入的先决条件是由边缘列表表示的图形，而不是邻接矩阵。详情请参见图的表示法。
    你可以假定输入的先决条件中没有重复的边。
    提示:

    这个问题相当于查找一个循环是否存在于有向图中。如果存在循环，则不存在拓扑排序，因此不可能选取所有课程进行学习。
    通过 DFS 进行拓扑排序 - 一个关于Coursera的精彩视频教程（21分钟），介绍拓扑排序的基本概念。
    拓扑排序也可以通过 BFS 完成。
 """
from collections import defaultdict, deque
from typing import List


class Solution:
    # 52ms, 16.5MB
    @classmethod
    def find_order(cls, num_courses: int, prerequisites: List[List[int]]) -> List[int]:
        """BFS"""
        edges = defaultdict(list)
        visited = [0] * num_courses
        result = list()
        invalid = False

        for info in prerequisites:
            edges[info[1]].append(info[0])

        def dfs(u: int):
            nonlocal invalid
            visited[u] = 1
            for v in edges[u]:
                if visited[v] == 0:
                    dfs(v)
                    if invalid:
                        return
                elif visited[v] == 1:
                    invalid = True
                    return
            visited[u] = 2
            result.append(u)

        for i in range(num_courses):
            if not invalid and not visited[i]:
                dfs(i)

        if invalid:
            return list()

        return result[::-1]

    # 60ms, 14.3MB
    @classmethod
    def find_order_v2(cls, num_courses: int, prerequisites: List[List[int]]) -> List[int]:
        """DFS"""
        edges = defaultdict(list)
        in_deg = [0] * num_courses
        result = list()

        for info in prerequisites:
            edges[info[1]].append(info[0])
            in_deg[info[0]] += 1

        q = deque([u for u in range(num_courses) if in_deg[u] == 0])

        while q:
            u = q.popleft()
            result.append(u)
            for v in edges[u]:
                in_deg[v] -= 1
                if in_deg[v] == 0:
                    q.append(v)

        if len(result) != num_courses:
            result = list()
        return result


if __name__ == '__main__':
    test_cases = [
        (2, [[1, 0]]),
        (4, [[1, 0], [2, 0], [3, 1], [3, 2]]),
    ]
    for tc in test_cases:
        print(Solution.find_order(*tc))
