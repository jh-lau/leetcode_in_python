"""
  @Author       : Liujianhan
  @Date         : 20/5/4 21:31
  @FileName     : 079.单词搜索(M).py
  @ProjectName  : leetcode_in_python
  @Description  : 给定一个二维网格和一个单词，找出该单词是否存在于网格中。
    单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母不允许被重复使用。
    示例:
    board =
    [
      ['A','B','C','E'],
      ['S','F','C','S'],
      ['A','D','E','E']
    ]
    给定 word = "ABCCED", 返回 true
    给定 word = "SEE", 返回 true
    给定 word = "ABCB", 返回 false
    提示：
    board 和 word 中只包含大写和小写英文字母。
    1 <= board.length <= 200
    1 <= board[i].length <= 200
    1 <= word.length <= 10^3
 """
from typing import List


class Solution:
    # 236ms, 14.7MB
    @classmethod
    def exist(cls, board: List[List[str]], word: str) -> bool:
        row = len(board)
        col = len(board[0])

        def helper(i, j, k, visited):
            if k == len(word):
                return True
            for x, y in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
                tmp_i = x + i
                tmp_j = y + j
                if 0 <= tmp_i < row and 0 <= tmp_j < col and (tmp_i, tmp_j) not in visited \
                        and board[tmp_i][tmp_j] == word[k]:
                    visited.add((tmp_i, tmp_j))
                    if helper(tmp_i, tmp_j, k + 1, visited):
                        return True
                    visited.remove((tmp_i, tmp_j))  # 回溯
            return False

        for i in range(row):
            for j in range(col):
                if board[i][j] == word[0] and helper(i, j, 1, {(i, j)}):
                    return True

        return False


if __name__ == '__main__':
    board = [
        ['A', 'B', 'C', 'E'],
        ['S', 'F', 'C', 'S'],
        ['A', 'D', 'E', 'E']
    ]
    for word in ['ABCCED', 'SEE', 'ABCB']:
        print(Solution.exist(board, word))
