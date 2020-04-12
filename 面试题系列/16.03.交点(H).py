"""
  @Author       : Liujianhan
  @Date         : 20/4/12 12:41
  @FileName     : 16.03.交点(H).py
  @ProjectName  : leetcode_in_python
  @Description  : 给定两条线段（表示为起点start = {X1, Y1}和终点end = {X2, Y2}），如果它们有交点，请计算其交点，没有交点则返回空值。
    要求浮点型误差不超过10^-6。若有多个交点（线段重叠）则返回 X 值最小的点，X 坐标相同则返回 Y 值最小的点。
    示例 1：

    输入：
    line1 = {0, 0}, {1, 0}
    line2 = {1, 1}, {0, -1}
    输出： {0.5, 0}
    示例 2：

    输入：
    line1 = {0, 0}, {3, 3}
    line2 = {1, 1}, {2, 2}
    输出： {1, 1}
    示例 3：

    输入：
    line1 = {0, 0}, {1, 1}
    line2 = {1, 0}, {2, 1}
    输出： {}，两条线段没有交点
    提示：

    坐标绝对值不会超过 2^7
    输入的坐标均是有效的二维坐标
 """
from typing import List


class Solution:
    # 52ms, 13.7MB
    @classmethod
    def intersection(cls, start1: List[int], end1: List[int], start2: List[int], end2: List[int]) -> List[float]:
        # 判断 (xk, yk) 是否在「线段」(x1, y1)~(x2, y2) 上
        # 这里的前提是 (xk, yk) 一定在「直线」(x1, y1)~(x2, y2) 上
        def inside(x1, y1, x2, y2, xk, yk):
            # 若与 x 轴平行，只需要判断 x 的部分
            # 若与 y 轴平行，只需要判断 y 的部分
            # 若为普通线段，则都要判断
            return (x1 == x2 or min(x1, x2) <= xk <= max(x1, x2)) and (y1 == y2 or min(y1, y2) <= yk <= max(y1, y2))

        def update(ans, xk, yk):
            # 将一个交点与当前 ans 中的结果进行比较
            # 若更优则替换
            return [xk, yk] if not ans or [xk, yk] < ans else ans

        x1, y1 = start1
        x2, y2 = end1
        x3, y3 = start2
        x4, y4 = end2

        ans = list()
        # 判断 (x1, y1)~(x2, y2) 和 (x3, y3)~(x4, y3) 是否平行
        if (y4 - y3) * (x2 - x1) == (y2 - y1) * (x4 - x3):
            # 若平行，则判断 (x3, y3) 是否在「直线」(x1, y1)~(x2, y2) 上
            if (y2 - y1) * (x3 - x1) == (y3 - y1) * (x2 - x1):
                # 判断 (x3, y3) 是否在「线段」(x1, y1)~(x2, y2) 上
                if inside(x1, y1, x2, y2, x3, y3):
                    ans = update(ans, x3, y3)
                # 判断 (x4, y4) 是否在「线段」(x1, y1)~(x2, y2) 上
                if inside(x1, y1, x2, y2, x4, y4):
                    ans = update(ans, x4, y4)
                # 判断 (x1, y1) 是否在「线段」(x3, y3)~(x4, y4) 上
                if inside(x3, y3, x4, y4, x1, y1):
                    ans = update(ans, x1, y1)
                # 判断 (x2, y2) 是否在「线段」(x3, y3)~(x4, y4) 上
                if inside(x3, y3, x4, y4, x2, y2):
                    ans = update(ans, x2, y2)
            # 在平行时，其余的所有情况都不会有交点
        else:
            # 联立方程得到 t1 和 t2 的值
            t1 = (x3 * (y4 - y3) + y1 * (x4 - x3) - y3 * (x4 - x3) - x1 * (y4 - y3)) / (
                        (x2 - x1) * (y4 - y3) - (x4 - x3) * (y2 - y1))
            t2 = (x1 * (y2 - y1) + y3 * (x2 - x1) - y1 * (x2 - x1) - x3 * (y2 - y1)) / (
                        (x4 - x3) * (y2 - y1) - (x2 - x1) * (y4 - y3))
            # 判断 t1 和 t2 是否均在 [0, 1] 之间
            if 0.0 <= t1 <= 1.0 and 0.0 <= t2 <= 1.0:
                ans = [x1 + t1 * (x2 - x1), y1 + t1 * (y2 - y1)]

        return ans


if __name__ == '__main__':
    test_cases = [
        ([0, 0], [1, 0], [1, 1], [0, -1]),
        ([0, 0], [3, 3], [1, 1], [2, 2]),
        ([0, 0], [1, 1], [1, 0], [2, 1])
    ]
    for tc in test_cases:
        print(Solution.intersection(*tc))
