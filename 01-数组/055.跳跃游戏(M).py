"""
  @Author       : liujianhan
  @Date         : 2020/4/17 上午10:26
  @Project      : leetcode_in_python
  @FileName     : 055.跳跃游戏(M).py
  @Description  : 给定一个非负整数数组，你最初位于数组的第一个位置。
    数组中的每个元素代表你在该位置可以跳跃的最大长度。
    判断你是否能够到达最后一个位置。
    示例 1:

    输入: [2,3,1,1,4]
    输出: true
    解释: 我们可以先跳 1 步，从位置 0 到达 位置 1, 然后再从位置 1 跳 3 步到达最后一个位置。
    示例 2:

    输入: [3,2,1,0,4]
    输出: false
    解释: 无论怎样，你总会到达索引为 3 的位置。但该位置的最大跳跃长度是 0 ， 所以你永远不可能到达最后一个位置。
"""
from typing import List


class Solution:
    # 76ms, 15.1MB
    @classmethod
    def can_jump(cls, nums: List[int]) -> bool:
        n, right_most = len(nums), 0
        for i in range(n):
            if i <= right_most:
                right_most = max(right_most, i + nums[i])
                if right_most >= n - 1:
                    return True

        return False

    # 48ms 15.2MB
    @classmethod
    def can_jump_v2(cls, nums: List[int]) -> bool:
        temp = 0
        for index, num in enumerate(nums):
            if index + num >= temp >= index:
                temp = index + num

        return temp >= index


if __name__ == '__main__':
    test_cases = [
        [2, 3, 1, 1, 4],
        [3, 2, 1, 0, 4]
    ]
    for tc in test_cases:
        print(Solution.can_jump(tc))
