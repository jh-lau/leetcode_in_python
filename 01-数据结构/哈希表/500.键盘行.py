"""
  @Author       : liujianhan
  @Date         : 2020/11/10 10:49
  @Project      : leetcode_in_python
  @FileName     : 500.键盘行.py
  @Description  : 给定一个单词列表，只返回可以使用在键盘同一行的字母打印出来的单词。键盘如下图所示。
    示例：

    输入: ["Hello", "Alaska", "Dad", "Peace"]
    输出: ["Alaska", "Dad"]
    注意：

    你可以重复使用键盘上同一字符。
    你可以假设输入的字符串将只包含字母。
"""
from typing import List


class Solution:
    # 32ms, 13.6MB
    @staticmethod
    def find_words(words: List[str]) -> List[str]:
        lookup = {
            1: 'QWERTYUIOP',
            2: 'ASDFGHJKL',
            3: 'ZXCVBNM'
        }
        new_lookup = {char: k for k, v in lookup.items() for char in v}
        for word in words[:]:
            if len(set([new_lookup[s] for s in word.upper()])) > 1:
                words.remove(word)
        return words


if __name__ == '__main__':
    test_cases = [
        ["Hello", "Alaska", "Dad", "Peace"]
    ]
    for tc in test_cases:
        print(Solution.find_words(tc))
