"""
  @Author       : Liujianhan
  @Date         : 20/4/6 0:27
  @FileName     : 72.编辑距离(H).py
  @ProjectName  : leetcode_in_python
  @Description  : 给你两个单词 word1 和 word2，请你计算出将 word1 转换成 word2 所使用的最少操作数 。
    你可以对一个单词进行如下三种操作：
    插入一个字符
    删除一个字符
    替换一个字符
    示例 1：

    输入：word1 = "horse", word2 = "ros"
    输出：3
    解释：
    horse -> rorse (将 'h' 替换为 'r')
    rorse -> rose (删除 'r')
    rose -> ros (删除 'e')
    示例 2：

    输入：word1 = "intention", word2 = "execution"
    输出：5
    解释：
    intention -> inention (删除 't')
    inention -> enention (将 'i' 替换为 'e')
    enention -> exention (将 'n' 替换为 'x')
    exention -> exection (将 'n' 替换为 'c')
    exection -> execution (插入 'u')
 """
from collections import deque


class Solution:
    # 196ms, 17.4MB
    @classmethod
    def min_distance(cls, word1: str, word2: str) -> int:
        n1 = len(word1)
        n2 = len(word2)
        dp = [[0] * (n2 + 1) for _ in range(n1 + 1)]
        for j in range(1, n2 + 1):
            dp[0][j] = dp[0][j - 1] + 1
        for i in range(1, n1 + 1):
            dp[i][0] = dp[i - 1][0] + 1
        for i in range(1, n1 + 1):
            for j in range(1, n2 + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = min(dp[i][j - 1], dp[i - 1][j], dp[i - 1][j - 1]) + 1
        return dp[-1][-1]

    # 64ms, 13.7MB
    @classmethod
    def min_distance_v2(cls, word1: str, word2: str) -> int:
        visit, dq = set(), deque([(word1, word2, 0)])
        while True:
            w1, w2, d = dq.popleft()
            if (w1, w2) not in visit:
                if w1 == w2:
                    return d
                visit.add((w1, w2))
                while w1 and w2 and w1[0] == w2[0]:
                    w1, w2 = w1[1:], w2[1:]
                d += 1
                dq.extend([(w1[1:], w2[1:], d), (w1, w2[1:], d),
                           (w1[1:], w2, d)])


if __name__ == '__main__':
    test_cases = [('horse', 'ros'), ('intention', 'execution')]
    for tc in test_cases:
        print(f'{tc[0]} -> {tc[1]}', Solution.min_distance(*tc))
        print(f'{tc[0]} -> {tc[1]}', Solution.min_distance_v2(*tc))
        print()
