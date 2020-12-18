"""
  @Author       : liujianhan
  @Date         : 2020/12/16 10:03
  @Project      : leetcode_in_python
  @FileName     : 836.矩形重叠.py
  @Description  : 矩形以列表 [x1, y1, x2, y2] 的形式表示，其中 (x1, y1) 为左下角的坐标，(x2, y2) 是右上角的坐标。
    矩形的上下边平行于 x 轴，左右边平行于 y 轴。
    如果相交的面积为 正 ，则称两矩形重叠。需要明确的是，只在角或边接触的两个矩形不构成重叠。
    给出两个矩形 rec1 和 rec2 。如果它们重叠，返回 true；否则，返回 false 。
     
    示例 1：
    输入：rec1 = [0,0,2,2], rec2 = [1,1,3,3]
    输出：true

    示例 2：
    输入：rec1 = [0,0,1,1], rec2 = [1,0,2,1]
    输出：false

    示例 3：
    输入：rec1 = [0,0,1,1], rec2 = [2,2,3,3]
    输出：false

    提示：

    rect1.length == 4
    rect2.length == 4
    -109 <= rec1[i], rec2[i] <= 109
    rec1[0] <= rec1[2] 且 rec1[1] <= rec1[3]
    rec2[0] <= rec2[2] 且 rec2[1] <= rec2[3]
"""
from typing import List


class Solution:
    # 44ms, 14.7MB
    @staticmethod
    def is_rectangle_overlap(rec1: List[int], rec2: List[int]) -> bool:
        def is_line_overlap(x1, x2, a1, a2):
            tmp = [x1, x2, a1, a2]
            x_diff = x2 - x1
            a_diff = a2 - a1
            x_length = max(tmp) - min(tmp)
            return True if x_diff + a_diff > x_length else False

        x1, y1, x2, y2 = rec1
        a1, b1, a2, b2 = rec2
        x_overlap = is_line_overlap(x1, x2, a1, a2)
        y_overlap = is_line_overlap(y1, y2, b1, b2)

        return x_overlap and y_overlap

    # 32ms, 14.8MB
    @staticmethod
    def is_rectangle_overlap_v2(rec1: List[int], rec2: List[int]) -> bool:
        def intersect(p_left, p_right, q_left, q_right):
            return min(p_right, q_right) > max(p_left, q_left)

        return (intersect(rec1[0], rec1[2], rec2[0], rec2[2]) and
                intersect(rec1[1], rec1[3], rec2[1], rec2[3]))


if __name__ == '__main__':
    test_cases = [
        ([0, 0, 2, 2], [1, 1, 3, 3]),
        ([0, 0, 1, 1], [1, 0, 2, 1]),
        ([0, 0, 1, 1], [2, 2, 3, 3])
    ]
    for tc in test_cases:
        print(Solution.is_rectangle_overlap(*tc))
        print(Solution.is_rectangle_overlap_v2(*tc))
