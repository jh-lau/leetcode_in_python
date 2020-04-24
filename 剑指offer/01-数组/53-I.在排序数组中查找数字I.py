"""
  @Author       : Liujianhan
  @Date         : 20/4/24 23:33
  @FileName     : 53-I.在排序数组中查找数字I.py
  @ProjectName  : leetcode_in_python
  @Description  : 统计一个数字在排序数组中出现的次数。
    示例 1:
    输入: nums = [5,7,7,8,8,10], target = 8
    输出: 2
    示例 2:
    输入: nums = [5,7,7,8,8,10], target = 6
    输出: 0
    注： 同主站034题。
 """
from typing import List


class Solution:
    # 48ms, 14.5MB
    @classmethod
    def search(cls, nums: List[int], target: int) -> int:
        return nums.count(target)


if __name__ == '__main__':
    test_cases = [
        ([5, 7, 7, 8, 8, 10], 8),
        ([5, 7, 7, 8, 8, 10], 6)
    ]
    for tc in test_cases:
        print(Solution.search(*tc))
