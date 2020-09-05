"""
  @Author       : liujianhan
  @Date         : 2020/9/5 19:49
  @Project      : leetcode_in_python
  @FileName     : 310.最小高度树(M).py
  @Description  : 对于一个具有树特征的无向图，我们可选择任何一个节点作为根。图因此可以成为树，在所有可能的树中，具有最小高度的树被称为最小高度树。给出这样的一个图，写出一个函数找到所有的最小高度树并返回他们的根节点。
    格式
    该图包含 n 个节点，标记为 0 到 n - 1。给定数字 n 和一个无向边 edges 列表（每一个边都是一对标签）。
    你可以假设没有重复的边会出现在 edges 中。由于所有的边都是无向边， [0, 1]和 [1, 0] 是相同的，因此不会同时出现在 edges 里。
    示例 1:
    输入: n = 4, edges = [[1, 0], [1, 2], [1, 3]]

            0
            |
            1
           / \
          2   3

    输出: [1]
    示例 2:
    输入: n = 6, edges = [[0, 3], [1, 3], [2, 3], [4, 3], [5, 4]]

         0  1  2
          \ | /
            3
            |
            4
            |
            5

    输出: [3, 4]
    说明:

     根据树的定义，树是一个无向图，其中任何两个顶点只通过一条路径连接。 换句话说，一个任何没有简单环路的连通图都是一棵树。
    树的高度是指根节点和叶子节点之间最长向下路径上边的数量。
"""
import collections
from typing import List


class Solution:
    # 116ms, 18.6MB
    @staticmethod
    def find_min_height_trees(n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]
        e = collections.defaultdict(set)  # 字典初始化为集合
        for i, j in edges:
            e[i] |= {j}  # 把边哈希化，方便调用
            e[j] |= {i}
        q = {i for i in e if len(e[i]) == 1}  # 建立初始宽搜队列，长度为1时代表只连接一个点
        while n > 2:
            t = set()  # 临时队列
            for i in q:
                j = e[i].pop()  # 把连接点取出
                e[j] -= {i}  # 连接是双向的，所以要删除关系
                if len(e[j]) == 1:  # 更新后，如果长度为1时则加入下一个轮队列
                    t |= {j}
                n -= 1  # 删除计数
            q = t
        return list(q)

    # 88ms, 18.4MB
    @staticmethod
    def find_min_height_trees_v2(n: int, edges: List[List[int]]) -> List[int]:
        graph = collections.defaultdict(set)
        for p, q in edges:
            graph[p].add(q)
            graph[q].add(p)

        nodes = []
        for i in range(n):
            if len(graph[i]) < 2:
                nodes.append(i)

        while True:
            temp = []
            for i in nodes:
                for j in graph[i]:
                    graph[j].remove(i)
                    if len(graph[j]) == 1:
                        temp.append(j)
            if not temp:
                return nodes
            nodes = temp


if __name__ == '__main__':
    test_cases = [
        (4, [[1, 0], [1, 2], [1, 3]]),
        (6, [[0, 3], [1, 3], [2, 3], [4, 3], [5, 4]])
    ]
    for tc in test_cases:
        print(Solution.find_min_height_trees(*tc))
        print(Solution.find_min_height_trees_v2(*tc))
