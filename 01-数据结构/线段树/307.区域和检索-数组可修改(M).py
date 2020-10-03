"""
  @Author       : liujianhan
  @Date         : 20/10/3 12:42
  @Project      : leetcode_in_python
  @FileName     : 307.区域和检索-数组可修改(M).py
  @Description  : 给定一个整数数组  nums，求出数组从索引 i 到 j  (i ≤ j) 范围内元素的总和，
    包含 i,  j 两点。update(i, val) 函数可以通过将下标为 i 的数值更新为 val，从而对数列进行修改。
    示例:

    Given nums = [1, 3, 5]

    sumRange(0, 2) -> 9
    update(1, 2)
    sumRange(0, 2) -> 8
    说明:

    数组仅可以在 update 函数下进行修改。
    你可以假设 update 函数与 sumRange 函数的调用次数是均匀分布的
"""
import math
from typing import List


class NumArray:
    # 564ms, 16.6MB
    def __init__(self, nums: List[int]):
        self.list = nums

    def update(self, i: int, val: int) -> None:
        self.list[i] = val

    def sum_range(self, i: int, j: int) -> int:
        return sum(self.list[i:j + 1])


class NumArray2:
    # 92ms, 16.6MB
    def __init__(self, nums: List[int]):
        self.nums = nums
        if self.nums:
            n = len(nums)
            unit_len = int(n ** 0.5)
            count = math.ceil(n / unit_len)
            self.unit_len = unit_len
            self.dp = [0] * count
            for i in range(n):
                self.dp[i // unit_len] += nums[i]

    def update(self, i: int, val: int) -> None:
        if self.nums:
            block_num = i // self.unit_len
            self.dp[block_num] += val - self.nums[i]
            self.nums[i] = val

    def sum_range(self, i: int, j: int) -> int:
        if self.nums:
            block_num1 = i // self.unit_len
            block_num2 = j // self.unit_len
            if block_num1 == block_num2:
                return sum(self.nums[i:j + 1])
            else:
                res = sum(self.nums[i:(block_num1 + 1) * self.unit_len]) + sum(
                    self.dp[block_num1 + 1:block_num2]) + sum(self.nums[block_num2 * self.unit_len:j + 1])
                return res


if __name__ == '__main__':
    array = NumArray([1, 3, 5])
    print(array.sum_range(0, 2))
    array.update(1, 2)
    print(array.sum_range(0, 2))
