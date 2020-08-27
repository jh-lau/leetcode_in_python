"""
  @Author       : liujianhan
  @Date         : 2020/8/27 10:34
  @Project      : leetcode_in_python
  @FileName     : 332.重新安排行程(M).py
  @Description  : 给定一个机票的字符串二维数组 [from, to]，子数组中的两个成员分别表示飞机出发和降落的机场地点，对该行程进行重新规划排序。所有这些机票都属于一个从 JFK（肯尼迪国际机场）出发的先生，所以该行程必须从 JFK 开始。

说明:

如果存在多种有效的行程，你可以按字符自然排序返回最小的行程组合。例如，行程 ["JFK", "LGA"] 与 ["JFK", "LGB"] 相比就更小，排序更靠前
所有的机场都用三个大写字母表示（机场代码）。
假定所有机票至少存在一种合理的行程。
示例 1:

输入: [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
输出: ["JFK", "MUC", "LHR", "SFO", "SJC"]
示例 2:

输入: [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
输出: ["JFK","ATL","JFK","SFO","ATL","SFO"]
解释: 另一种有效的行程是 ["JFK","SFO","ATL","JFK","ATL","SFO"]。但是它自然排序更大更靠后。
"""
import collections
from typing import List


class Solution:
    # 56ms, 14.1MB
    @staticmethod
    def find_itinerary(tickets: List[List[str]]) -> List[str]:
        d = collections.defaultdict(list)  # 邻接表
        for f, t in tickets:
            d[f] += [t]  # 路径存进邻接表
        for f in d:
            d[f].sort()  # 邻接表排序
        ans = []

        def dfs(f):  # 深搜函数
            while d[f]:
                dfs(d[f].pop(0))  # 路径检索
            ans.insert(0, f)  # 放在最前

        dfs('JFK')
        return ans


if __name__ == '__main__':
    test_cases = [
        [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]],
        [["JFK", "SFO"], ["JFK", "ATL"], ["SFO", "ATL"], ["ATL", "JFK"], ["ATL", "SFO"]]
    ]
    for tc in test_cases:
        print(Solution.find_itinerary(tc))
