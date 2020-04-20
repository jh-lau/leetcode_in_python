"""
  @Author       : liujianhan
  @Date         : 2020/4/20 下午1:59
  @Project      : leetcode_in_python
  @FileName     : 207.课程表(M).py
  @Description  : 你这个学期必须选修 numCourse 门课程，记为 0 到 numCourse-1 。
    在选修某些课程之前需要一些先修课程。 例如，想要学习课程 0 ，你需要先完成课程 1 ，我们用一个匹配来表示他们：[0,1]
    给定课程总量以及它们的先决条件，请你判断是否可能完成所有课程的学习？
    示例 1:
    输入: 2, [[1,0]] 
    输出: true
    解释: 总共有 2 门课程。学习课程 1 之前，你需要完成课程 0。所以这是可能的。
    示例 2:
    输入: 2, [[1,0],[0,1]]
    输出: false
    解释: 总共有 2 门课程。学习课程 1 之前，你需要先完成​课程 0；并且学习课程 0 之前，你还应先完成课程 1。这是不可能的。
    提示：
    
    输入的先决条件是由 边缘列表 表示的图形，而不是 邻接矩阵 。详情请参见图的表示法。
    你可以假定输入的先决条件中没有重复的边。
    1 <= numCourses <= 10^5
"""
from collections import deque
from typing import List


class Solution:
    # 48ms, 14.4MB
    @classmethod
    def can_finish(cls, num_courses: int, prerequisites: List[List[int]]) -> bool:
        in_degrees = [0 for _ in range(num_courses)]
        adjacency = [[] for _ in range(num_courses)]
        queue = deque()
        for cur, pre in prerequisites:
            in_degrees[cur] += 1
            adjacency[pre].append(cur)
        for i in range(len(in_degrees)):
            if not in_degrees[i]:
                queue.append(i)
        while queue:
            pre = queue.popleft()
            num_courses -= 1
            for cur in adjacency[pre]:
                in_degrees[cur] -= 1
                if not in_degrees[cur]:
                    queue.append(cur)
        return not num_courses

    # 48ms, 16.1MB
    @classmethod
    def can_finish_v2(cls, num_courses: int, prerequisites: List[List[int]]) -> bool:
        def dfs(i, adjacency, flags):
            if flags[i] == -1: return True
            if flags[i] == 1: return False
            flags[i] = 1
            for j in adjacency[i]:
                if not dfs(j, adjacency, flags): return False
            flags[i] = -1
            return True

        adjacency = [[] for _ in range(num_courses)]
        flags = [0 for _ in range(num_courses)]
        for cur, pre in prerequisites:
            adjacency[pre].append(cur)
        for i in range(num_courses):
            if not dfs(i, adjacency, flags): return False
        return True


if __name__ == '__main__':
    test_cases = [
        (2, [[1, 0]]),
        (2, [[1, 0], [0, 1]])
    ]
    for tc in test_cases:
        print(Solution.can_finish(*tc))
        print(Solution.can_finish_v2(*tc))
