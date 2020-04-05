"""
  @Author       : Liujianhan
  @Date         : 20/4/5 18:00
  @FileName     : 557.反转字符串中的单词 II.py
  @ProjectName  : leetcode_in_python
  @Description  : 给定一个字符串，你需要反转字符串中每个单词的字符顺序，同时仍保留空格和单词的初始顺序。
    示例 1:
    输入: "Let's take LeetCode contest"
    输出: "s'teL ekat edoCteeL tsetnoc" 
    注意：在字符串中，每个单词由单个空格分隔，并且字符串中不会有任何额外的空格。
 """


class Solution:
    # 40ms, 14.3MB
    @classmethod
    def revers_words(cls, s: str) -> str:
        return ' '.join([t[::-1] for t in s.split()])

    # 52ms, 14.2MB
    @classmethod
    def revers_words_v2(cls, s: str) -> str:
        return ' '.join(s.split()[::-1])[::-1]


if __name__ == '__main__':
    test_cases = [
        "Let's take LeetCode contest"
    ]
    for tc in test_cases:
        print(tc, Solution.revers_words(tc))
        print(tc, Solution.revers_words_v2(tc))
