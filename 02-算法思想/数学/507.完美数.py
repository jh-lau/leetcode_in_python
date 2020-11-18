"""
  @Author       : liujianhan
  @Date         : 2020/11/18 11:09
  @Project      : leetcode_in_python
  @FileName     : 507.完美数.py
  @Description  : 对于一个 正整数，如果它和除了它自身以外的所有 正因子 之和相等，我们称它为 「完美数」。
    给定一个 整数 n， 如果是完美数，返回 true，否则返回 false
    示例 1：

    输入：28
    输出：True
    解释：28 = 1 + 2 + 4 + 7 + 14
    1, 2, 4, 7, 和 14 是 28 的所有正因子。
    示例 2：

    输入：num = 6
    输出：true
    示例 3：

    输入：num = 496
    输出：true
    示例 4：

    输入：num = 8128
    输出：true
    示例 5：

    输入：num = 2
    输出：false
     
    提示：

    1 <= num <= 108
"""
import math


class Solution:
    # 48ms, 13.6MB
    @staticmethod
    def check_perfect_number(num: int) -> bool:
        if num < 4:
            return False
        result = 1
        for i in range(2, int(math.sqrt(num)) + 1):
            if not num % i:
                result += i
                result += num // i
        return result == num


if __name__ == '__main__':
    test_cases = [
        1, 28, 6, 496, 8128, 2, 99999993
    ]
    for tc in test_cases:
        print(Solution.check_perfect_number(tc))
