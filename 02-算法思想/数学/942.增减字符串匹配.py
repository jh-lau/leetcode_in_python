"""
  @Author       : liujianhan
  @Date         : 2020/11/27 10:51
  @Project      : leetcode_in_python
  @FileName     : 942.增减字符串匹配.py
  @Description  : 给定只含 "I"（增大）或 "D"（减小）的字符串 S ，令 N = S.length。
    返回 [0, 1, ..., N] 的任意排列 A 使得对于所有 i = 0, ..., N-1，都有：
    如果 S[i] == "I"，那么 A[i] < A[i+1]
    如果 S[i] == "D"，那么 A[i] > A[i+1]
    示例 1：
    输入："IDID"
    输出：[0,4,1,3,2]
    示例 2：
    输入："III"
    输出：[0,1,2,3]
    示例 3：
    输入："DDI"
    输出：[3,2,0,1]
    提示：
    1 <= S.length <= 10000
    S 只包含字符 "I" 或 "D"。
"""
from typing import List


class Solution:
    # 64ms, 14.4MB
    @staticmethod
    def di_string_match(S: str) -> List[int]:
        low = 0
        high = len(S)
        result = []
        for s in S:
            if s == 'I':
                result.append(low)
                low += 1
            else:
                result.append(high)
                high -= 1
        result.append(high)

        return result

    # 72ms, 14.7MB
    @staticmethod
    def di_string_match_v2(S: str) -> List[int]:
        low = 0
        high = len(S)
        result = [0 for _ in range(high+1)]
        for i, s in enumerate(S):
            if s == 'I':
                result[i] = low
                low += 1
            else:
                result[i] = high
                high -= 1
        result[-1] = low

        return result


if __name__ == '__main__':
    test_cases = [
        'IDID', 'III', 'DDI'
    ]
    for tc in test_cases:
        print(Solution.di_string_match(tc))
        print(Solution.di_string_match_v2(tc))
