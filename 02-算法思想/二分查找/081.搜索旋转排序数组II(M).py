"""
  @Author       : Liujianhan
  @Date         : 20/5/5 15:53
  @FileName     : 081.搜索旋转排序数组II(M).py
  @ProjectName  : leetcode_in_python
  @Description  : 假设按照升序排序的数组在预先未知的某个点上进行了旋转。
    ( 例如，数组 [0,0,1,2,2,5,6] 可能变为 [2,5,6,0,0,1,2] )。
    编写一个函数来判断给定的目标值是否存在于数组中。若存在返回 true，否则返回 false。
    示例 1:
    输入: nums = [2,5,6,0,0,1,2], target = 0
    输出: true
    示例 2:
    输入: nums = [2,5,6,0,0,1,2], target = 3
    输出: false
    进阶:
    这是 搜索旋转排序数组 的延伸题目，本题中的 nums  可能包含重复元素。
    这会影响到程序的时间复杂度吗？会有怎样的影响，为什么？
 """
from typing import List


class Solution:
    # 40ms, 13.7MB
    @classmethod
    def search(cls, nums: List[int], target: int) -> bool:
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) >> 1
            if nums[mid] == target:
                return True
            if nums[mid] == nums[l] == nums[r]:
                l += 1
                r -= 1
            elif nums[mid] >= nums[l]:
                if nums[l] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1

        return False


if __name__ == '__main__':
    test_cases = [
        ([2, 5, 6, 0, 0, 1, 2], 0),
        ([2, 5, 6, 0, 0, 1, 2], 3)
    ]
    for tc in test_cases:
        print(Solution.search(*tc))
