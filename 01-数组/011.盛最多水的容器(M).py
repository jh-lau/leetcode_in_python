"""
  @Author       : liujianhan
  @Date         : 2020/4/18 上午10:24
  @Project      : leetcode_in_python
  @FileName     : 011.盛最多水的容器(M).py
  @Description  : 给你 n 个非负整数 a1，a2，...，an，每个数代表坐标中的一个点 (i, ai) 。在坐标内画 n 条垂直线，垂直线 i 的两个端点分别为 (i, ai) 和 (i, 0)。找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。
    说明：你不能倾斜容器，且 n 的值至少为 2。
    输入：[1,8,6,2,5,4,8,3,7]
    输出：49
"""
from typing import List


class Solution:
    # 84ms, 14.9MB
    @classmethod
    def max_area(cls, height: List[int]) -> int:
        """双指针"""
        left, right = 0, len(height) - 1
        ans = 0
        while left < right:
            area = min(height[left], height[right]) * (right - left)
            ans = max(ans, area)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return ans


if __name__ == '__main__':
    test_cases = [
        [1, 8, 6, 2, 5, 4, 8, 3, 7]
    ]
    for tc in test_cases:
        print(Solution.max_area(tc))
