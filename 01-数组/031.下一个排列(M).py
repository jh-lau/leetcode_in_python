"""
  @Author       : Liujianhan
  @Date         : 20/5/1 16:46
  @FileName     : 031.下一个排列(M).py
  @ProjectName  : leetcode_in_python
  @Description  : 实现获取下一个排列的函数，算法需要将给定数字序列重新排列成字典序中下一个更大的排列。
    如果不存在下一个更大的排列，则将数字重新排列成最小的排列（即升序排列）。
    必须原地修改，只允许使用额外常数空间。
    以下是一些例子，输入位于左侧列，其相应输出位于右侧列。
    1,2,3 → 1,3,2
    3,2,1 → 1,2,3
    1,1,5 → 1,5,1
 """
from typing import List


class Solution:
    # 36ms, 13.5MB
    @classmethod
    def next_permutation(cls, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums) - 1, 0, -1):
            if nums[i] > nums[i - 1]:
                nums[i:] = sorted(nums[i:])
                for j in range(i, len(nums)):
                    if nums[j] > nums[i - 1]:
                        nums[j], nums[i - 1] = nums[i - 1], nums[j]
                        break
                return

        nums.sort()


if __name__ == '__main__':
    test_cases = [
        [1, 2, 3], [3, 2, 1], [1, 1, 5]
    ]
    for tc in test_cases:
        Solution.next_permutation(tc)
        print(tc)
