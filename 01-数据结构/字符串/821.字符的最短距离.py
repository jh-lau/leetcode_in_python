"""
  @Author       : liujianhan
  @Date         : 2020/12/2 14:24
  @Project      : leetcode_in_python
  @FileName     : 821.字符的最短距离.py
  @Description  : 给定一个字符串 S 和一个字符 C。返回一个代表字符串 S 中每个字符到字符串 S 中的字符 C 的最短距离的数组。
    示例 1:
    输入: S = "loveleetcode", C = 'e'
    输出: [3, 2, 1, 0, 1, 0, 0, 1, 2, 2, 1, 0]
    说明:
    字符串 S 的长度范围为 [1, 10000]。
    C 是一个单字符，且保证是字符串 S 里的字符。
    S 和 C 中的所有字母均为小写字母。
"""
from typing import List


class Solution:
    # 72ms, 13.7MB
    @staticmethod
    def shortest_to_char(S: str, C: str) -> List[int]:
        c_index = [i for i, char in enumerate(S) if char == C]
        result = []
        for i in range(len(S)):
            result.append(min([abs(i-j) for j in c_index]))
        return result

    # 48ms, 13.6MB
    @staticmethod
    def shortest_to_char_v2(S: str, C: str) -> List[int]:
        left = 0
        result = [float('inf') for i in S]

        for right in range(len(S)):
            if S[right] is C:
                for i in range(left, right + 1):
                    result[i] = min(result[i], right - i)
                left = right
            elif S[left] is C:
                result[right] = min(result[right], right - left)

        return result


if __name__ == '__main__':
    test_cases = [
        ['loveleetcode', 'e']
    ]
    for tc in test_cases:
        print(Solution.shortest_to_char(*tc))
