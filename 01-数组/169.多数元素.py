"""
  @Author       : liujianhan
  @Date         : 2020/4/2 下午7:31
  @Project      : leetcode_in_python
  @FileName     : 169.多数元素.py
  @Description  : 给定一个大小为 n 的数组，找到其中的多数元素。多数元素是指在数组中出现次数大于 ⌊ n/2 ⌋ 的元素。
    你可以假设数组是非空的，并且给定的数组总是存在多数元素。
    输入: [3,2,3]
    输出: 3

    输入: [2,2,1,1,1,2,2]
    输出: 2
"""
from collections import Counter
from typing import List


class Solution:
    # 56ms, 15.2MB
    @classmethod
    def majority_element(cls, nums: List[int]) -> int:
        res = dict()
        for num in nums:
            res[num] = res.get(num, 0) + 1
        temp = [(k, v) for k, v in res.items()]
        temp = sorted(temp, key=lambda x: x[1])
        print(temp)
        return temp[-1][0]

    # 60ms, 15.1MB
    @classmethod
    def majority_element_v2(cls, nums: List[int]) -> int:
        counts = Counter(nums)

        return max(counts.keys(), key=counts.get)

    @classmethod
    def majority_element_v3(cls, nums: List[int]) -> int:
        def majority_element_rec(lo, hi):
            if lo == hi:
                return nums[lo]

            mid = (hi - lo) // 2 + lo
            left = majority_element_rec(lo, mid)
            right = majority_element_rec(mid + 1, hi)

            if left == right:
                return left

            left_count = sum(1 for i in range(lo, hi + 1) if nums[i] == left)
            right_count = sum(1 for i in range(lo, hi + 1) if nums[i] == right)

            return left if left_count > right_count else right

        return majority_element_rec(0, len(nums) - 1)


if __name__ == '__main__':
    test_cases = [
        [3, 2, 3],
        [2, 2, 1, 1, 1, 2, 2]
    ]
    for tc in test_cases:
        print(Solution.majority_element(tc))
        print(Solution.majority_element_v2(tc))
        print(Solution.majority_element_v3(tc))