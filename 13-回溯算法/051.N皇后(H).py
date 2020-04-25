"""
  @Author       : Liujianhan
  @Date         : 20/4/25 16:47
  @FileName     : 051.N皇后(H).py
  @ProjectName  : leetcode_in_python
  @Description  : n 皇后问题研究的是如何将 n 个皇后放置在 n×n 的棋盘上，并且使皇后彼此之间不能相互攻击。
    给定一个整数 n，返回所有不同的 n 皇后问题的解决方案。
    每一种解法包含一个明确的 n 皇后问题的棋子放置方案，该方案中 'Q' 和 '.' 分别代表了皇后和空位。

    示例:

    输入: 4
    输出: [
     [".Q..",  // 解法 1
      "...Q",
      "Q...",
      "..Q."],

     ["..Q.",  // 解法 2
      "Q...",
      "...Q",
      ".Q.."]
    ]
    解释: 4 皇后问题存在两个不同的解法。
 """
from typing import List


class Solution:
    # 72ms, 14.2MB
    @classmethod
    def solve_n_queens(cls, n: int) -> List[List[str]]:
        def could_place(row, col):
            return not (cols[col] + hill_diagonals[row - col] + dale_diagonals[row + col])

        def place_queen(row, col):
            queens.add((row, col))
            cols[col] = 1
            hill_diagonals[row - col] = 1
            dale_diagonals[row + col] = 1

        def remove_queen(row, col):
            queens.remove((row, col))
            cols[col] = 0
            hill_diagonals[row - col] = 0
            dale_diagonals[row + col] = 0

        def add_solution():
            solution = []
            for _, col in sorted(queens):
                solution.append('.' * col + 'Q' + '.' * (n - col - 1))
            output.append(solution)

        def backtrack(row=0):
            for col in range(n):
                if could_place(row, col):
                    place_queen(row, col)
                    if row + 1 == n:
                        add_solution()
                    else:
                        backtrack(row + 1)
                    remove_queen(row, col)

        cols = [0] * n
        hill_diagonals = [0] * (2 * n - 1)
        dale_diagonals = [0] * (2 * n - 1)
        queens = set()
        output = []
        backtrack()

        return output

    # 60ms, 14MB
    @classmethod
    def solve_n_queens_v2(cls, n: int) -> List[List[str]]:
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

        return [["." * i + "Q" + "." * (n - i - 1) for i in sol] for sol in res]


if __name__ == '__main__':
    test_cases = [4, 6, 7, 8]
    for tc in test_cases:
        print(Solution.solve_n_queens(tc))
        print(Solution.solve_n_queens_v2(tc))
