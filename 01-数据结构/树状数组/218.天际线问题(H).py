"""
  @Author       : liujianhan
  @Date         : 2020/6/23 上午9:24
  @Project      : leetcode_in_python
  @FileName     : 218.天际线问题(H).py
  @Description  : 城市的天际线是从远处观看该城市中所有建筑物形成的轮廓的外部轮廓。现在，假设您获得了城市风光照片（图A）
  上显示的所有建筑物的位置和高度，请编写一个程序以输出由这些建筑物形成的天际线（图B）。
    每个建筑物的几何信息用三元组 [Li，Ri，Hi] 表示，其中 Li 和 Ri 分别是第 i 座建筑物左右边缘的 x 坐标，Hi 是其高度。
    可以保证 0 ≤ Li, Ri ≤ INT_MAX, 0 < Hi ≤ INT_MAX 和 Ri - Li > 0。您可以假设所有建筑物都是在绝对平坦且高度为 0 的表面上的完美矩形。
    例如，图A中所有建筑物的尺寸记录为：[ [2 9 10], [3 7 15], [5 12 12], [15 20 10], [19 24 8] ] 。
    输出是以 [ [x1,y1], [x2, y2], [x3, y3], ... ] 格式的“关键点”（图B中的红点）的列表，它们唯一地定义了天际线。
    关键点是水平线段的左端点。请注意，最右侧建筑物的最后一个关键点仅用于标记天际线的终点，并始终为零高度。
    此外，任何两个相邻建筑物之间的地面都应被视为天际线轮廓的一部分。
    例如，图B中的天际线应该表示为：[ [2 10], [3 15], [7 12], [12 0], [15 10], [20 8], [24, 0] ]。
    说明:
    任何输入列表中的建筑物数量保证在 [0, 10000] 范围内。
    输入列表已经按左 x 坐标 Li  进行升序排列。
    输出列表必须按 x 位排序。
    输出天际线中不得有连续的相同高度的水平线。例如 [...[2 3], [4 5], [7 5], [11 5], [12 7]...] 是不正确的答案；
    三条高度为 5 的线应该在最终输出中合并为一个：[...[2 3], [4 5], [12 7], ...]
"""
from typing import List


class Solution:
    # 68ms, 18.9MB
    @staticmethod
    def get_skyline(buildings: List[List[int]]) -> List[List[int]]:
        # 扫描线法：利用堆辅助
        import heapq
        # 记录每一个关键点
        points = sorted([(L, -H, R) for L, R, H in buildings] + [(R, 0, 0) for _, R, _ in buildings])
        res = [[0, 0]]  # 初始化楼的左边界为0，,高度为0
        heap = [[0, float('inf')]]  # 初始化最大楼高为0，右边界为∞
        for x, h, r in points:
            # 当扫描线到达堆中最高楼的右边界时，该楼从堆中删除
            while x >= heap[0][1]:
                heapq.heappop(heap)  # 让列表像堆那样操作
            # 将楼的信息加入堆中（不加入人为设置的边界）
            if h:
                heapq.heappush(heap, [h, r])
            # 若此时结果集中最后一栋楼高不等于堆中最大楼高，说明楼高改变，关键点出现
            if res[-1][1] != -heap[0][0]:
                res.append([x, -heap[0][0]])
        return res[1:]

    # 92ms, 16.3MB
    @classmethod
    def get_skyline_v2(cls, buildings: List[List[int]]) -> List[List[int]]:
        if not buildings: return []  # base case
        if len(buildings) == 1: return [[buildings[0][0], buildings[0][2]], [buildings[0][1], 0]]
        mid = len(buildings) // 2  # divide and conquer
        left = cls.get_skyline_v2(buildings[:mid])
        right = cls.get_skyline_v2(buildings[mid:])
        return cls.merge(left, right)

    @classmethod
    def merge(cls, left, right):
        res = []
        lheight, rheight = 0, 0  # 初始化建筑最大高度
        l, r = 0, 0  # 初始化建筑起始位置
        while l < len(left) and r < len(right):
            if left[l][0] < right[r][0]:
                curpoint = [left[l][0], max(left[l][1], rheight)]
                lheight = left[l][1]
                l += 1
            elif left[l][0] > right[r][0]:
                curpoint = [right[r][0], max(right[r][1], lheight)]
                rheight = right[r][1]
                r += 1
            else:
                curpoint = [right[r][0], max(left[l][1], right[r][1])]
                lheight = left[l][1]
                rheight = right[r][1]
                l += 1
                r += 1
            if not res or res[-1][1] != curpoint[1]:
                res.append(curpoint)
        res.extend(left[l:] or right[r:])
        return res


if __name__ == '__main__':
    tc = [[2, 9, 10],
          [3, 7, 15],
          [5, 12, 12],
          [15, 20, 10],
          [19, 24, 8]]
    print(Solution.get_skyline(tc))
    print(Solution.get_skyline_v2(tc))
