"""
  @Author       : Liujianhan
  @Date         : 20/4/24 23:00
  @FileName     : 51.数组中的逆序对(H).py
  @ProjectName  : leetcode_in_python
  @Description  : 在数组中的两个数字，如果前面一个数字大于后面的数字，则这两个数字组成一个逆序对。输入一个数组，求出这个数组中的逆序对的总数。
    示例 1:
    输入: [7,5,6,4]
    输出: 5
    限制：
    0 <= 数组长度 <= 50000
 """
from typing import List


class Solution:
    def merge_sort(self, nums: List[int], tmp: List[int], l: int, r: int) -> int:
        if l >= r:
            return 0

        mid = (l + r) // 2
        inv_count = self.merge_sort(nums, tmp, l, mid) + self.merge_sort(nums, tmp, mid + 1, r)
        i, j, pos = l, mid + 1, l
        while i <= mid and j <= r:
            if nums[i] <= nums[j]:
                tmp[pos] = nums[i]
                i += 1
                inv_count += (j - (mid + 1))
            else:
                tmp[pos] = nums[j]
                j += 1
            pos += 1
        for k in range(i, mid + 1):
            tmp[pos] = nums[k]
            inv_count += (j - (mid + 1))
            pos += 1
        for k in range(j, r + 1):
            tmp[pos] = nums[k]
            pos += 1
        nums[l:r + 1] = tmp[l:r + 1]

        return inv_count

    # 1616ms, 18.4MB
    def reverse_pairs(self, nums: List[int]) -> int:
        n = len(nums)
        tmp = [0] * n

        return self.merge_sort(nums, tmp, 0, n - 1)


if __name__ == '__main__':
    test_cases = [
        [7, 5, 6, 4]
    ]
    for tc in test_cases:
        print(Solution().reverse_pairs(tc))
