"""
  @Author       : liujianhan
  @Date         : 2020/4/18 上午10:53
  @Project      : leetcode_in_python
  @FileName     : 350.两个数组的交集II.py
  @Description  : 给定两个数组，编写一个函数来计算它们的交集。
    示例 1:

    输入: nums1 = [1,2,2,1], nums2 = [2,2]
    输出: [2,2]
    示例 2:

    输入: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
    输出: [4,9]
    说明：

    输出结果中每个元素出现的次数，应与元素在两个数组中出现的次数一致。
    我们可以不考虑输出结果的顺序。
    进阶:

    如果给定的数组已经排好序呢？你将如何优化你的算法？
    如果 nums1 的大小比 nums2 小很多，哪种方法更优？
    如果 nums2 的元素存储在磁盘上，磁盘内存是有限的，并且你不能一次加载所有的元素到内存中，你该怎么办？
"""
from typing import List


class Solution:
    # 108ms, 13.9MB
    @classmethod
    def intersect(cls, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        dic = {num: nums1.count(num) for num in nums1}
        res = []
        for num in nums2:
            if dic.get(num, 0):
                res.append(num)
                dic[num] -= 1

        return res

    # 72ms, 13.8MB
    @classmethod
    def intersect_v2(cls, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        nums1.sort()
        nums2.sort()
        i, j = 0, 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                i += 1
            elif nums1[i] > nums2[j]:
                j += 1
            else:
                res.append(nums1[i])
                i += 1
                j += 1

        return res


if __name__ == '__main__':
    test_cases = [
        ([1, 2, 2, 1], [2, 2]),
        ([4, 9, 5], [9, 4, 9, 8, 4])
    ]
    for tc in test_cases:
        print(Solution.intersect(*tc))
        print(Solution.intersect_v2(*tc))
