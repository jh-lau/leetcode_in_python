"""
  @Author       : Liujianhan
  @Date         : 20/6/7 11:39
  @FileName     : 209.长度最小的子数组(M).py
  @ProjectName  : leetcode_in_python
  @Description  : 给定一个含有 n 个正整数的数组和一个正整数 s ，找出该数组中满足其和 ≥ s 的长度最小的连续子数组，并返回其长度。如果不存在符合条件的连续子数组，返回 0。
    示例: 
    输入: s = 7, nums = [2,3,1,2,4,3]
    输出: 2
    解释: 子数组 [4,3] 是该条件下的长度最小的连续子数组。
    进阶:
    如果你已经完成了O(n) 时间复杂度的解法, 请尝试 O(n log n) 时间复杂度的解法。
 """
import bisect
from typing import List


class Solution:
    # 52ms, 15.2MB
    @classmethod
    def min_sub_array_len(cls, s: int, nums: List[int]) -> int:
        if not nums:
            return 0
        left = cur = 0
        res = float('inf')
        for right in range(len(nums)):
            cur += nums[right]
            while cur >= s:
                res = min(res, right - left + 1)
                cur -= nums[left]
                left += 1

        return res if res != float('inf') else 0

    # 72ms, 15.3MB
    @classmethod
    def min_sub_array_len_v2(cls, s: int, nums: List[int]) -> int:
        if not nums:
            return 0
        for i in range(1, len(nums)):
            nums[i] += nums[i - 1]
        if nums[-1] < s: return 0
        res = float("inf")
        nums = [0] + nums
        for i in range(1, len(nums)):
            if nums[i] - s >= 0:
                loc = bisect.bisect_left(nums, nums[i] - s)
                if nums[i] - nums[loc] >= s:
                    res = min(res, i - loc)
                    continue
                if loc > 0:
                    res = min(res, i - loc + 1)
        return res


if __name__ == '__main__':
    test_cases = [
        (7, [2, 3, 1, 2, 4, 3]),
        (8, [2, 3, 1, 2, 4, 3]),
    ]
    for tc in test_cases:
        print(Solution.min_sub_array_len(*tc))
        print(Solution.min_sub_array_len_v2(*tc))
