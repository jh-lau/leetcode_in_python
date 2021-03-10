"""
  @Author       : liujianhan
  @Date         : 21/3/6 18:05
  @Project      : leetcode_in_python
  @FileName     : 503.下一个更大元素II(M).py
  @Description  : 给定一个循环数组（最后一个元素的下一个元素是数组的第一个元素），输出每个元素的下一个更大元素。数字 x
    的下一个更大的元素是按数组遍历顺序，这个数字之后的第一个比它更大的数，这意味着你应该循环地搜索它的下一个更大的数。如果不存在，则输出 -1。

    示例 1:

    输入: [1,2,1]
    输出: [2,-1,2]
    解释: 第一个 1 的下一个更大的数是 2；
    数字 2 找不到下一个更大的数；
    第二个 1 的下一个最大的数需要循环搜索，结果也是 2。
    注意: 输入数组的长度不会超过 10000。
"""
from typing import List


class Solution:
    # 228ms, 16.3MB
    @staticmethod
    def next_greater_elements(nums: List[int]) -> List[int]:
        n = len(nums)
        ret = [-1] * n
        stk = list()

        for i in range(n * 2 - 1):
            while stk and nums[stk[-1]] < nums[i % n]:
                ret[stk.pop()] = nums[i % n]
            stk.append(i % n)

        return ret


if __name__ == '__main__':
    test_cases = [
        [1, 2, 1], [1, 2, 23, 4, 2, 1]
    ]
    for test_case in test_cases:
        print(Solution.next_greater_elements(test_case))
