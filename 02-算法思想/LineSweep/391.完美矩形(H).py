"""
  @Author       : liujianhan
  @Date         : 2020/9/27 11:21
  @Project      : leetcode_in_python
  @FileName     : 391.完美矩形(H).py
  @Description  : 我们有 N 个与坐标轴对齐的矩形, 其中 N > 0, 判断它们是否能精确地覆盖一个矩形区域。
    每个矩形用左下角的点和右上角的点的坐标来表示。
    例如， 一个单位正方形可以表示为 [1,1,2,2]。 ( 左下角的点的坐标为 (1, 1) 以及右上角的点的坐标为 (2, 2) )。
    示例 1:

    rectangles = [
      [1,1,3,3],
      [3,1,4,2],
      [3,2,4,4],
      [1,3,2,4],
      [2,3,3,4]
    ]

    返回 true。5个矩形一起可以精确地覆盖一个矩形区域。

    示例 2:

    rectangles = [
      [1,1,2,3],
      [1,3,2,4],
      [3,1,4,2],
      [3,2,4,4]
    ]

    返回 false。两个矩形之间有间隔，无法覆盖成一个矩形。
    示例 3:

    rectangles = [
      [1,1,3,3],
      [3,1,4,2],
      [1,3,2,4],
      [3,2,4,4]
    ]

    返回 false。图形顶端留有间隔，无法覆盖成一个矩形。
    示例 4:

    rectangles = [
      [1,1,3,3],
      [3,1,4,2],
      [1,3,2,4],
      [2,2,4,4]
    ]

    返回 false。因为中间有相交区域，虽然形成了矩形，但不是精确覆盖。
    思路：
    把每个子矩形的面积累加，四个坐标放进一个vector，然后sort一下，相同的坐标消去。
    最后剩下4个出现奇数次的点，且这个四个点围成的矩形面积等于子矩形面积和，则为true
"""
from typing import List


class Solution:
    # 464ms, 20.2MB
    @staticmethod
    def is_rectangle_cover(rectangles: List[List[int]]) -> bool:
        s = 0
        vector = set()

        for x1, y1, x2, y2 in rectangles:
            s += (x2 - x1) * (y2 - y1)  # 当前矩形区域的计算面积，并进行统计
            for ele in [(x1, y1), (x1, y2), (x2, y1), (x2, y2)]:
                if ele in vector:
                    vector.remove(ele)  # 如果有相同坐标就删除
                else:
                    vector.add(ele)  # 新的坐标就添加

        vector = list(vector)  # 转成列表进行排序
        vector.sort()

        if len(vector) != 4:  # 如果不是四个坐标说明有缺少区域
            return False

        x1, y1 = vector[0]
        x2, y2 = vector[-1]
        new_s = (x2 - x1) * (y2 - y1)  # 通过排序好的坐标，取左下角和右上角的坐标，计算总面积

        if new_s == s:
            return True  # 面积相同则精准覆盖
        else:
            return False


if __name__ == '__main__':
    test_cases = [
        [
            [1, 1, 3, 3],
            [3, 1, 4, 2],
            [3, 2, 4, 4],
            [1, 3, 2, 4],
            [2, 3, 3, 4]
        ],
        [
            [1, 1, 2, 3],
            [1, 3, 2, 4],
            [3, 1, 4, 2],
            [3, 2, 4, 4]
        ],
        [
            [1, 1, 3, 3],
            [3, 1, 4, 2],
            [1, 3, 2, 4],
            [3, 2, 4, 4]
        ],
        [
            [1, 1, 3, 3],
            [3, 1, 4, 2],
            [1, 3, 2, 4],
            [2, 2, 4, 4]
        ]
    ]
    for tc in test_cases:
        print(Solution.is_rectangle_cover(tc))
