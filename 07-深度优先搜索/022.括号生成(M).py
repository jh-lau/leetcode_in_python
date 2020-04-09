"""
  @Author       : liujianhan
  @Date         : 2020/4/9 上午10:08
  @Project      : leetcode_in_python
  @FileName     : 022.括号生成(M).py
  @Description  : 数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。
    示例：

    输入：n = 3
    输出：[
           "((()))",
           "(()())",
           "(())()",
           "()(())",
           "()()()"
         ]
"""
from typing import List


class Solution:
    # 40ms, 13.7MB
    @classmethod
    def generate_parenthesis(cls, n: int) -> List[str]:
        res = []
        cur_str = ''

        def dfs(cur_str, left, right):
            """
            @param cur_str: 从根节点到叶子节点的路径字符串
            @param left: 左括号还可以使用的数量
            @param right: 右括号还可以使用的数量
            @return:
            """
            if not left and not right:
                res.append(cur_str)
                return
            if right < left:
                return
            if left > 0:
                dfs(cur_str + '(', left - 1, right)
            if right > 0:
                dfs(cur_str + ')', left, right - 1)

        dfs(cur_str, n, n)

        return res

    # 48ms, 13.8MB
    @classmethod
    def generate_parenthesis_v2(cls, n: int) -> List[str]:
        if not n:
            return []
        dp = [None for _ in range(n + 1)]
        dp[0] = ['']

        for i in range(1, n + 1):
            cur = []
            for j in range(i):
                left = dp[j]
                right = dp[i - j - 1]
                for s1 in left:
                    for s2 in right:
                        cur.append(f'({s1}){s2}')
            dp[i] = cur

        return dp[n]


if __name__ == '__main__':
    for tc in range(2, 5):
        print(tc, Solution.generate_parenthesis(tc))
        print(tc, Solution.generate_parenthesis_v2(tc))
