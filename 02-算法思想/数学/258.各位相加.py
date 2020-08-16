"""
  @Author       : liujianhan
  @Date         : 2020/7/13 下午8:19
  @Project      : leetcode_in_python
  @FileName     : 258.各位相加.py
  @Description  : 给定一个非负整数 num，反复将各个位上的数字相加，直到结果为一位数。
    示例:
    输入: 38
    输出: 2
    解释: 各位相加的过程为：3 + 8 = 11, 1 + 1 = 2。 由于 2 是一位数，所以返回 2。
    进阶:
    你可以不使用循环或者递归，且在 O(1) 时间复杂度内解决这个问题吗？
"""


class Solution:
    # 36ms, 13.6MB
    @staticmethod
    def add_digits(num: int) -> int:
        if num == 0:
            return 0
        if num % 9 == 0:
            return 9
        else:
            return num % 9


if __name__ == '__main__':
    print(Solution.add_digits(38))