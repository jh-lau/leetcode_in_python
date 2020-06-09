"""
  @Author       : liujianhan
  @Date         : 2020/6/9 下午5:47
  @Project      : leetcode_in_python
  @FileName     : 46.把数字翻译成字符串(M).py
  @Description  : 给定一个数字，我们按照如下规则把它翻译为字符串：0 翻译成 “a” ，1 翻译成 “b”，……，11 翻译成 “l”，……，25 翻译成 “z”。一个数字可能有多个翻译。请编程实现一个函数，用来计算一个数字有多少种不同的翻译方法。
    示例 1:
    输入: 12258
    输出: 5
    解释: 12258有5种不同的翻译，分别是"bccfi", "bwfi", "bczi", "mcfi"和"mzi"
"""


class Solution:
    # 40ms, 13.5MB
    @classmethod
    def translate_num(cls, num: int) -> str:
        a = b = 1
        y = num % 10
        while num:
            num //= 10
            x = num % 10
            a, b = (a + b if 10 <= 10 * x + y <= 25 else a), a
            y = x
        return a


if __name__ == '__main__':
    print(Solution.translate_num(12258))
