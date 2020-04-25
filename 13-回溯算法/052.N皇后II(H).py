"""
  @Author       : Liujianhan
  @Date         : 20/4/25 16:53
  @FileName     : 052.N皇后II(H).py
  @ProjectName  : leetcode_in_python
  @Description  : n 皇后问题研究的是如何将 n 个皇后放置在 n×n 的棋盘上，并且使皇后彼此之间不能相互攻击。
    给定一个整数 n，返回 n 皇后不同的解决方案的数量。
    示例:
    输入: 4
    输出: 2
    解释: 4 皇后问题存在如下两个不同的解法。
    [
     [".Q..",  // 解法 1
      "...Q",
      "Q...",
      "..Q."],

     ["..Q.",  // 解法 2
      "Q...",
      "...Q",
      ".Q.."]
    ]
 """


class Solution:
    # 36s, 13.6MB
    @classmethod
    def total_queens(cls, n: int) -> int:
        res = 0

        def dfs(n, row, col, ld, rd):
            if row >= n:
                nonlocal res
                res += 1
                return

            bits = ~(col | ld | rd) & ((1 << n) - 1)
            while bits > 0:
                pick = bits & - bits
                dfs(n, row + 1, col | pick, (ld | pick) << 1, (rd | pick) >> 1)
                bits &= bits - 1

        dfs(n, 0, 0, 0, 0)

        return res

    # 56ms, 13.8MB
    @classmethod
    def total_queens_v2(cls, n: int) -> int:
        res = []

        def dfs(queens, xy_dif, xy_sum):
            p = len(queens)
            if p == n:
                res.append(queens)
                return
            for q in range(n):
                if q not in queens and p - q not in xy_dif and p + q not in xy_sum:
                    dfs(queens + [q], xy_dif + [p - q], xy_sum + [p + q])

        dfs([], [], [])

        return len([["." * i + "Q" + "." * (n - i - 1) for i in sol] for sol in res])


if __name__ == '__main__':
    test_cases = [4, 6, 7, 8]
    for tc in test_cases:
        print(Solution.total_queens(tc))
        print(Solution.total_queens_v2(tc))
