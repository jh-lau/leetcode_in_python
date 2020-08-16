"""
  @Author       : Liujianhan
  @Date         : 20/4/4 23:18
  @FileName     : 443.压缩字符串.py
  @ProjectName  : leetcode_in_python
  @Description  : 给定一组字符，使用原地算法将其压缩。
    压缩后的长度必须始终小于或等于原数组长度。
    数组的每个元素应该是长度为1 的字符（不是 int 整数类型）。
    在完成原地修改输入数组后，返回数组的新长度。
    进阶：
    你能否仅使用O(1) 空间解决问题？

    输入：
    ["a","a","b","b","c","c","c"]
    输出：
    返回6，输入数组的前6个字符应该是：["a","2","b","2","c","3"]
    说明：
    "aa"被"a2"替代。"bb"被"b2"替代。"ccc"被"c3"替代
    ["a"]
    输出：
    返回1，输入数组的前1个字符应该是：["a"]
    说明：
    没有任何字符串被替代。
 """
from typing import List


class Solution:
    # not here
    @classmethod
    def compress(cls, chars: List[str]) -> int:
        count_dic = {char: chars.count(char) for char in chars}
        single = len([k for k, v in count_dic.items() if v == 1])
        multiple = sum([len(str(v)) + len(k) for k, v in count_dic.items() if v > 1])
        return single + multiple

    # 76ms, 13.9MB
    @classmethod
    def compress_v2(cls, chars: List[str]) -> int:
        anchor = write = 0
        for read, c in enumerate(chars):
            if read + 1 == len(chars) or chars[read + 1] != c:
                chars[write] = chars[anchor]
                write += 1
                if read > anchor:
                    for digit in str(read - anchor + 1):
                        chars[write] = digit
                        write += 1
                anchor = read + 1
        return write


if __name__ == '__main__':
    test_cases = [
        ["a", "a", "b", "b", "c", "c", "c"],
        ["a"],
        ["a", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b"]
    ]
    for tc in test_cases:
        print(tc, Solution.compress(tc))
        print(tc, Solution.compress_v2(tc))
