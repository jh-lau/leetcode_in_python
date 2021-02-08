"""
  @Author       : liujianhan
  @Date         : 21/2/8 19:08
  @Project      : leetcode_in_python
  @FileName     : 978.最长湍流子数组(M).py
  @Description  : 当 A 的子数组 A[i], A[i+1], ..., A[j] 满足下列条件时，我们称其为湍流子数组：
    若 i <= k < j，当 k 为奇数时， A[k] > A[k+1]，且当 k 为偶数时，A[k] < A[k+1]；
    或 若 i <= k < j，当 k 为偶数时，A[k] > A[k+1] ，且当 k 为奇数时， A[k] < A[k+1]。
    也就是说，如果比较符号在子数组中的每个相邻元素对之间翻转，则该子数组是湍流子数组。
    返回 A 的最大湍流子数组的长度。
     
    示例 1：
    输入：[9,4,2,10,7,8,8,1,9]
    输出：5
    解释：(A[1] > A[2] < A[3] > A[4] < A[5])

    示例 2：
    输入：[4,8,12,16]
    输出：2

    示例 3：
    输入：[100]
    输出：1

    提示：
    1 <= A.length <= 40000
    0 <= A[i] <= 10^9
"""
from typing import List


class Solution:
    # 192ms, 18.2MB
    @staticmethod
    def max_turbulence_size(arr: List[int]) -> int:

        """
        :type arr: List[int]
        :rtype: int
        """
        N = len(arr)
        up = [1] * N
        down = [1] * N
        res = 1
        for i in range(1, N):
            if arr[i - 1] < arr[i]:
                up[i] = down[i - 1] + 1
            elif arr[i - 1] > arr[i]:
                down[i] = up[i - 1] + 1
            res = max(res, max(up[i], down[i]))
        return res


if __name__ == '__main__':
    test_cases = [
        [9, 4, 2, 10, 7, 8, 8, 1, 9],
        [4, 8, 12, 16],
        [100]
    ]
    for tc in test_cases:
        print(Solution.max_turbulence_size(tc))
