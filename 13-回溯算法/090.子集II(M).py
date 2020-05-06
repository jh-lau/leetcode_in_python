"""
  @Author       : Liujianhan
  @Date         : 20/5/6 22:05
  @FileName     : 090.子集II(M).py
  @ProjectName  : leetcode_in_python
  @Description  : 给定一个可能包含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。
    说明：解集不能包含重复的子集。
    示例:
    输入: [1,2,2]
    输出:
    [
      [2],
      [1],
      [1,2,2],
      [2,2],
      [1,2],
      []
    ]
 """
from typing import List


class Solution:
    # 56ms, 13.7MB
    @classmethod
    def subsets_with_dup(cls, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        check = [0 for _ in range(len(nums))]

        def backtrack(sol, index, nums, check):
            if index == len(nums):
                nonlocal res
                res.append(sol)
                return
            if not (index > 0 and nums[index] == nums[index - 1] and not check[index - 1]):
                check[index] = 1
                backtrack(sol + [nums[index]], index + 1, nums, check)
                check[index] = 0
            backtrack(sol, index + 1, nums, check)

        backtrack([], 0, nums, check)

        return res

    # 44ms, 14MB
    @classmethod
    def subsets_with_dup_v2(cls, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        def back(nums, path):
            res.append(path)
            for i in range(len(nums)):
                if i > 0 and nums[i] == nums[i - 1]:
                    continue
                back(nums[i + 1:], path + [nums[i]])

        back(nums, [])

        return res


if __name__ == '__main__':
    test_cases = [
        [1, 2, 2]
    ]
    for tc in test_cases:
        print(Solution.subsets_with_dup(tc))
