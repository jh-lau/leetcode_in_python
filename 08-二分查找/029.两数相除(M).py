"""
  @Author       : Liujianhan
  @Date         : 20/5/1 16:31
  @FileName     : 029.两数相除(M).py
  @ProjectName  : leetcode_in_python
  @Description  : 给定两个整数，被除数 dividend 和除数 divisor。将两数相除，要求不使用乘法、除法和 mod 运算符。
    返回被除数 dividend 除以除数 divisor 得到的商。
    整数除法的结果应当截去（truncate）其小数部分，例如：truncate(8.345) = 8 以及 truncate(-2.7335) = -2
    示例 1:
    输入: dividend = 10, divisor = 3
    输出: 3
    解释: 10/3 = truncate(3.33333..) = truncate(3) = 3
    示例 2:
    输入: dividend = 7, divisor = -3
    输出: -2
    解释: 7/-3 = truncate(-2.33333..) = -2
    提示：
    被除数和除数均为 32 位有符号整数。
    除数不为 0。
    假设我们的环境只能存储 32 位有符号整数，其数值范围是 [−231,  231 − 1]。本题中，如果除法结果溢出，则返回 231 − 1。
 """


class Solution:
    # 36ms, 13.7MB
    @classmethod
    def divide(cls, dividend: int, divisor: int) -> int:
        sign = 1
        if (dividend < 0) ^ (divisor < 0):
            sign = -1
        dividend = abs(dividend)
        divisor = abs(divisor)
        result = 0

        while dividend >= divisor:
            i = 0
            a = divisor
            while a <= dividend:
                a = a << 1
                i += 1
            result += (1 << (i - 1))
            dividend -= (a >> 1)

        result = result * sign
        if result > 2147483647:
            result = 2147483647

        return result


if __name__ == '__main__':
    test_cases = [(10, 3), (7, -3)]
    for tc in test_cases:
        print(Solution.divide(*tc))
