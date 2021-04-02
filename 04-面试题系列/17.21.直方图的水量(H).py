"""
  @Author       : liujianhan
  @Date         : 21/4/2 9:27
  @Project      : leetcode_in_python
  @FileName     : 17.21.直方图的水量(H).py
  @Description  : Placeholder
"""
from typing import List


class Solution:
    # 48ms, 15MB
    @staticmethod
    def trap(height: List[int]) -> int:
        ans = 0
        left, right = 0, len(height) - 1
        leftMax = rightMax = 0

        while left < right:
            leftMax = max(leftMax, height[left])
            rightMax = max(rightMax, height[right])
            if height[left] < height[right]:
                ans += leftMax - height[left]
                left += 1
            else:
                ans += rightMax - height[right]
                right -= 1

        return ans


if __name__ == '__main__':
    test_cases = [
        [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    ]
    for test_case in test_cases:
        print(Solution.trap(test_case))
