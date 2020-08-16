"""
  @Author       : Liujianhan
  @Date         : 20/5/5 16:07
  @FileName     : 084.柱状图中的最大矩形(H).py
  @ProjectName  : leetcode_in_python
  @Description  : 给定 n 个非负整数，用来表示柱状图中各个柱子的高度。每个柱子彼此相邻，且宽度为 1 。
    求在该柱状图中，能够勾勒出来的矩形的最大面积。
    以上是柱状图的示例，其中每个柱子的宽度为 1，给定的高度为 [2,1,5,6,2,3]。
    图中阴影部分为所能勾勒出的最大矩形面积，其面积为 10 个单位。
    示例:
    输入: [2,1,5,6,2,3]
    输出: 10
 """
from typing import List


class Solution:
    # 56ms, 15.7MB
    @classmethod
    def largest_rectangle_area(cls, heights: List[int]) -> int:
        stack = []
        heights = [0] + heights + [0]
        res = 0
        for i in range(len(heights)):
            while stack and heights[stack[-1]] > heights[i]:
                tmp = stack.pop()
                res = max(res, (i - stack[-1] - 1) * heights[tmp])
            stack.append(i)

        return res


if __name__ == '__main__':
    test_cases = [
        [2, 1, 5, 6, 2, 3]
    ]
    for tc in test_cases:
        print(Solution.largest_rectangle_area(tc))
