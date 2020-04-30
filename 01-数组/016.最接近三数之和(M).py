"""
  @Author       : Liujianhan
  @Date         : 20/4/30 22:35
  @FileName     : 016.最接近三数之和(M).py
  @ProjectName  : leetcode_in_python
  @Description  : 给定一个包括 n 个整数的数组 nums 和 一个目标值 target。找出 nums 中的三个整数，使得它们的和与 target 最接近。返回这三个数的和。假定每组输入只存在唯一答案。
    例如，给定数组 nums = [-1，2，1，-4], 和 target = 1.
    与 target 最接近的三个数的和为 2. (-1 + 2 + 1 = 2).
 """
from typing import List


class Solution:
    # 100ms, 13.7MB
    @classmethod
    def three_sum_closest(cls, nums: List[int], target: int) -> int:
        # 特判：n=3，返回sum(nums)
        n = len(nums)
        if n == 3:
            return sum(nums)
        # 令最小差的绝对值为无限大
        min_diff = float("inf")
        closest_sum = 0
        # nums排序
        nums.sort()
        # 遍历nums
        for i in range(n - 2):
            if i > 1 and nums[i] == nums[i - 1]:
                continue
            # 双指针
            L = i + 1
            R = n - 1
            while L < R:
                three_sum = nums[i] + nums[L] + nums[R]
                diff = three_sum - target
                # 如果diff的绝对值比min_diff小，那么更新min_diff和closest_sum
                if abs(diff) < min_diff:
                    min_diff = abs(diff)
                    closest_sum = three_sum
                if diff == 0:
                    # 如果diff为0，直接返回three_sum
                    return closest_sum
                elif diff < 0:
                    # 说明three_sum < target，L右移
                    L += 1
                    while L < R and nums[L] == nums[L - 1]:
                        L += 1
                else:
                    # 说明three_sum > target，R左移
                    R -= 1
                    while L < R and nums[R] == nums[R + 1]:
                        R -= 1
        return closest_sum


if __name__ == '__main__':
    print(Solution.three_sum_closest([-1, 2, 1, -4], 1))
