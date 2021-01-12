"""
  @Author       : liujianhan
  @Date         : 2021/1/12 9:32
  @Project      : leetcode_in_python
  @FileName     : 1203.项目管理(H).py
  @Description  : 公司共有 n 个项目和  m 个小组，每个项目要不无人接手，要不就由 m 个小组之一负责。
    group[i] 表示第 i 个项目所属的小组，如果这个项目目前无人接手，那么 group[i] 就等于 -1。（项目和小组都是从零开始编号的）
    小组可能存在没有接手任何项目的情况。
    请你帮忙按要求安排这些项目的进度，并返回排序后的项目列表：
    同一小组的项目，排序后在列表中彼此相邻。
    项目之间存在一定的依赖关系，我们用一个列表 beforeItems 来表示，其中 beforeItems[i] 表示在进行第 i 个项目前（位于第 i 个项目左侧）
    应该完成的所有项目。
    如果存在多个解决方案，只需要返回其中任意一个即可。如果没有合适的解决方案，就请返回一个 空列表 。

    示例 1：
    输入：n = 8, m = 2, group = [-1,-1,1,0,0,1,0,-1], beforeItems = [[],[6],[5],[6],[3,6],[],[],[]]
    输出：[6,3,4,1,5,2,0,7]

    示例 2：
    输入：n = 8, m = 2, group = [-1,-1,1,0,0,1,0,-1], beforeItems = [[],[6],[5],[6],[3],[],[4],[]]
    输出：[]
    解释：与示例 1 大致相同，但是在排序后的列表中，4 必须放在 6 的前面。

    提示：

    1 <= m <= n <= 3 * 104
    group.length == beforeItems.length == n
    -1 <= group[i] <= m - 1
    0 <= beforeItems[i].length <= n - 1
    0 <= beforeItems[i][j] <= n - 1
    i != beforeItems[i][j]
    beforeItems[i] 不含重复元素
"""
from typing import List


class Solution:
    # 180ms, 28.1MB
    @staticmethod
    def sort_items(n: int, m: int, group: List[int], beforeItems: List[List[int]]) -> List[int]:
        dep = [0] * n
        group_dep = [0] * m
        other_queue = []
        group_queue = [[] for _ in range(m)]
        queue_queue = []
        dependedBy = [[] for _ in range(n)]
        for i, l in enumerate(beforeItems):
            dep[i] = len(l)
            gi = group[i]
            for j in l:
                dependedBy[j].append(i)
                if gi != -1 and group[j] != gi:
                    group_dep[gi] += 1
            if not l:
                (group_queue[gi] if gi != -1 else other_queue).append(i)
        for i, gd in enumerate(group_dep):
            if not gd:
                queue_queue.append(group_queue[i])
        result = []
        while True:
            if queue_queue:
                current_queue = queue_queue.pop()
            elif other_queue:
                current_queue = other_queue
            else:
                if len(result) < n:
                    return []
                else:
                    return result
            while current_queue:
                p = current_queue.pop()
                result.append(p)
                gp = group[p]
                for i in dependedBy[p]:
                    gi = group[i]
                    dep[i] -= 1
                    if not dep[i]:
                        (group_queue[gi] if gi != -1 else other_queue).append(i)
                    if gi != -1 and gi != gp:
                        group_dep[gi] -= 1
                        if not group_dep[gi]:
                            queue_queue.append(group_queue[gi])


if __name__ == '__main__':
    test_cases = [
        (8, 2, [-1, -1, 1, 0, 0, 1, 0, -1], [[], [6], [5], [6], [3, 6], [], [], []]),
        (8, 2, [-1, -1, 1, 0, 0, 1, 0, -1], [[], [6], [5], [6], [3], [], [4], []]),
    ]
    for tc in test_cases:
        print(Solution.sort_items(*tc))
