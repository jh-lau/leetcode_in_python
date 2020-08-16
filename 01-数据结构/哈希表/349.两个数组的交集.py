"""
  @Author       : liujianhan
  @Date         : 2020/4/18 上午10:45
  @Project      : leetcode_in_python
  @FileName     : 349.两个数组的交集.py
  @Description  : 给定两个数组，编写一个函数来计算它们的交集。
    示例 1:
    输入: nums1 = [1,2,2,1], nums2 = [2,2]
    输出: [2]
    示例 2:
    输入: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
    输出: [9,4]
    说明:
    输出结果中的每个元素一定是唯一的。
    我们可以不考虑输出结果的顺序。
"""
from typing import List


class Solution:
    # 64ms, 13.7MB
    @classmethod
    def intersection(cls, nums1: List[int], nums2: List[int]) -> List[int]:
        return list(set(nums1) & set(nums2))


if __name__ == '__main__':
    test_cases = [
        ([1, 2, 2, 1], [2, 2]),
        ([4, 9, 5], [9, 4, 9, 8, 4])
    ]
    for tc in test_cases:
        print(Solution.intersection(*tc))
