"""
  @Author       : liujianhan
  @Date         : 2020/8/13 下午7:24
  @Project      : leetcode_in_python
  @FileName     : 334.递增的三元子序列(M).py
  @Description  : 给定一个未排序的数组，判断这个数组中是否存在长度为 3 的递增子序列。
    数学表达式如下:

    如果存在这样的 i, j, k,  且满足 0 ≤ i < j < k ≤ n-1，
    使得 arr[i] < arr[j] < arr[k] ，返回 true ; 否则返回 false 。
    说明: 要求算法的时间复杂度为 O(n)，空间复杂度为 O(1) 。

    示例 1:

    输入: [1,2,3,4,5]
    输出: true
    示例 2:

    输入: [5,4,3,2,1]
    输出: false
"""
import sys
from typing import List


class Solution:
    # 64ms, 14.1MB
    @staticmethod
    def increasing_triplet(nums: List[int]) -> bool:
        r1, r2 = sys.maxsize, sys.maxsize
        for n in nums:
            if n <= r1:
                r1 = n
            elif n <= r2:
                r2 = n
            else:
                return True
        return False


if __name__ == '__main__':
    test_cases = [
        [1, 2, 3, 4, 5],
        [5, 4, 3, 2, 1]
    ]
    for tc in test_cases:
        print(Solution.increasing_triplet(tc))
