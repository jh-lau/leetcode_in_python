"""
  @Author       : Liujianhan
  @Date         : 20/5/24 19:03
  @FileName     : 166.分数到小数(M).py
  @ProjectName  : leetcode_in_python
  @Description  : 给定两个整数，分别表示分数的分子 numerator 和分母 denominator，以字符串形式返回小数。
    如果小数部分为循环小数，则将循环的部分括在括号内。
    示例 1:
    输入: numerator = 1, denominator = 2
    输出: "0.5"
    示例 2:
    输入: numerator = 2, denominator = 1
    输出: "2"
    示例 3:
    输入: numerator = 2, denominator = 3
    输出: "0.(6)"
 """


class Solution:
    # 40ms, 13.5MB
    @classmethod
    def fraction_to_decimal(cls, numerator: int, denominator: int) -> str:
        if numerator == 0:
            return '0'
        res = []
        if (numerator > 0) ^ (denominator > 0):
            res.append('-')
        numerator, denominator = abs(numerator), abs(denominator)
        a, b = divmod(numerator, denominator)
        res.append(str(a))

        if b == 0:
            return ''.join(res)
        res.append('.')
        loc = {b: len(res)}
        while b:
            b *= 10
            a, b = divmod(b ,denominator)
            res.append(str(a))
            if b in loc:
                res.insert(loc[b], '(')
                res.append(')')
                break
            loc[b] = len(res)

        return ''.join(res)


if __name__ == '__main__':
    test_cases = [
        (1, 2), (2, 1), (2, 3)
    ]
    for tc in test_cases:
        print(tc, Solution.fraction_to_decimal(*tc))
