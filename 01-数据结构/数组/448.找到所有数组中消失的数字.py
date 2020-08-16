"""
  @Author       : Liujianhan
  @Date         : 20/4/16 22:29
  @FileName     : 448.找到所有数组中消失的数字.py
  @ProjectName  : leetcode_in_python
  @Description  : 给定一个范围在  1 ≤ a[i] ≤ n ( n = 数组大小 ) 的 整型数组，数组中的元素一些出现了 两次，另一些只出现一次。
    找到所有在 [1, n] 范围之间没有出现在数组中的数字。
    您能在不使用额外空间且时间复杂度为O(n)的情况下完成这个任务吗? 你可以假定返回的数组不算在额外空间内。
    示例:

    输入:
    [4,3,2,7,8,2,3,1]

    输出:
    [5,6]
 """
from typing import List


class Solution:
    # 524ms, 21.3MB
    @classmethod
    def find_disappeared_numbers(cls, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            new_index = abs(nums[i]) - 1
            if nums[new_index] > 0:
                nums[new_index] *= -1

        result = []

        for i in range(1, len(nums) + 1):
            if nums[i - 1] > 0:
                result.append(i)

        return result

    # 424ms, 23.2MB
    @classmethod
    def find_disappeared_numbers_v2(cls, nums: List[int]) -> List[int]:
        res = []
        n = len(nums)
        nums = set(nums)
        for i in range(1, n + 1):
            if i not in nums:
                res.append(i)

        return res


if __name__ == '__main__':
    test_cases = [[4, 3, 2, 7, 8, 2, 3, 1]]
    for tc in test_cases:
        # print(Solution.find_disappeared_numbers(tc))
        print(Solution.find_disappeared_numbers_v2(tc))
