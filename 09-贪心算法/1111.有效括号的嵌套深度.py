"""
  @Author       : liujianhan
  @Date         : 2020/4/1 下午2:03
  @Project      : leetcode_in_python
  @FileName     : 1111.有效括号的嵌套深度.py
  @Description  : 有效括号字符串 定义：对于每个左括号，都能找到与之对应的右括号，反之亦然。详情参见题末「有效括号字符串」部分。
    嵌套深度 depth 定义：即有效括号字符串嵌套的层数。详情参见题末「嵌套深度」部分。
    给你一个「有效括号字符串」 seq，请你将其分成两个不相交的子序列 A 和 B，且 A 和 B 都满足有效括号字符串的定义
    （注意：A.length + B.length = seq.length）。
    由于可能存在多种划分方案，请你从中选出 任意 这样的 A 和 B，使 max(depth(A), depth(B)) 的可能取值最小。
    其中 depth(A) 表示 A 的嵌套深度，depth(B) 表示 B 的嵌套深度。
    请你返回一个长度为 seq.length 的答案数组 answer，编码规则如下：如果 seq[i] 是 A 的一部分，那么 answer[i] = 0。
    否则，answer[i] = 1。即便有多个满足要求的答案存在，你也只需返回 一个。

    输入：seq = "(()())"
    输出：[0,1,1,1,1,0]

    输入：seq = "()(())()"
    输出：[0,0,0,1,1,0,1,1]
    https://leetcode-cn.com/problems/maximum-nesting-depth-of-two-valid-parentheses-strings/solution/you-xiao-gua-hao-de-qian-tao-shen-du-by-leetcode-s/
"""
from typing import List


class Solution:
    # 60ms, 13.8MB
    @classmethod
    def max_depth_after_split(cls, seq: str) -> List[int]:
        ans = []
        d = 0
        for c in seq:
            if c == '(':
                d += 1
                ans.append(d % 2)
            else:
                ans.append(d % 2)
                d -= 1
        return ans


if __name__ == '__main__':
    test_cases = [
        '(()())',
        '()(())()'
    ]
    for tc in test_cases:
        print(Solution.max_depth_after_split(tc))
