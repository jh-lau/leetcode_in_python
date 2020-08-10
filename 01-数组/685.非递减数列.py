"""
  @Author       : liujianhan
  @Date         : 2020/8/10 下午7:31
  @Project      : leetcode_in_python
  @FileName     : 685.非递减数列.py
  @Description  : 给你一个长度为 n 的整数数组，请你判断在 最多 改变 1 个元素的情况下，该数组能否变成一个非递减数列。
    我们是这样定义一个非递减数列的： 对于数组中所有的 i (0 <= i <= n-2)，总满足 nums[i] <= nums[i + 1]。

    示例 1:

    输入: nums = [4,2,3]
    输出: true
    解释: 你可以通过把第一个4变成1来使得它成为一个非递减数列。
    示例 2:

    输入: nums = [4,2,1]
    输出: false
    解释: 你不能在只改变一个元素的情况下将其变为非递减数列。
     

    说明：

    1 <= n <= 10 ^ 4
    - 10 ^ 5 <= nums[i] <= 10 ^ 5
"""
from typing import List


class Solution:
    # 40ms, 14.8MB
    @staticmethod
    def check_possibility(nums: List[int]) -> bool:
        count = 0
        for i in range(1, len(nums)):
            if nums[i] < nums[i - 1]:
                count += 1
                if i + 1 < len(nums) and i - 2 >= 0:
                    if nums[i + 1] < nums[i - 1] and nums[i - 2] > nums[i]:
                        return False
            if count > 1:
                return False
        return True


if __name__ == '__main__':
    test_cases = [
        [4, 2, 3],
        [4, 2, 1],
        [-1, 4, 2, 3]
    ]
    for tc in test_cases:
        print(Solution.check_possibility(tc))
