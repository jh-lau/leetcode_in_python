"""
  @Author       : liujianhan
  @Date         : 20/11/1 22:12
  @Project      : leetcode_in_python
  @FileName     : 645.错误的集合.py
  @Description  : 集合 S 包含从1到 n 的整数。不幸的是，因为数据错误，导致集合里面某一个元素复制了成了集合里面的另外一个元素的值，
    导致集合丢失了一个整数并且有一个元素重复。给定一个数组 nums 代表了集合 S 发生错误后的结果。你的任务是首先寻找到重复出现的整数，
    再找到丢失的整数，将它们以数组的形式返回。
    示例 1:

    输入: nums = [1,2,2,4]
    输出: [2,3]
    注意:

    给定数组的长度范围是 [2, 10000]。
    给定的数组是无序的。
"""
from typing import List
from collections import defaultdict


class Solution:
    # 3472ms, 16.2MB
    @staticmethod
    def find_error_nums(nums: List[int]) -> List[int]:
        normal = set(range(1, len(nums) + 1))
        missing = list(normal - set(nums))[0]
        for num in nums[:]:
            nums.remove(num)
            if num in nums:
                return [num, missing]

    # 244ms, 15.3MB
    @staticmethod
    def find_error_nums_v2(nums: List[int]) -> List[int]:
        a = sum(nums) - sum(set(nums))  # a为重复数字，b为缺失数字
        c = 0
        for i, num in enumerate(nums, 1):  # 从1开始计数
            c ^= (i ^ num)
        b = c ^ a
        return [a, b]


if __name__ == '__main__':
    test_cases = [
        [1, 2, 2, 4],
        [3, 2, 2],
        [3, 2, 3, 4, 6, 5],
        [1, 5, 3, 2, 2, 7, 6, 4, 8, 9]
    ]
    for tc in test_cases:
        print(Solution.find_error_nums(tc))
