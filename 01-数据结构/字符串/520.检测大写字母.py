"""
  @Author       : Liujianhan
  @Date         : 20/4/5 13:05
  @FileName     : 520.检测大写字母.py
  @ProjectName  : leetcode_in_python
  @Description  : 给定一个单词，你需要判断单词的大写使用是否正确。
    我们定义，在以下情况时，单词的大写用法是正确的：
    全部字母都是大写，比如"USA"。
    单词中所有字母都不是大写，比如"leetcode"。
    如果单词不只含有一个字母，只有首字母大写， 比如 "Google"。
    否则，我们定义这个单词没有正确使用大写字母。

    输入: "USA"
    输出: True
    输入: "FlaG"
    输出: False
 """


class Solution:
    # 36ms, 13.6MB
    @classmethod
    def detect_capital_use(cls, word: str) -> bool:
        return word.isupper() or word.islower() or word.istitle()


if __name__ == '__main__':
    test_cases = ['USA', 'FlaG', 'Google', 'leetcode']
    for tc in test_cases:
        print(tc, Solution.detect_capital_use(tc))
