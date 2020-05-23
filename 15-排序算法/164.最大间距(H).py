"""
  @Author       : Liujianhan
  @Date         : 20/5/23 21:48
  @FileName     : 164.最大间距(H).py
  @ProjectName  : leetcode_in_python
  @Description  : 给定一个无序的数组，找出数组在排序之后，相邻元素之间最大的差值。
    如果数组元素个数小于 2，则返回 0。
    示例 1:
    输入: [3,6,9,1]
    输出: 3
    解释: 排序后的数组是 [1,3,6,9], 其中相邻元素 (3,6) 和 (6,9) 之间都存在最大差值 3。
    示例 2:
    输入: [10]
    输出: 0
    解释: 数组元素个数小于 2，因此返回 0。

 """
from itertools import chain
from typing import List


class Solution:
    # 56ms, 14.2MB
    @classmethod
    def maximum_gap(cls, nums: List[int]) -> int:
        def radix_sort(nums):
            n = len(nums)
            if n < 2:
                return nums
            max_val, exp, radix = max(nums), 1, 10
            while max_val // exp > 0:
                counter = [[] for _ in range(radix)]
                for num in nums:
                    counter[(num // exp) % radix].append(num)
                nums = list(chain(*counter))
                exp *= radix
            return nums

        n = len(nums)
        if n < 2:
            return 0
        nums = radix_sort(nums)
        return max(nums[i] - nums[i - 1] for i in range(1, n))


if __name__ == '__main__':
    test_cases = [
        [3, 6, 9, 1], [10]
    ]
    for tc in test_cases:
        print(Solution.maximum_gap(tc))
