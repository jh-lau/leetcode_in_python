"""
  @Author       : liujianhan
  @Date         : 2020/9/16 10:23
  @Project      : leetcode_in_python
  @FileName     : 316.去除重复字母(H).py
  @Description  : 给你一个仅包含小写字母的字符串，请你去除字符串中重复的字母，使得每个字母只出现一次。
  需保证返回结果的字典序最小（要求不能打乱其他字符的相对位置）。

    示例 1:

    输入: "bcabc"
    输出: "abc"
    示例 2:

    输入: "cbacdcbc"
    输出: "acdb"
"""


class Solution:
    # 160ms, 13.4MB
    @staticmethod
    def remove_duplicate_letters(s: str) -> str:
        stack = []
        remain_counter = {c: s.count(c) for c in s}
        for c in s:
            if c not in stack:
                while stack and c < stack[-1] and remain_counter[stack[-1]] > 0:
                    stack.pop()
                stack.append(c)
            remain_counter[c] -= 1

        return ''.join(stack)


if __name__ == '__main__':
    test_cases = [
        'bcabc', 'cbacdcbc'
    ]
    for tc in test_cases:
        print(Solution.remove_duplicate_letters(tc))
