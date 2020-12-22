"""
  @Author       : liujianhan
  @Date         : 2020/12/22 10:03
  @Project      : leetcode_in_python
  @FileName     : 717.1比特与2比特字符.py
  @Description  : 有两种特殊字符。第一种字符可以用一比特0来表示。第二种字符可以用两比特(10 或 11)来表示。
    现给一个由若干比特组成的字符串。问最后一个字符是否必定为一个一比特字符。给定的字符串总是由0结束。

    示例 1:
    输入:
    bits = [1, 0, 0]
    输出: True
    解释:
    唯一的编码方式是一个两比特字符和一个一比特字符。所以最后一个字符是一比特字符。

    示例 2:
    输入:
    bits = [1, 1, 1, 0]
    输出: False
    解释:
    唯一的编码方式是两比特字符和两比特字符。所以最后一个字符不是一比特字符。
    注意:

    1 <= len(bits) <= 1000.
    bits[i] 总是0 或 1.
"""
from typing import List


class Solution:
    # 80ms, 14.9MB
    @staticmethod
    def is_one_bit_character(bits: List[int]) -> bool:
        while len(bits) > 1:
            if bits[0] == 0:
                bits = bits[1:]
            else:
                bits = bits[2:]
        if bits == [0]:
            return True
        else:
            return False


if __name__ == '__main__':
    test_cases = [
        [1, 0, 0],
        [1, 1, 1, 0]
    ]
    for tc in test_cases:
        print(Solution.is_one_bit_character(tc))
