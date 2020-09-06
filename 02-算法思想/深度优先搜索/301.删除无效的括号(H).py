"""
  @Author       : liujianhan
  @Date         : 2020/9/3 9:33
  @Project      : leetcode_in_python
  @FileName     : 301.删除无效的括号(H).py
  @Description  : 删除最小数量的无效括号，使得输入的字符串有效，返回所有可能的结果。
    说明: 输入可能包含了除 ( 和 ) 以外的字符。
    示例 1:
    输入: "()())()"
    输出: ["()()()", "(())()"]
    示例 2:

    输入: "(a)())()"
    输出: ["(a)()()", "(a())()"]
    示例 3:

    输入: ")("
    输出: [""]
"""
from typing import List


class Solution:
    # 168ms, 14MB
    @staticmethod
    def remove_invalid_parentheses(s: str) -> List[str]:
        def is_valid(string):  # 判断括号串是否合法
            l_minus_r = 0
            for c in string:
                if c == '(':
                    l_minus_r += 1
                elif c == ')':
                    l_minus_r -= 1
                    if l_minus_r < 0:
                        return False
            return l_minus_r == 0

        level = {s}
        while True:  # BFS
            valid = list(filter(is_valid, level))
            if valid:
                return valid
            level = {s[:i] + s[i + 1:] for s in level for i in range(len(s)) if s[i] in '()'}

    # 40ms, 13.8MB
    @staticmethod
    def remove_invalid_parentheses_v2(s: str) -> List[str]:
        res = []

        def remove(s, ibegin, jbegin, tmp1, tmp2):
            left_p = 0
            right_p = 0
            for i in range(ibegin, len(s)):
                if s[i] == tmp1: left_p += 1
                if s[i] == tmp2: right_p += 1
                if left_p < right_p:
                    for j in range(jbegin, i + 1):
                        if s[j] == tmp2 and (j == jbegin or s[j - 1] != tmp2):
                            remove(s[:j] + s[j + 1:], i, j, tmp1, tmp2)
                    return
            rev = s[::-1]
            if tmp1 == "(":
                remove(rev, 0, 0, ")", "(")
            else:
                res.append(rev)
        remove(s, 0, 0, "(", ")")
        return res


if __name__ == '__main__':
    test_cases = [
        "()())()", "(a)())()", ")("
    ]
    for tc in test_cases:
        print(Solution.remove_invalid_parentheses(tc))
        print(Solution.remove_invalid_parentheses_v2(tc))
