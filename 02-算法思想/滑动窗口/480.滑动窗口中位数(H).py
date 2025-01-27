"""
  @Author       : liujianhan
  @Date         : 2021/2/3 10:19
  @Project      : leetcode_in_python
  @FileName     : 480.滑动窗口中位数(H).py
  @Description  : 中位数是有序序列最中间的那个数。如果序列的大小是偶数，则没有最中间的数；此时中位数是最中间的两个数的平均数。
    例如：
    [2,3,4]，中位数是 3
    [2,3]，中位数是 (2 + 3) / 2 = 2.5
    给你一个数组 nums，有一个大小为 k 的窗口从最左端滑动到最右端。窗口中有 k 个数，每次窗口向右移动 1 位。
    你的任务是找出每次窗口移动后得到的新窗口中元素的中位数，并输出由它们组成的数组。

    示例：
    给出 nums = [1,3,-1,-3,5,3,6,7]，以及 k = 3。
    窗口位置                      中位数
    ---------------               -----
    [1  3  -1] -3  5  3  6  7       1
     1 [3  -1  -3] 5  3  6  7      -1
     1  3 [-1  -3  5] 3  6  7      -1
     1  3  -1 [-3  5  3] 6  7       3
     1  3  -1  -3 [5  3  6] 7       5
     1  3  -1  -3  5 [3  6  7]      6
     因此，返回该滑动窗口的中位数数组 [1,-1,-1,3,5,6]。

    提示：
    你可以假设 k 始终有效，即：k 始终小于输入的非空数组的元素个数。
    与真实值误差在 10 ^ -5 以内的答案将被视作正确答案。
"""
import bisect
from typing import List


class Solution:
    # 5216ms, 16.1MB
    @staticmethod
    def median_sliding_window(nums: List[int], k: int) -> List[float]:
        res = []
        for i in range(len(nums) - k + 1):
            slide = nums[i:i + k]
            slide.sort()
            middle = slide[k // 2] if k % 2 else (slide[k // 2-1] + slide[k // 2]) / 2
            res.append(middle)

        return res

    # 96ms, 16.1MB
    @staticmethod
    def median_sliding_window_v2(nums: List[int], k: int) -> List[float]:
        arr = [0] + sorted(nums[:k - 1])
        n = len(nums)
        left_i = 0
        odd = True if k % 2 else False
        a, b = k // 2 - 1, k // 2
        rst = []
        for i in range(n - k + 1):
            arr.pop(left_i)
            bisect.insort(arr, nums[i + k - 1])
            left_i = bisect.bisect_left(arr, nums[i])
            if odd:
                rst.append(arr[b])
            else:
                rst.append((arr[a] + arr[b]) / 2)
        return rst


if __name__ == '__main__':
    test_cases = [
        ([1, 3, -1, -3, 5, 3, 6, 7], 3),
        ([1, 4, 2, 3], 4)
    ]
    for tc in test_cases:
        print(Solution.median_sliding_window(*tc))
        print(Solution.median_sliding_window_v2(*tc))
