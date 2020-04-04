"""
  @Author       : Liujianhan
  @Date         : 20/4/4 14:25
  @FileName     : 42.接雨水(H).py
  @ProjectName  : leetcode_in_python
  @Description  : 给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。
 """
from typing import List


class Solution:
    # 56ms, 14.1MB
    @classmethod
    def trap(cls, height: List[int]) -> int:
        """动态规划O(N), O(N)"""
        if not height:
            return 0
        length = len(height)
        max_left = [0] * length
        max_right = [0] * length
        ans = 0
        max_left[0] = height[0]
        max_right[length-1] = height[length-1]

        for i in range(1, length):
            max_left[i] = max(height[i], max_left[i-1])
        for j in range(length-2, -1, -1):
            max_right[j] = max(height[j], max_right[j+1])
        for k in range(length):
            if min(max_left[k], max_right[k]) > height[k]:
                ans += min(max_left[k], max_right[k]) - height[k]

        return ans

    # 72ms, 14.2MB
    @classmethod
    def trap_v2(cls, height: List[int]) -> int:
        """双指针O(N), O(1)"""
        if not height:
            return 0
        length = len(height)
        left, right = 0, length-1
        max_left, max_right = height[0], height[length-1]
        ans = 0

        while left < right:
            max_left = max(height[left], max_left)
            max_right = max(height[right], max_right)
            if max_left < max_right:
                ans += max_left - height[left]
                left += 1
            else:
                ans += max_right - height[right]
                right -= 1

        return ans


if __name__ == '__main__':
    test_cases = [
        [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    ]
    for tc in test_cases:
        print(Solution.trap(tc))
        print(Solution.trap_v2(tc))
