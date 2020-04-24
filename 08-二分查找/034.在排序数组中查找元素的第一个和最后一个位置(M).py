"""
  @Author       : Liujianhan
  @Date         : 20/4/24 23:25
  @FileName     : 034.在排序数组中查找元素的第一个和最后一个位置(M).py
  @ProjectName  : leetcode_in_python
  @Description  : 给定一个按照升序排列的整数数组 nums，和一个目标值 target。找出给定目标值在数组中的开始位置和结束位置。
    你的算法时间复杂度必须是 O(log n) 级别。
    如果数组中不存在目标值，返回 [-1, -1]。
    示例 1:
    输入: nums = [5,7,7,8,8,10], target = 8
    输出: [3,4]
    示例 2:
    输入: nums = [5,7,7,8,8,10], target = 6
    输出: [-1,-1]
 """
from typing import List


class Solution:
    # 36ms, 14.7MB
    @classmethod
    def search_range(cls, nums: List[int], target: int) -> List[int]:
        """线性扫描"""
        for i in range(len(nums)):
            if nums[i] == target:
                left_idx = i
                break
        else:
            return [-1, -1]

        # find the index of the rightmost appearance of `target` (by reverse
        # iteration). it is guaranteed to appear.
        for j in range(len(nums) - 1, -1, -1):
            if nums[j] == target:
                right_idx = j
                break

        return [left_idx, right_idx]

    @classmethod
    def extreme_insertion_index(cls, nums: List[int], target: int, left: bool):
        lo = 0
        hi = len(nums)

        while lo < hi:
            mid = (lo + hi) // 2
            if nums[mid] > target or (left and target == nums[mid]):
                hi = mid
            else:
                lo = mid + 1

        return lo

    # 64ms, 14.5MB
    def search_range_v2(self, nums: List[int], target: int):
        left_idx = self.extreme_insertion_index(nums, target, True)
        # assert that `left_idx` is within the array bounds and that `target`
        # is actually in `nums`.
        if left_idx == len(nums) or nums[left_idx] != target:
            return [-1, -1]

        return [left_idx, self.extreme_insertion_index(nums, target, False) - 1]


if __name__ == '__main__':
    test_cases = [
        ([5, 7, 7, 8, 8, 10], 8),
        ([5, 7, 7, 8, 8, 10], 6)
    ]
    for tc in test_cases:
        print(Solution.search_range(*tc))
        print(Solution().search_range_v2(*tc))
