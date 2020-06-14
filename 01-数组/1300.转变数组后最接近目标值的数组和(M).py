"""
  @Author       : Liujianhan
  @Date         : 20/6/14 19:30
  @FileName     : 1300.转变数组后最接近目标值的数组和(M).py
  @ProjectName  : leetcode_in_python
  @Description  : 给你一个整数数组 arr 和一个目标值 target ，请你返回一个整数 value ，使得将数组中所有大于 value 的值变成 value 后，数组的和最接近  target （最接近表示两者之差的绝对值最小）。
    如果有多种使得和最接近 target 的方案，请你返回这些整数中的最小值。
    请注意，答案不一定是 arr 中的数字。
    示例 1：
    输入：arr = [4,9,3], target = 10
    输出：3
    解释：当选择 value 为 3 时，数组会变成 [3, 3, 3]，和为 9 ，这是最接近 target 的方案。
    示例 2：
    输入：arr = [2,3,5], target = 10
    输出：5
    示例 3：
    输入：arr = [60864,25176,27249,21296,20204], target = 56803
    输出：11361
 """
from typing import List


class Solution:
    # 64ms, 14.8MB
    @classmethod
    def find_best_value(cls, arr: List[int], target: int) -> int:
        _sum = sum(arr)
        if _sum <= target:
            return max(arr)
        l = len(arr)
        val = target // l
        _sum, last = val * l, 0
        while _sum < target:
            last = _sum
            _sum = 0
            for i in range(l):
                _sum += arr[i] if val > arr[i] else val
            val += 1
        return val - 2 if abs(target - _sum) >= abs(target - last) else val - 1


if __name__ == '__main__':
    test_cases = [
        ([4, 9, 3], 10),
        ([2, 3, 5], 10),
        ([60864, 25176, 27249, 21296, 20204], 56803)
    ]
    for tc in test_cases:
        print(Solution.find_best_value(*tc))
