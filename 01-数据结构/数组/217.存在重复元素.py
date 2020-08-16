"""
  @Author       : Liujianhan
  @Date         : 20/6/21 18:20
  @FileName     : 217.存在重复元素.py
  @ProjectName  : leetcode_in_python
  @Description  : 给定一个整数数组，判断是否存在重复元素。
    如果任意一值在数组中出现至少两次，函数返回 true 。如果数组中每个元素都不相同，则返回 false 。
    示例 1:
    输入: [1,2,3,1]
    输出: true
    示例 2:
    输入: [1,2,3,4]
    输出: false
    示例 3:
    输入: [1,1,1,3,3,4,3,2,4,2]
    输出: true
 """
from typing import List


class Solution:
    # 56ms, 19.2MB
    @classmethod
    def contains_duplicate(cls, nums: List[int]) -> bool:
        return len(nums) != len(set(nums))


if __name__ == '__main__':
    test_cases = [
        [1, 2, 3, 1],
        [1, 2, 3, 4],
        [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
    ]
    for tc in test_cases:
        print(Solution.contains_duplicate(tc))