"""
  User: Liujianhan
  Time: 15:51
 """
__author__ = 'liujianhan'


class Solution:
    @staticmethod
    def merge_two_lists(nums1, m, nums2, n):
        pos = m + n - 1
        m -= 1
        n -= 1
        while m >= 0 and n >= 0:
            if nums1[m] > nums2[n]:
                nums1[pos] = nums1[m]
                pos -= 1
                m -= 1
            else:
                nums1[pos] = nums2[n]
                pos -= 1
                n -= 1
        while n >= 0:
            nums1[pos] = nums2[n]
            pos -= 1
            n -= 1
