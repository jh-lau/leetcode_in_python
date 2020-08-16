"""
  @Author       : Liujianhan
  @Date         : 20/4/16 23:01
  @FileName     : 453.最小移动次数使数组元素相等.py
  @ProjectName  : leetcode_in_python
  @Description  : 给定一个长度为 n 的非空整数数组，找到让数组所有元素相等的最小移动次数。每次移动可以使 n - 1 个元素增加 1。
    示例:

    输入:
    [1,2,3]

    输出:
    3
    解释:
    只需要3次移动（注意每次移动会增加两个元素的值）：

    [1,2,3]  =>  [2,3,3]  =>  [3,4,3]  =>  [4,4,4]
 """
from typing import List


class Solution:
    # 408ms, 14.9MB
    @classmethod
    def min_moves(cls, nums: List[int]) -> int:
        return sum(nums) - min(nums) * len(nums)

    # out of time
    @classmethod
    def min_moves_v2(cls, nums: List[int]) -> int:
        """题意可理解位每次让一个值减去1，使得所有的值相等，
        那理想情况就是每个值最终等于最小值。那么题目就转换为所有值减去最小值的和。"""
        min_value = min(nums)
        cnt = 0
        for i in nums:
            cnt += i - min_value

        return cnt


if __name__ == '__main__':
    test_cases = [[1, 2, 3]]
    for tc in test_cases:
        print(Solution.min_moves(tc))
