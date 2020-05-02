"""
  @Author       : Liujianhan
  @Date         : 20/5/2 13:14
  @FileName     : 043.字符串相乘(M).py
  @ProjectName  : leetcode_in_python
  @Description  : 给定两个以字符串形式表示的非负整数 num1 和 num2，返回 num1 和 num2 的乘积，它们的乘积也表示为字符串形式。
    示例 1:
    输入: num1 = "2", num2 = "3"
    输出: "6"
    示例 2:
    输入: num1 = "123", num2 = "456"
    输出: "56088"
    说明：
    num1 和 num2 的长度小于110。
    num1 和 num2 只包含数字 0-9。
    num1 和 num2 均不以零开头，除非是数字 0 本身。
    不能使用任何标准库的大数类型（比如 BigInteger）或直接将输入转换为整数来处理
 """


class Solution:
    # 168ms, 13.5MB
    @classmethod
    def multiply(cls, num1: str, num2: str) -> str:
        if num1 == '0' or num2 == '0':
            return '0'
        num1, num2 = num1[::-1], num2[::-1]
        len_sum = len(num1) + len(num2)
        res = [0 for c in range(len_sum)]
        for index2 in range(len(num2)):
            multiplier2 = int(num2[index2])
            for index1 in range(len(num1)):
                multiplier1 = int(num1[index1])
                temp = multiplier2 * multiplier1 + res[index1 + index2]
                if temp >= 10:
                    res[index1 + index2] = temp % 10
                    res[index1 + index2 + 1] += int(temp / 10)
                else:
                    res[index1 + index2] = temp

        res = res[::-1]
        while res and not res[0]:
            del res[0]
        res = [str(c) for c in res]

        return ''.join(res)


if __name__ == '__main__':
    test_cases = [
        ('2', '3'), ('123', '456')
    ]
    for tc in test_cases:
        print(Solution.multiply(*tc))
