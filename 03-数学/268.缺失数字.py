"""
  @Author       : Liujianhan
  @Date         : 20/7/18 21:22
  @FileName     : 268.缺失数字.py
  @ProjectName  : leetcode_in_python
  @Description  : 给定一个包含 0, 1, 2, ..., n 中 n 个数的序列，找出 0 .. n 中没有出现在序列中的那个数。
    示例 1:
    输入: [3,0,1]
    输出: 2
    示例 2:
    输入: [9,6,4,2,3,5,7,0,1]
    输出: 8
    说明:
    你的算法应具有线性时间复杂度。你能否仅使用额外常数空间来实现?
 """
from typing import List


class Solution:
    # 68ms, 14.8MB
    @staticmethod
    def missing_number(nums: List[int]) -> int:
        """位运算"""
        missing = len(nums)
        for i, num in enumerate(nums):
            missing ^= i ^ num
        return missing

    # 64ms, 14.6MB
    @staticmethod
    def missing_number_v2(nums: List[int]) -> int:
        """数学"""
        target = len(nums) * (len(nums) + 1) // 2
        actual = sum(nums)
        return target - actual

    # 40ms, 15.1MB
    @staticmethod
    def missing_number_v3(nums: List[int]) -> int:
        """哈希表"""
        num_set = set(nums)
        n = len(nums) + 1
        for number in range(n):
            if number not in num_set:
                return number


if __name__ == '__main__':
    test_cases = [
        [3, 0, 1],
        [9, 6, 4, 2, 3, 5, 7, 0, 1]
    ]
    for tc in test_cases:
        print(Solution.missing_number(tc))
        print(Solution.missing_number_v2(tc))
        print(Solution.missing_number_v3(tc))
