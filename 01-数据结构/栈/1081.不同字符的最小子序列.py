"""
  @Author       : liujianhan
  @Date         : 2020/9/16 11:05
  @Project      : leetcode_in_python
  @FileName     : 1081.不同字符的最小子序列.py
  @Description  : 返回字符串 text 中按字典序排列最小的子序列，该子序列包含 text 中所有不同字符一次。（同316题目）
    示例 1：

    输入："cdadabcc"
    输出："adbc"
    示例 2：

    输入："abcd"
    输出："abcd"
    示例 3：

    输入："ecbacba"
    输出："eacb"
    示例 4：

    输入："leetcode"
    输出："letcod"
     

    提示：

    1 <= text.length <= 1000
    text 由小写英文字母组成
"""


class Solution:
    # 48ms, 13.3MB
    @staticmethod
    def smallest_subsequence(s: str) -> str:
        stack = []
        remain_counter = {c: s.count(c) for c in s}
        for c in s:
            if c not in stack:
                while stack and c < stack[-1] and remain_counter[stack[-1]] > 0:
                    stack.pop()
                stack.append(c)
            remain_counter[c] -= 1

        return ''.join(stack)