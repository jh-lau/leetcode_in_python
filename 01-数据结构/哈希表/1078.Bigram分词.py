"""
  @Author       : liujianhan
  @Date         : 20/12/6 21:01
  @Project      : leetcode_in_python
  @FileName     : 1078.Bigram分词.py
  @Description  : 给出第一个词 first 和第二个词 second，考虑在某些文本 text 中可能以 "first second third" 形式出现的情况，
    其中 second 紧随 first 出现，third 紧随 second 出现。
    对于每种这样的情况，将第三个词 "third" 添加到答案中，并返回答案。
    示例 1：
    输入：text = "alice is a good girl she is a good student", first = "a", second = "good"
    输出：["girl","student"]
    示例 2：
    输入：text = "we will we will rock you", first = "we", second = "will"
    输出：["we","rock"]
    提示：
    1 <= text.length <= 1000
    text 由一些用空格分隔的单词组成，每个单词都由小写英文字母组成
    1 <= first.length, second.length <= 10
    first 和 second 由小写英文字母组成
"""
from typing import List


class Solution:
    # 44ms, 13.5MB
    @staticmethod
    def find_ocurrences(text: str, first: str, second: str) -> List[str]:
        result = []
        text = text.split()
        for i, word in enumerate(text[:-1]):
            if word == first and text[i + 1] == second:
                if i + 2 < len(text):
                    result.append(text[i + 2])

        return result


if __name__ == '__main__':
    test_cases = [
        ("alice is a good girl she is a good student", 'a', 'good'),
        ("we will we will rock you", 'we', 'will'),
        ("jkypmsxd jkypmsxd kcyxdfnoa jkypmsxd kcyxdfnoa jkypmsxd kcyxdfnoa kcyxdfnoa jkypmsxd kcyxdfnoa", "kcyxdfnoa",
         "jkypmsxd")
    ]
    for tc in test_cases:
        print(Solution.find_ocurrences(*tc))
