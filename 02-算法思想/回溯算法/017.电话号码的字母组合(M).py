"""
  @Author       : Liujianhan
  @Date         : 20/4/30 22:40
  @FileName     : 017.电话号码的字母组合(M).py
  @ProjectName  : leetcode_in_python
  @Description  : 给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。
    给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。
    输入："23"
    输出：["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
 """
from typing import List


class Solution:
    # 32ms, 13.7MB
    @classmethod
    def letter_combinations(cls, digits: str) -> List[str]:
        phone = {'2': ['a', 'b', 'c'],
                 '3': ['d', 'e', 'f'],
                 '4': ['g', 'h', 'i'],
                 '5': ['j', 'k', 'l'],
                 '6': ['m', 'n', 'o'],
                 '7': ['p', 'q', 'r', 's'],
                 '8': ['t', 'u', 'v'],
                 '9': ['w', 'x', 'y', 'z']}

        def backtrack(combination, next_digits):
            if not len(next_digits):
                output.append(combination)
            else:
                for letter in phone[next_digits[0]]:
                    backtrack(combination + letter, next_digits[1:])

        output = []
        if digits:
            backtrack("", digits)
        return output


if __name__ == '__main__':
    print(Solution.letter_combinations('23'))
