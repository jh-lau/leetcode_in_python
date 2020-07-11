"""
  @Author       : liujianhan
  @Date         : 2020/7/11 上午9:52
  @Project      : leetcode_in_python
  @FileName     : 315.计算右侧小于当前元素的个数(H).py
  @Description  : 给定一个整数数组 nums，按要求返回一个新数组 counts。数组 counts 有该性质： counts[i] 的值是  nums[i] 右侧小于 nums[i] 的元素的数量。
    示例:
    输入: [5,2,6,1]
    输出: [2,1,1,0]
    解释:
    5 的右侧有 2 个更小的元素 (2 和 1).
    2 的右侧仅有 1 个更小的元素 (1).
    6 的右侧有 1 个更小的元素 (1).
"""
import bisect
from typing import List


class Solution:
    # 140ms, 17.1MB
    @staticmethod
    def count_smaller(nums: List[int]) -> List[int]:
        sortns = []
        res = []
        for n in reversed(nums):
            idx = bisect.bisect_left(sortns, n)
            res.append(idx)
            sortns.insert(idx, n)
        return res[::-1]


if __name__ == '__main__':
    print(Solution.count_smaller([5, 2, 6, 1]))
