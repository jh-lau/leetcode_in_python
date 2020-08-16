"""
  @Author       : liujianhan
  @Date         : 2020/5/19 上午10:00
  @Project      : leetcode_in_python
  @FileName     : 153.寻找旋转排序数组中的最小值(M).py
  @Description  : 假设按照升序排序的数组在预先未知的某个点上进行了旋转。
    ( 例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2] )。
    请找出其中最小的元素。
    你可以假设数组中不存在重复元素。
    示例 1:
    输入: [3,4,5,1,2]
    输出: 1
    示例 2:
    输入: [4,5,6,7,0,1,2]
    输出: 0
"""
from typing import List


class Solution:
    # 44ms, 13.8MB
    @classmethod
    def find_min(cls, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) >> 1
            if nums[mid] < nums[right]:
                right = mid
            else:
                left = mid + 1

        return nums[left]

    # 40ms, 13.9MB
    @classmethod
    def find_min(cls, nums: List[int]) -> int:
        return min(nums)


if __name__ == '__main__':
    test_cases = [
        [3, 4, 5, 1, 2],
        [4, 5, 6, 7, 0, 1, 2]
    ]
    for tc in test_cases:
        print(Solution.find_min(tc))
