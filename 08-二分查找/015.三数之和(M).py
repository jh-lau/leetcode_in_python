"""
  @Author       : Liujianhan
  @Date         : 20/4/30 22:22
  @FileName     : 015.三数之和(M).py
  @ProjectName  : leetcode_in_python
  @Description  : 给你一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？请你找出所有满足条件且不重复的三元组。
    注意：答案中不可以包含重复的三元组。
    示例：
    给定数组 nums = [-1, 0, 1, 2, -1, -4]，
    满足要求的三元组集合为：
    [
      [-1, 0, 1],
      [-1, -1, 2]
    ]
 """
import bisect
from collections import Counter
from typing import List


class Solution:
    # 184ms, 17.1MB
    @classmethod
    def three_sum(cls, nums: List[int]) -> List[List[int]]:
        ans = []
        counts = Counter(nums)
        nums = sorted(counts)

        for i, num in enumerate(nums):
            if counts[num] > 1:
                if num == 0:
                    if counts[num] > 2:
                        ans.append([0, 0, 0])
                else:
                    if -num * 2 in counts:
                        ans.append([num, num, -2 * num])
            if num < 0:
                two_sum = -num
                left = bisect.bisect_left(nums, (two_sum - nums[-1]), i + 1)
                for i in nums[left: bisect.bisect_right(nums, (two_sum // 2), left)]:
                    j = two_sum - i
                    if j in counts and j != i:
                        ans.append([num, i, j])

        return ans


if __name__ == '__main__':
    print(Solution.three_sum([-1, 0, 1, 2, -1, -4]))
