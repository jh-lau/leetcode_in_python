"""
  @Author       : liujianhan
  @Date         : 2020/11/9 10:13
  @Project      : leetcode_in_python
  @FileName     : 973.最接近原点的K个点.py
  @Description  : 我们有一个由平面上的点组成的列表 points。需要从中找出 K 个距离原点 (0, 0) 最近的点。
    （这里，平面上两点之间的距离是欧几里德距离。）
    你可以按任何顺序返回答案。除了点坐标的顺序之外，答案确保是唯一的。

    示例 1：

    输入：points = [[1,3],[-2,2]], K = 1
    输出：[[-2,2]]
    解释：
    (1, 3) 和原点之间的距离为 sqrt(10)，
    (-2, 2) 和原点之间的距离为 sqrt(8)，
    由于 sqrt(8) < sqrt(10)，(-2, 2) 离原点更近。
    我们只需要距离原点最近的 K = 1 个点，所以答案就是 [[-2,2]]。
    示例 2：

    输入：points = [[3,3],[5,-1],[-2,4]], K = 2
    输出：[[3,3],[-2,4]]
    （答案 [[-2,4],[3,3]] 也会被接受。）
     

    提示：

    1 <= K <= points.length <= 10000
    -10000 < points[i][0] < 10000
    -10000 < points[i][1] < 10000
"""
from typing import List
import heapq


class Solution:
    # 800ms, 19MB
    @staticmethod
    def k_closest(points: List[List[int]], K: int) -> List[List[int]]:
        result = []
        for point in points:
            dis = point[0] ** 2 + point[1] ** 2
            heapq.heappush(result, (dis, point))

        return [s[1] for s in heapq.nsmallest(K, result)]


if __name__ == '__main__':
    test_cases = [
        ([[1, 3], [-2, 2]], 1),
        ([[3, 3], [5, -1], [-2, 4]], 2),
    ]
    for tc in test_cases:
        print(Solution.k_closest(*tc))
