"""
  @Author       : liujianhan
  @Date         : 2020/4/2 下午4:41
  @Project      : leetcode_in_python
  @FileName     : 289.生命游戏(M).py
  @Description  : 根据 百度百科 ，生命游戏，简称为生命，是英国数学家约翰·何顿·康威在 1970 年发明的细胞自动机。
    给定一个包含 m × n 个格子的面板，每一个格子都可以看成是一个细胞。每个细胞都具有一个初始状态：1 即为活细胞（live），
    或 0 即为死细胞（dead）。每个细胞与其八个相邻位置（水平，垂直，对角线）的细胞都遵循以下四条生存定律：
    如果活细胞周围八个位置的活细胞数少于两个，则该位置活细胞死亡；
    如果活细胞周围八个位置有两个或三个活细胞，则该位置活细胞仍然存活；
    如果活细胞周围八个位置有超过三个活细胞，则该位置活细胞死亡；
    如果死细胞周围正好有三个活细胞，则该位置死细胞复活；
    根据当前状态，写一个函数来计算面板上所有细胞的下一个（一次更新后的）状态。下一个状态是通过将上述规则同时应用于当前状态
    下的每个细胞所形成的，其中细胞的出生和死亡是同时发生的。
    输入：
    [
      [0,1,0],
      [0,0,1],
      [1,1,1],
      [0,0,0]
    ]
    输出：
    [
      [0,0,0],
      [1,0,1],
      [0,1,1],
      [0,1,0]
    ]
    进阶：
    你可以使用原地算法解决本题吗？请注意，面板上所有格子需要同时被更新：你不能先更新某些格子，然后使用它们的更新后的值再更新其他格子。
    本题中，我们使用二维数组来表示面板。原则上，面板是无限的，但当活细胞侵占了面板边界时会造成问题。你将如何解决这些问题？
"""
from typing import List


class Solution:
    # 36ms, 13.7MB
    @classmethod
    def game_of_life(cls, board: List[List[int]]) -> None:
        m, n = len(board), len(board[0])

        def affect(x, y):
            for i in range(x - 1, x + 2):
                for j in range(y - 1, y + 2):
                    if i < 0 or i >= m or j < 0 or j >= n or (i == x and j == y):
                        continue
                    board[i][j] += 10

        for i in range(m):
            for j in range(n):
                if board[i][j] % 10:
                    affect(i, j)

        def recover(x, y):
            value = board[x][y]
            # 30, 死细胞复活；31,21，活细胞保持
            if value in [30, 31, 21]:
                board[x][y] = 1
            else:
                board[x][y] = 0

        for i in range(m):
            for j in range(n):
                recover(i, j)


if __name__ == '__main__':
    test_case = [[0, 1, 0], [0, 0, 1], [1, 1, 1], [0, 0, 0]]
    Solution.game_of_life(test_case)
    print(test_case)
