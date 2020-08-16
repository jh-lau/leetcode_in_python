"""
  @Author       : liujianhan
  @Date         : 2020/5/21 上午10:27
  @Project      : leetcode_in_python
  @FileName     : 154.寻找旋转排序数组中的最小值II(H).py
  @Description  : 假设按照升序排序的数组在预先未知的某个点上进行了旋转。
    ( 例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2] )。
    请找出其中最小的元素。
    注意数组中可能存在重复的元素。
    示例 1：
    输入: [1,3,5]
    输出: 1
    示例 2：
    输入: [2,2,2,0,1]
    输出: 0
    说明：
    这道题是 寻找旋转排序数组中的最小值 的延伸题目。
    允许重复会影响算法的时间复杂度吗？会如何影响，为什么？
"""
from typing import List


class Solution:
    # 60ms, 13.7MB
    @classmethod
    def find_min(cls, nums: List[int]) -> int:
        return min(nums)

    # 48ms, 13.8MB
    @classmethod
    def find_min_v2(cls, nums: List[int]) -> int:
        start, end = 0, len(nums) - 1
        if end == 0:
            return nums[0]

        while start <= end:
            mid = (start + end) >> 1
            if nums[mid] < nums[mid - 1]:
                return nums[mid]
            if nums[start] > nums[end]:
                if nums[mid] >= nums[start]:
                    start = mid + 1
                else:
                    end = mid - 1
            else:
                end -= 1

        return nums[end]


if __name__ == '__main__':
    test_cases = [
        [1, 3, 5], [2, 2, 2, 0, 1]
    ]
    for tc in test_cases:
        print(Solution.find_min(tc))
        print(Solution.find_min_v2(tc))
