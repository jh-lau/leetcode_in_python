"""
  @Author       : liujianhan
  @Date         : 2020/9/8 9:32
  @Project      : leetcode_in_python
  @FileName     : 367.有效的完全平方数.py
  @Description  : 给定一个正整数 num，编写一个函数，如果 num 是一个完全平方数，则返回 True，否则返回 False。

    说明：不要使用任何内置的库函数，如  sqrt。

    示例 1：

    输入：16
    输出：True
    示例 2：

    输入：14
    输出：False
"""


class Solution:
    # 44ms, 13.7MB
    @staticmethod
    def is_perfect_square(num: int) -> bool:
        if num < 2:
            return True

        left, right = 2, num // 2

        while left <= right:
            x = left + (right - left) // 2
            guess_squared = x * x
            if guess_squared == num:
                return True
            if guess_squared > num:
                right = x - 1
            else:
                left = x + 1

        return False

    # 36ms, 13.5MB
    @staticmethod
    def is_perfect_square_v2(num: int) -> bool:
        if num < 2:
            return True

        x = num // 2
        while x * x > num:
            x = (x + num // x) // 2
        return x * x == num


if __name__ == '__main__':
    test_cases = [16, 9, 15, 169, 14]
    for tc in test_cases:
        print(Solution.is_perfect_square(tc))
        print(Solution.is_perfect_square_v2(tc))
