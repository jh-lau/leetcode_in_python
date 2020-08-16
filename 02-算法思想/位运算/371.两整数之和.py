"""
  @Author       : Liujianhan
  @Date         : 20/8/9 13:31
  @FileName     : 371.两整数之和.py
  @ProjectName  : leetcode_in_python
  @Description  : 不使用运算符 + 和 - ​​​​​​​，计算两整数 ​​​​​​​a 、b ​​​​​​​之和。

    示例 1:

    输入: a = 1, b = 2
    输出: 3
    示例 2:

    输入: a = -2, b = 3
    输出: 1
    通过次数33,804提交次数60,727
 """


class Solution:
    # 56ms, 13.6MB
    @staticmethod
    def get_sum(a: int, b: int) -> int:
        a &= 0xFFFFFFFF
        b &= 0xFFFFFFFF
        while b:
            carry = a & b
            a ^= b
            b = (carry << 1) & 0xFFFFFFFF
        return a if a < 0x80000000 else ~(a ^ 0xFFFFFFFF)


if __name__ == '__main__':
    test_cases = [
        (1, 2),
        (-2, 3)
    ]
    for tc in test_cases:
        print(Solution.get_sum(*tc))
