"""
  @Author       : liujianhan
  @Date         : 2020/4/2 下午5:35
  @Project      : leetcode_in_python
  @FileName     : 167.两数之和II - 输入有序数组.py
  @Description  : 给定一个已按照升序排列 的有序数组，找到两个数使得它们相加之和等于目标数。
    函数应该返回这两个下标值 index1 和 index2，其中 index1 必须小于 index2。
    说明:
    返回的下标值（index1 和 index2）不是从零开始的。
    你可以假设每个输入只对应唯一的答案，而且你不可以重复使用相同的元素。

    输入: numbers = [2, 7, 11, 15], target = 9
    输出: [1,2]
    解释: 2 与 7 之和等于目标数 9 。因此 index1 = 1, index2 = 2
"""
from typing import List


class Solution:
    # 48ms, 13.9MB
    @classmethod
    def two_sum(cls, numbers: List[int], target: int) -> List[int]:
        """ 双指针，时间复杂度O(n), 空间复杂度O(1)
            特判，若数组为空，返回[]
            定义左指针l=0l=0指向最小元素，定义右指针r=n-1r=n−1指向最大元素
            循环条件l<rl<r：
            若numbers[l]+numbers[r]==targetnumbers[l]+numbers[r]==target，则返回[l+1,r+1][l+1,r+1]
            若numbers[l]+numbers[r]>targetnumbers[l]+numbers[r]>target，说明右边的值太大，调小一点，即r=r-1r=r−1
            否则说明左边的值太小，令l=l+1l=l+1
            执行到这步，若不返回说明无解，返回[-1,-1][−1,−1]"""
        if not numbers:
            return []
        left, right = 0, len(numbers) - 1
        while left < right:
            if numbers[left] + numbers[right] == target:
                return [left + 1, right + 1]
            elif numbers[left] + numbers[right] > target:
                right -= 1
            else:
                left += 1
        return [-1, -1]


if __name__ == '__main__':
    test_cases = [
        [2, 7, 11, 15],
        [4, 6, 9, 12]
    ]
    for tc in test_cases:
        print(Solution.two_sum(tc, 9))
        print(Solution.two_sum(tc, 15))
