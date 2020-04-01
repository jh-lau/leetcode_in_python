"""
  @Author       : liujianhan
  @Date         : 2020/3/23 下午4:06
  @Project      : leetcode_in_python
  @FileName     : 136.只出现一次的数字.py
  @Description  : 给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。
  你的算法应该具有线性时间复杂度。 你可以不使用额外空间来实现吗？
"""
from typing import List


class Solution:
    # 56ms, 15MB
    @classmethod
    def single_number(cls, nums: List[int]) -> int:
        result = nums[0]
        for num in nums[1:]:
            result ^= num

        return result

    # 52ms, 15.5MB
    @classmethod
    def single_number_v2(cls, nums: List[int]) -> int:
        s = dict()
        for num in nums:
            s[num] = s.get(num, 0) + 1

        return [key for key, value in s.items() if value == 1][0]


if __name__ == '__main__':
    test_case = [[1, 1, 2, 2, 3], [2, 2, 1], [4, 1, 2, 1, 2]]
    for tc in test_case:
        print(tc, Solution.single_number(tc))
        print(tc, Solution.single_number_v2(tc))
