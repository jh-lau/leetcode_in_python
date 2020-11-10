"""
  @Author       : liujianhan
  @Date         : 2020/11/10 10:30
  @Project      : leetcode_in_python
  @FileName     : 496.下一个更大元素I.py
  @Description  : 给定两个 没有重复元素 的数组 nums1 和 nums2 ，其中nums1 是 nums2 的子集。
    找到 nums1 中每个元素在 nums2 中的下一个比其大的值。
    nums1 中数字 x 的下一个更大元素是指 x 在 nums2 中对应位置的右边的第一个比 x 大的元素。如果不存在，对应位置输出 -1 。
    示例 1:

    输入: nums1 = [4,1,2], nums2 = [1,3,4,2].
    输出: [-1,3,-1]
    解释:
        对于num1中的数字4，你无法在第二个数组中找到下一个更大的数字，因此输出 -1。
        对于num1中的数字1，第二个数组中数字1右边的下一个较大数字是 3。
        对于num1中的数字2，第二个数组中没有下一个更大的数字，因此输出 -1。
    示例 2:

    输入: nums1 = [2,4], nums2 = [1,2,3,4].
    输出: [3,-1]
    解释:
        对于 num1 中的数字 2 ，第二个数组中的下一个较大数字是 3 。
        对于 num1 中的数字 4 ，第二个数组中没有下一个更大的数字，因此输出 -1 。
     
    提示：

    nums1和nums2中所有元素是唯一的。
    nums1和nums2 的数组大小都不超过1000。
"""
from typing import List


class Solution:
    # 92ms, 13.7MB
    @staticmethod
    def next_greater_element(nums1: List[int], nums2: List[int]) -> List[int]:
        result = [-1] * len(nums1)
        for i, n1 in enumerate(nums1):
            for n2 in nums2[nums2.index(n1)+1:]:
                if n2 > n1:
                    result[i] = n2
                    break

        return result

    # 64ms, 13.8MB
    @staticmethod
    def next_greater_element_v2(nums1: List[int], nums2: List[int]) -> List[int]:
        if not nums2:
            return []
        temp = {nums2[-1]: -1}
        for i in range(len(nums2) - 1):
            for j in range(i + 1, len(nums2)):
                temp[nums2[i]] = -1
                if nums2[j] > nums2[i]:
                    temp[nums2[i]] = nums2[j]
                    break
        res = [temp[i] for i in nums1]

        return res


if __name__ == '__main__':
    test_cases = [
        ([4, 1, 2], [1, 3, 4, 2]),
        ([2, 4], [1, 2, 3, 4]),
    ]
    for tc in test_cases:
        print(Solution.next_greater_element(*tc))
        print(Solution.next_greater_element_v2(*tc))
