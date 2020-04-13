"""
  @Author       : liujianhan
  @Date         : 2020/4/13 上午10:20
  @Project      : leetcode_in_python
  @FileName     : 189.旋转数组.py
  @Description  : 给定一个数组，将数组中的元素向右移动 k 个位置，其中 k 是非负数。
    示例 1:

    输入: [1,2,3,4,5,6,7] 和 k = 3
    输出: [5,6,7,1,2,3,4]
    解释:
    向右旋转 1 步: [7,1,2,3,4,5,6]
    向右旋转 2 步: [6,7,1,2,3,4,5]
    向右旋转 3 步: [5,6,7,1,2,3,4]
    示例 2:

    输入: [-1,-100,3,99] 和 k = 2
    输出: [3,99,-1,-100]
    解释:
    向右旋转 1 步: [99,-1,-100,3]
    向右旋转 2 步: [3,99,-1,-100]
    说明:

    尽可能想出更多的解决方案，至少有三种不同的方法可以解决这个问题。
    要求使用空间复杂度为 O(1) 的 原地 算法。
"""
from typing import List


class Solution:
    # 44ms, 13.8MB
    @classmethod
    def rotate(cls, nums: List[int], k: int) -> None:
        nums[:] = (nums[i] for i in range(-(k % len(nums)), len(nums) - k % len(nums)))

    # 44ms, 14MB
    @classmethod
    def rotate_v2(cls, nums: List[int], k: int) -> None:
        k %= len(nums)
        if not k:
            return
        nums[:-k], nums[-k:] = nums[-k:], nums[:-k]

    # 44ms, 13.7MB
    @classmethod
    def rotate_v3(cls, nums: List[int], k: int) -> None:
        nums[:] = nums[-k % len(nums):] + nums[:-k % len(nums)]


if __name__ == '__main__':
    test_cases = [
        ([1, 2, 3, 4, 5, 6, 7], 3),
        ([-1, -100, 3, 99], 2),
        ([-1, -100, 3, 99], 0),
        ([1, 2, 3], 10)
    ]
    for tc in test_cases:
        # Solution.rotate(*tc)
        # Solution.rotate_v2(*tc)
        Solution.rotate_v3(*tc)
        print(tc[0])
