"""
  @Author       : liujianhan
  @Date         : 2020/4/8 下午5:46
  @Project      : leetcode_in_python
  @FileName     : 01.06.字符串压缩.py
  @Description  : 字符串压缩。利用字符重复出现的次数，编写一种方法，实现基本的字符串压缩功能。比如，字符串aabcccccaaa会变为a2b1c5a3。
  若“压缩”后的字符串没有变短，则返回原先的字符串。你可以假设字符串中只包含大小写英文字母（a至z）。
    示例1:

     输入："aabcccccaaa"
     输出："a2b1c5a3"
    示例2:

     输入："abbccd"
     输出："abbccd"
     解释："abbccd"压缩后为"a1b2c2d1"，比原字符串长度更长。

     同类型题：字符串->443题
"""


class Solution:
    # 72ms, 13.9MB
    @classmethod
    def compress_string(cls, s: str) -> str:
        if not s:
            return s
        index, cnt = 0, 1
        res = ''
        while index < len(s) - 1:
            if s[index] == s[index + 1]:
                cnt += 1
            else:
                res += f'{s[index]}{cnt}'
                cnt = 1
            index += 1
        res += f'{s[index]}{cnt}'
        return res if len(res) < len(s) else s

    # 44ms, 13.6MB
    @classmethod
    def compress_string_v2(cls, s: str) -> str:
        res = ""
        if len(s) <= 2:
            return s
        flag = s[0]
        count = 0
        for char in s:
            if char == flag:
                count += 1
            else:
                res += flag + str(count)
                flag = char
                count = 1
        res += flag + str(count)
        if len(s) <= len(res):
            return s
        return res


if __name__ == '__main__':
    test_cases = ['aabcccccaaa', 'abbccd', '']
    for tc in test_cases:
        print(Solution.compress_string(tc))
        print(Solution.compress_string_v2(tc))
