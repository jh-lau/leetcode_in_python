"""
  @Author       : Liujianhan
  @Date         : 20/5/2 13:29
  @FileName     : 045.跳跃游戏II(H).py
  @ProjectName  : leetcode_in_python
  @Description  : 给定一个非负整数数组，你最初位于数组的第一个位置。
    数组中的每个元素代表你在该位置可以跳跃的最大长度。
    你的目标是使用最少的跳跃次数到达数组的最后一个位置。
    示例:
    输入: [2,3,1,1,4]
    输出: 2
    解释: 跳到最后一个位置的最小跳跃数是 2。
         从下标为 0 跳到下标为 1 的位置，跳 1 步，然后跳 3 步到达数组的最后一个位置。
    说明:
    假设你总是可以到达数组的最后一个位置。
 """
from typing import List


class Solution:
    @classmethod
    def jump(cls, nums: List[int]) -> int:
        step = 0
        cur_end, max_end = 0, 0

        for i, n in enumerate(nums):
            if i == cur_end + 1:
                cur_end = max_end
                step += 1

            max_end = max(max_end, i + n)

        return step


if __name__ == '__main__':
    print(Solution.jump([2, 3, 1, 1, 4]))
