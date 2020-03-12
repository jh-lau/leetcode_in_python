"""
  @Author       : liujianhan
  @Date         : 2020/3/12 上午9:25
  @Project      : leetcode_in_python
  @FileName     : 03.数组中重复的数字.py
  @Description  : 在一个长度为 n 的数组 nums 里的所有数字都在 0～n-1 的范围内。数组中某些数字是重复的，但不知道有几个数字重复了，
  也不知道每个数字重复了几次。请找出数组中任意一个重复的数字。
    输入：
    [2, 3, 1, 0, 2, 5, 3]
    输出：2 或 3
"""


class Solution:
    @classmethod
    def find_repeat_number(cls, nums) -> int:
        for i in range(len(nums)):
            while i != nums[i]:
                if nums[i] == nums[nums[i]]:
                    return nums[i]
                nums[nums[i]], nums[i] = nums[i], nums[nums[i]]


if __name__ == '__main__':
    test = [6, 3, 1, 0, 2, 5, 3]
    print(Solution.find_repeat_number(test))
