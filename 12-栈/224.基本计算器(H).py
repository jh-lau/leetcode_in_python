"""
  @Author       : Liujianhan
  @Date         : 20/6/27 9:37
  @FileName     : 224.基本计算器(H).py
  @ProjectName  : leetcode_in_python
  @Description  : 实现一个基本的计算器来计算一个简单的字符串表达式的值。
    字符串表达式可以包含左括号 ( ，右括号 )，加号 + ，减号 -，非负整数和空格  。
    示例 1:
    输入: "1 + 1"
    输出: 2
    示例 2:
    输入: " 2-1 + 2 "
    输出: 3
    示例 3:
    输入: "(1+(4+5+2)-3)+(6+8)"
    输出: 23
    说明：
    你可以假设所给定的表达式都是有效的。
    请不要使用内置的库函数 eval。
 """


class Solution:
    # 104ms, 13.8MB
    @staticmethod
    def calculate(s: str) -> int:
        stack = []
        operand = 0
        res = 0
        sign = 1

        for ch in s:
            if ch.isdigit():
                operand = (operand * 10) + int(ch)
            elif ch == '+':
                res += sign * operand
                sign, operand = 1, 0
            elif ch == '-':
                res += sign * operand
                sign, operand = -1, 0
            elif ch == '(':
                stack.append(res)
                stack.append(sign)
                sign, res = 1, 0
            elif ch == ')':
                res += sign * operand
                res *= stack.pop()
                res += stack.pop()
                operand = 0

        return res + sign * operand


if __name__ == '__main__':
    test_cases = [
        "1 + 1",
        " 2-1 + 2 ",
        "(1+(4+5+2)-3)+(6+8)",
        "1-(5)"
    ]
    for tc in test_cases:
        print(Solution.calculate(tc))
