"""
  @Author       : liujianhan
  @Date         : 2020/4/7 下午2:24
  @Project      : leetcode_in_python
  @FileName     : 01.03.URL化.py
  @Description  : URL化。编写一种方法，将字符串中的空格全部替换为%20。假定该字符串尾部有足够的空间存放新增字符，并且知道字符串的“真实”长度。
  （注：用Java实现的话，请使用字符数组实现，以便直接在数组上操作。）

    示例1:

     输入："Mr John Smith    ", 13
     输出："Mr%20John%20Smith"
    示例2:

     输入："               ", 5
     输出："%20%20%20%20%20"
    提示：

    字符串长度在[0, 500000]范围内。
"""


class Solution:
    # 72ms, 19.4MB
    @classmethod
    def replace_spaces(cls, s: str, length: int) -> str:
        s = s[:length].replace(' ', '%20')
        return s


if __name__ == '__main__':
    test_cases = [('Mr John Smith', 13), ('         ', 5)]
    for tc in test_cases:
        print(Solution.replace_spaces(*tc))
