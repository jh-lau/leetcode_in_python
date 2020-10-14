"""
  @Author       : liujianhan
  @Date         : 2020/10/14 10:07
  @Project      : leetcode_in_python
  @FileName     : 1002.查找常用字符.py
  @Description  : 给定仅有小写字母组成的字符串数组 A，返回列表中的每个字符串中都显示的全部字符（包括重复字符）组成的列表。
    例如，如果一个字符在每个字符串中出现 3 次，但不是 4 次，则需要在最终答案中包含该字符 3 次。
    你可以按任意顺序返回答案。
    示例 1：
    输入：["bella","label","roller"]
    输出：["e","l","l"]

    示例 2：
    输入：["cool","lock","cook"]
    输出：["c","o"]

    提示：
    1 <= A.length <= 100
    1 <= A[i].length <= 100
    A[i][j] 是小写字母
"""
from typing import List
from functools import reduce


class Solution:
    # 48ms, 13.8MB
    @staticmethod
    def common_chars(str_list: List[str]) -> List[str]:
        common_char_set = list(reduce(lambda x, y: set(x) & set(y), str_list))
        first_dict = {s: str_list[0].count(s) for s in common_char_set}
        for string in str_list[1:]:
            for char in common_char_set:
                if string.count(char) < first_dict[char]:
                    first_dict[char] = string.count(char)
        r = []
        for k, v in first_dict.items():
            for _ in range(v):
                r.append(k)

        return r

    # 44ms, 13.7MB
    @staticmethod
    def common_chars_v2(str_list: List[str]) -> List[str]:
        if not str_list:
            return []
        res = []
        key = set(str_list[0])
        for k in key:
            cnt = min(a.count(k) for a in str_list)
            res.extend(k * cnt)

        return res


if __name__ == '__main__':
    test_cases = [
        ["bella", "label", "roller"],
        ["cool", "lock", "cook"],
        ["bbddabab", "cbcddbdd", "bbcadcab", "dabcacad", "cddcacbc", "ccbdbcba", "cbddaccc", "accdcdbb"]
    ]
    for tc in test_cases:
        print(Solution.common_chars(tc))
        print(Solution.common_chars_v2(tc))
