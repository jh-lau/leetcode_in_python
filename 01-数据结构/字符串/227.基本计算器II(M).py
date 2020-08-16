"""
  @Author       : liujianhan
  @Date         : 2020/6/28 下午8:00
  @Project      : leetcode_in_python
  @FileName     : 227.基本计算器II(M).py
  @Description  : 实现一个基本的计算器来计算一个简单的字符串表达式的值。
    字符串表达式仅包含非负整数，+， - ，*，/ 四种运算符和空格  。 整数除法仅保留整数部分。
    示例 1:
    输入: "3+2*2"
    输出: 7
    示例 2:
    输入: " 3/2 "
    输出: 1
    示例 3:
    输入: " 3+5 / 2 "
    输出: 5
    说明：
    你可以假设所给定的表达式都是有效的。
    请不要使用内置的库函数 eval。
"""


class Solution:
    # 112ms, 15.4MB
    @staticmethod
    def calculate(s: str) -> int:
        num = 0
        stack = list()
        op = '+'
        for i, c in enumerate(s):
            if c.isnumeric():
                num = num * 10 + int(c)
            if c in '+-*/' or i == len(s) - 1:
                if op == '+':
                    stack.append(num)
                if op == '-':
                    stack.append(-num)
                if op == '*':
                    stack.append(stack.pop() * num)
                if op == '/':
                    stack.append(int(stack.pop() / num))
                op = c
                num = 0
        return sum(stack)


if __name__ == '__main__':
    test_cases = [
        "3+2*2",
        " 3/2 ",
        " 3+5 / 2 "
    ]
    for tc in test_cases:
        print(Solution.calculate(tc))
