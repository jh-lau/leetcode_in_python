"""
  @Author       : liujianhan
  @Date         : 2020/9/2 10:17
  @Project      : leetcode_in_python
  @FileName     : 20.表示数值的字符串(M).py
  @Description  : 请实现一个函数用来判断字符串是否表示数值（包括整数和小数）。例如，
  字符串"+100"、"5e2"、"-123"、"3.1416"、"-1E-16"、"0123"都表示数值，
  但"12e"、"1a3.14"、"1.2.3"、"+-5"及"12e+5.4"都不是。
"""


class Solution:
    # 48ms, 13.6MB
    @staticmethod
    def is_number(s: str) -> bool:
        states = [
            {' ': 0, 's': 1, 'd': 2, '.': 4},  # 0. start with 'blank'
            {'d': 2, '.': 4},  # 1. 'sign' before 'e'
            {'d': 2, '.': 3, 'e': 5, ' ': 8},  # 2. 'digit' before 'dot'
            {'d': 3, 'e': 5, ' ': 8},  # 3. 'digit' after 'dot'
            {'d': 3},  # 4. 'digit' after 'dot' (‘blank’ before 'dot')
            {'s': 6, 'd': 7},  # 5. 'e'
            {'d': 7},  # 6. 'sign' after 'e'
            {'d': 7, ' ': 8},  # 7. 'digit' after 'e'
            {' ': 8}  # 8. end with 'blank'
        ]
        p = 0  # start with state 0
        for c in s:
            if '0' <= c <= '9':
                t = 'd'  # digit
            elif c in "+-":
                t = 's'  # sign
            elif c in "eE":
                t = 'e'  # e or E
            elif c in ". ":
                t = c  # dot, blank
            else:
                t = '?'  # unknown
            if t not in states[p]: return False
            p = states[p][t]
        return p in (2, 3, 7, 8)


if __name__ == '__main__':
    test_cases = [
        "+100", "5e2", "-123", "3.1416", "-1E-16", "0123",
        "12e", "1a3.14", "1.2.3", "+-5", "12e+5.4"
    ]
    for tc in test_cases:
        print(tc, Solution.is_number(tc))
