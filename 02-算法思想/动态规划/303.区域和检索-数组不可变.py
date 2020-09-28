"""
  @Author       : liujianhan
  @Date         : 2020/9/28 13:53
  @Project      : leetcode_in_python
  @FileName     : 303.区域和检索-数组不可变.py
  @Description  : 给定一个整数数组  nums，求出数组从索引 i 到 j  (i ≤ j) 范围内元素的总和，包含 i,  j 两点。
    示例：
    给定 nums = [-2, 0, 3, -5, 2, -1]，求和函数为 sumRange()

    sumRange(0, 2) -> 1
    sumRange(2, 5) -> -1
    sumRange(0, 5) -> -3
    说明:

    你可以假设数组不可变。
    会多次调用 sumRange 方法。
"""
from typing import List


class NumArray:
    # 84ms, 16.8MB
    def __init__(self, nums: List[int]):
        for i, num in enumerate(nums[1:], start=1):
            nums[i] += nums[i-1]
        self.nums = nums

    def sum_range(self, i: int, j: int) -> int:
        if not i:
            return self.nums[j]
        return self.nums[j] - self.nums[i-1]


if __name__ == '__main__':
    test_cases = [
        [-2, 0, 3, -5, 2, -1]
    ]
    s = NumArray(test_cases[0])
    print(s.sum_range(0, 2))
    print(s.sum_range(2, 5))
    print(s.sum_range(0, 5))