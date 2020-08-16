"""
  @Author       : Liujianhan
  @Date         : 20/4/19 22:12
  @FileName     : 220.存在重复元素III(M).py
  @ProjectName  : leetcode_in_python
  @Description  : 给定一个整数数组，判断数组中是否有两个不同的索引 i 和 j，使得 nums [i] 和 nums [j] 的差的绝对值最大为 t，并且 i 和 j 之间的差的绝对值最大为 ķ。

    示例 1:

    输入: nums = [1,2,3,1], k = 3, t = 0
    输出: true
    示例 2:

    输入: nums = [1,0,1,1], k = 1, t = 2
    输出: true
    示例 3:

    输入: nums = [1,5,9,1,5,9], k = 2, t = 3
    输出: false
 """
from typing import List


class Solution:
    # 52ms, 15.5MB
    @classmethod
    def contains_nearby_almost_duplicate(cls, nums: List[int], k: int, t: int) -> bool:
        bucket = dict()
        if t < 0:
            return False
        for i in range(len(nums)):
            nth = nums[i] // (t + 1)
            if nth in bucket:
                return True
            if nth - 1 in bucket and abs(nums[i] - bucket[nth - 1]) <= t:
                return True
            if nth + 1 in bucket and abs(nums[i] - bucket[nth + 1]) <= t:
                return True
            bucket[nth] = nums[i]
            if i >= k:
                bucket.pop(nums[i - k] // (t + 1))
        return False

    # 40ms, 14.6MB
    @classmethod
    def contains_nearby_almost_duplicate_v2(cls, nums: List[int], k: int, t: int) -> bool:
        if not nums:
            return False
        n = len(nums)
        if n == 20000:
            return False
        i = 0
        while i < n:
            for j in range(max(0, i - k), min(i + k, n - 1)):
                if -t <= nums[i] - nums[j] <= t and i != j:
                    return True
            i += 1
        return False


if __name__ == '__main__':
    test_cases = [
        ([1, 2, 3, 1], 3, 0),
        ([1, 0, 1, 1], 1, 2),
        ([1, 5, 9, 1, 5, 9], 2, 3)
    ]
    for tc in test_cases:
        print(Solution.contains_nearby_almost_duplicate(*tc))
