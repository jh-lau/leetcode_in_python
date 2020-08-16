"""
  @Author       : Liujianhan
  @Date         : 20/5/26 23:00
  @FileName     : 287.寻找重复数(M).py
  @ProjectName  : leetcode_in_python
  @Description  : 给定一个包含 n + 1 个整数的数组 nums，其数字都在 1 到 n 之间（包括 1 和 n），可知至少存在一个重复的整数。假设只有一个重复的整数，找出这个重复的数。
    示例 1:
    输入: [1,3,4,2,2]
    输出: 2
    示例 2:
    输入: [3,1,3,4,2]
    输出: 3
    说明：
    不能更改原数组（假设数组是只读的）。
    只能使用额外的 O(1) 的空间。
    时间复杂度小于 O(n2) 。
    数组中只有一个重复的数字，但它可能不止重复出现一次。
 """
from typing import List


class Solution:
    # 100ms, 16.1MB
    @classmethod
    def find_duplicate(cls, nums: List[int]) -> int:
        size = len(nums)
        left = 1
        right = size - 1

        while left < right:
            mid = left + (right - left) // 2
            cnt = 0

            for num in nums:
                if num <= mid:
                    cnt += 1

            if cnt > mid:
                right = mid
            else:
                left = mid + 1

        return left

    # 84ms, 16MB
    @classmethod
    def find_duplicate_v2(cls, nums: List[int]) -> int:
        slow = nums[0]
        fast = nums[nums[0]]
        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]
        root = 0
        while root != slow:
            root = nums[root]
            slow = nums[slow]

        return slow


if __name__ == '__main__':
    test_cases = [
        [1, 3, 4, 2, 2],
        [3, 1, 3, 4, 2]
    ]
    for tc in test_cases:
        print(Solution.find_duplicate(tc))
        print(Solution.find_duplicate_v2(tc))
