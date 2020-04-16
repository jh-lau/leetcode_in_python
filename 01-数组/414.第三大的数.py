"""
  @Author       : Liujianhan
  @Date         : 20/4/16 21:45
  @FileName     : 414.第三大的数.py
  @ProjectName  : leetcode_in_python
  @Description  : 给定一个非空数组，返回此数组中第三大的数。如果不存在，则返回数组中最大的数。要求算法时间复杂度必须是O(n)。
    示例 1:

    输入: [3, 2, 1]

    输出: 1

    解释: 第三大的数是 1.
    示例 2:

    输入: [1, 2]

    输出: 2

    解释: 第三大的数不存在, 所以返回最大的数 2 .
    示例 3:

    输入: [2, 2, 3, 1]

    输出: 1

    解释: 注意，要求返回第三大的数，是指第三大且唯一出现的数。
    存在两个值为2的数，它们都排第二。
"""
from typing import List


class Solution:
    # 100ms, 15MB
    @classmethod
    def third_max(cls, nums: List[int]) -> int:
        ans = sorted(list(set(nums)))
        return ans[-3] if len(ans) > 2 else ans[-1]

    # 88ms, 14.4MB
    @classmethod
    def third_max_v2(cls, nums: List[int]) -> int:
        first = second = third = float('-inf')
        for num in nums:
            if num > third:  # 通过第3关
                if num < second:
                    third = num
                elif num > second:  # 通过第2关
                    if num < first:
                        third = second
                        second = num
                    elif num > first:  # 通过第1关
                        third = second
                        second = first
                        first = num
        if third == float('-inf'):
            return first
        else:
            return third


if __name__ == '__main__':
    test_cases = [
        [3, 2, 1],
        [1, 2],
        [1, 2, 2, 2],
        [2, 2, 3, 1]
    ]
    for tc in test_cases:
        print(Solution.third_max(tc))
        print(Solution.third_max_v2(tc))
