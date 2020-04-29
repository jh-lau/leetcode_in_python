"""
  @Author       : Liujianhan
  @Date         : 20/4/29 22:25
  @FileName     : 004.寻找两个有序数组的中位数(H).py
  @ProjectName  : leetcode_in_python
  @Description  : 给定两个大小为 m 和 n 的有序数组 nums1 和 nums2。
    请你找出这两个有序数组的中位数，并且要求算法的时间复杂度为 O(log(m + n))。
    你可以假设 nums1 和 nums2 不会同时为空。
    示例 1:
    nums1 = [1, 3]
    nums2 = [2]
    则中位数是 2.0
    示例 2:
    nums1 = [1, 2]
    nums2 = [3, 4]
    则中位数是 (2 + 3)/2 = 2.5
 """
from typing import List


class Solution:
    # 64ms, 13.7MB
    @classmethod
    def find_median_sorted_arrays(cls, nums1: List[int], nums2: List[int]) -> float:
        # 1. 下面这些情况进行处理
        len1 = len(nums1)
        len2 = len(nums2)
        # 一个数组为空，补上另一个数组，中值/2后还是原来的结果(类似于: 3 * 2 / 2还是原来的结果)
        if len1 == 0:
            nums1 = nums2
        elif len2 == 0:
            nums2 = nums1
        if len1 == 1 and len2 == 1: return (nums1[0] + nums2[0]) / 2  # 这个情况直接返回

        # 2. 获取基本变量信息
        length_all = len1 + len2
        mid = int(length_all / 2 + 1)  # 使运行到这里长度总>=3，mid中值的位置(3/2+1=2、4/2+1=3)
        i = j = 0  # 便利索引
        ary = [0, 0]  # 存储中值的列表

        # 3. 核心代码
        while i < len1 and j < len2:
            # 假定两个数字长度相同，和一个数组遍历到临界点的时候，刚好i + j == mid

            if nums1[i] < nums2[j]:
                ary[(i + j) % 2] = nums1[i]
                i += 1
            else:
                ary[(i + j) % 2] = nums2[j]
                j += 1
            if i + j == mid: break  # 达到中值 退出循环
        # 对两个数组长度不一，以及一个数组下标i或j先行达临界点(nums1.length = i或nums2.length == j)进行补充
        while i + j < mid and i == len1:
            ary[(i + j) % 2] = nums2[j]
            j += 1
        while i + j < mid and j == len2:
            ary[(i + j) % 2] = nums1[i]
            i += 1

        # 4. 判断后返回对应的运行结果
        if length_all % 2 != 0:
            return ary[(i + j - 1) % 2]  # 总长度为奇数，最后一个赋值就是中值。
        else:
            return (ary[0] + ary[1]) / 2  # 总长度为偶数，直接返回他们相加的平均值。


if __name__ == '__main__':
    test_cases = [
        ([1, 3], [2]), ([1, 2], [3, 4])
    ]
    for tc in test_cases:
        print(Solution.find_median_sorted_arrays(*tc))
