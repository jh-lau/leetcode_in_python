"""
  @Author       : liujianhan
  @Date         : 2020/1/23 下午2:24
  @Project      : leetcode_in_python
  @FileName     : 058.最后一个单词的长度.py
  @Description  : 给定一个仅包含大小写字母和空格 ' ' 的字符串 s，返回其最后一个单词的长度。
                如果字符串从左向右滚动显示，那么最后一个单词就是最后出现的单词。
                如果不存在最后一个单词，请返回 0 。
                说明：一个单词是指仅由字母组成、不包含任何空格的 最大子字符串。
"""


class Solution:
    # 28ms, 13.2MB
    @staticmethod
    def length_of_last_word(s: str) -> int:
        if not s or s.isspace():
            return 0
        return len(s.split()[-1])

    # 52ms, 13.5MB
    @classmethod
    def length_of_last_word_v2(cls, s:str) -> int:
        s = s.strip()
        if len(s) != 0:
            return len(s.split()[-1])
        else:
            return 0


if __name__ == '__main__':
    print(Solution().length_of_last_word('a '))
    print(Solution.length_of_last_word_v2('a '))