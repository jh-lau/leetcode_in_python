"""
  @Author       : liujianhan
  @Date         : 2020/4/8 下午6:45
  @Project      : leetcode_in_python
  @FileName     : 709.转换成小写字母.py
  @Description  : 实现函数 ToLowerCase()，该函数接收一个字符串参数 str，并将该字符串中的大写字母转换成小写字母，之后返回新的字符串。
    示例 1：

    输入: "Hello"
    输出: "hello"
    示例 2：

    输入: "here"
    输出: "here"
    示例 3：

    输入: "LOVELY"
    输出: "lovely"
"""


class Solution:
    # 44ms, 13.6MB
    @classmethod
    def to_lower_case(cls, str: str) -> str:
        return str.lower()

    # 52ms, 13.6MB
    @classmethod
    def to_lower_case_v2(cls, str: str) -> str:
        new_str = ''
        for char in str:
            if ord(char) in range(65, 91):
                new_str += chr(ord(char) + 32)
            else:
                new_str += char

        return new_str


if __name__ == '__main__':
    test_cases = ['Hllo', 'WORLD', 'Why so Serious!']
    for tc in test_cases:
        print(Solution.to_lower_case(tc))
        print(Solution.to_lower_case_v2(tc))
