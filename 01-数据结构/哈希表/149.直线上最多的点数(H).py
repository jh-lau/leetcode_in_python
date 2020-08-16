"""
  @Author       : Liujianhan
  @Date         : 20/5/16 21:35
  @FileName     : 149.直线上最多的点数(H).py
  @ProjectName  : leetcode_in_python
  @Description  : 给定一个二维平面，平面上有 n 个点，求最多有多少个点在同一条直线上。
    示例 1:
    输入: [[1,1],[2,2],[3,3]]
    输出: 3
    示例 2:
    输入: [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
    输出: 4
 """
from collections import Counter
from decimal import Decimal
from typing import List


class Solution:
    # 128ms, 15.8MB
    @classmethod
    def max_points(cls, points: List[List[int]]) -> int:
        points = Counter([tuple(p) for p in points])
        points = [(k, points[k]) for k in points]
        n = len(points)
        if n == 0:  return 0
        if n == 1:  return points[0][1]
        lines = {}
        for i in range(n - 1):
            for j in range(i + 1, n):
                x1, y1 = points[i][0]
                x2, y2 = points[j][0]
                n1, n2 = points[i][1], points[j][1]
                if x1 == x2:
                    k, b = 'inf', x1
                else:
                    k = Decimal(y2 - y1) / Decimal(x2 - x1)
                    b = y1 - k * x1
                if (k, b) not in lines:
                    lines[(k, b)] = [n1 + n2, i]
                elif i == lines[(k, b)][1]:
                    lines[(k, b)][0] += n2
        return max([v[0] for v in lines.values()])


if __name__ == '__main__':
    test_cases = [
        [[1, 1], [2, 2], [3, 3]],
        [[1, 1], [3, 2], [5, 3], [4, 1], [2, 3], [1, 4]],
        [[0, 0], [94911150, 94911151], [94911151, 94911152]]
    ]
    for tc in test_cases:
        print(Solution.max_points(tc))

