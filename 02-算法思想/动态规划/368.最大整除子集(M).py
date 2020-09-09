"""
  @Author       : liujianhan
  @Date         : 2020/9/9 19:52
  @Project      : leetcode_in_python
  @FileName     : 368.最大整除子集(M).py
  @Description  : 给出一个由无重复的正整数组成的集合，找出其中最大的整除子集，子集中任意一对 (Si，Sj) 都要满足：
  Si % Sj = 0 或 Sj % Si = 0。
    如果有多个目标子集，返回其中任何一个均可。
    示例 1:

    输入: [1,2,3]
    输出: [1,2] (当然, [1,3] 也正确)
    示例 2:

    输入: [1,2,4,8]
    输出: [1,2,4,8]
"""
from typing import List


class Solution:
    # 372ms, 14.8MB
    @staticmethod
    def largest_divisible_subset(nums: List[int]) -> List[int]:
        def EDS(i):
            """ recursion with memoization """
            if i in memo:
                return memo[i]

            tail = nums[i]
            maxSubset = []
            # The value of EDS(i) depends on it previous elements
            for p in range(0, i):
                if tail % nums[p] == 0:
                    subset = EDS(p)
                    if len(maxSubset) < len(subset):
                        maxSubset = subset

            # extend the found max subset with the current tail.
            maxSubset = maxSubset.copy()
            maxSubset.append(tail)

            # memorize the intermediate solutions for reuse.
            memo[i] = maxSubset
            return maxSubset

        # test case with empty set
        if len(nums) == 0: return []

        nums.sort()
        memo = {}

        # Find the largest divisible subset
        return max([EDS(i) for i in range(len(nums))], key=len)


if __name__ == '__main__':
    test_cases = [
        [1, 2, 3],
        [1, 2, 4, 8]
    ]
    for tc in test_cases:
        print(Solution.largest_divisible_subset(tc))
