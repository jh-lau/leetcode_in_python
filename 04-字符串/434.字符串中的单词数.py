"""
  @Author       : Liujianhan
  @Date         : 20/4/4 22:55
  @FileName     : 434.字符串中的单词数.py
  @ProjectName  : leetcode_in_python
  @Description  : 统计字符串中的单词个数，这里的单词指的是连续的不是空格的字符。
    请注意，你可以假定字符串里不包括任何不可打印的字符。
    输入: "Hello, my name is John"
    输出: 5
 """


class Solution:
    # 52ms, 13.6MB
    @classmethod
    def count_segments(cls, s: str) -> int:
        res = 0
        for i in range(len(s)):
            if s[i] != " " and (i == 0 or s[i - 1] == " "):
                res += 1
        return res

    # 40ms, 13.7MB
    @classmethod
    def count_segments_v2(cls, s: str) -> int:
        return len(s.split())


if __name__ == '__main__':
    test_cases = [
        '", , , ,        a, eaefa"',
        'a',
        "Hello, my name is John",
        "love live! mu'sic forever",
        "love live! mu'sic forever 'yes",
        "love live! mu'sic forever no' ",
        "The one-hour drama series Westworld is a dark odyssey about the dawn of artificial consciousness and the evolution of sin. Set at the intersection of the near future and the reimagined past, it explores a world in which every human appetite, no matter how noble or depraved, can be indulged."
    ]
    for tc in test_cases:
        print(tc, Solution.count_segments(tc))
        print(tc, Solution.count_segments_v2(tc))
        print()
