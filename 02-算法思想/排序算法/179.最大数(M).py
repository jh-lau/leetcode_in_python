"""
  @Author       : liujianhan
  @Date         : 2020/5/29 上午10:41
  @Project      : leetcode_in_python
  @FileName     : 179.最大数(M).py
  @Description  : 给定一组非负整数，重新排列它们的顺序使之组成一个最大的整数。
    示例 1:
    输入: [10,2]
    输出: 210
    示例 2:
    输入: [3,30,34,5,9]
    输出: 9534330
    说明: 输出结果可能非常大，所以你需要返回一个字符串而不是整数。
"""
from typing import List


class LargerNumKey(str):
    def __lt__(self, other):
        return self + other > other + self


class Solution:
    # 48ms, 13.5MB
    @classmethod
    def largest_number(cls, nums: List[int]) -> str:
        largest_num = ''.join(sorted(map(str, nums), key=LargerNumKey))

        return '0' if largest_num[0] == '0' else largest_num


if __name__ == '__main__':
    test_cases = [
        [10, 2], [3, 30, 34, 5, 9]
    ]
    for tc in test_cases:
        print(Solution.largest_number(tc))
