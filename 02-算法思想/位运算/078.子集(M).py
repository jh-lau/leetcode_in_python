"""
  @Author       : Liujianhan
  @Date         : 20/5/4 21:20
  @FileName     : 078.子集(M).py
  @ProjectName  : leetcode_in_python
  @Description  : 给定一组不含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。
    说明：解集不能包含重复的子集。
    示例:
    输入: nums = [1,2,3]
    输出:
    [
      [3],
      [1],
      [2],
      [1,2,3],
      [1,3],
      [2,3],
      [1,2],
      []
    ]
 """
from itertools import combinations
from typing import List


class Solution:
    # 44ms, 13.7MB
    @classmethod
    def subsets(cls, nums: List[int]) -> List[List[int]]:
        return [list(s) for n in range(len(nums)+1)
                for s in combinations(nums, n)]


if __name__ == '__main__':
    print(Solution.subsets([1, 2, 3]))

