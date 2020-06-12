"""
  @Author       : Liujianhan
  @Date         : 20/6/12 22:03
  @FileName     : 212.单词搜索II(H).py
  @ProjectName  : leetcode_in_python
  @Description  : 给定一个二维网格 board 和一个字典中的单词列表 words，找出所有同时在二维网格和字典中出现的单词。
    单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母在一个单词中不允许被重复使用。
    示例:
    输入:
    words = ["oath","pea","eat","rain"] and board =
    [
      ['o','a','a','n'],
      ['e','t','a','e'],
      ['i','h','k','r'],
      ['i','f','l','v']
    ]
    输出: ["eat","oath"]
    说明:
    你可以假设所有输入都由小写字母 a-z 组成。
    提示:
    你需要优化回溯算法以通过更大数据量的测试。你能否早点停止回溯？
    如果当前单词不存在于所有单词的前缀中，则可以立即停止回溯。什么样的数据结构可以有效地执行这样的操作？散列表是否可行？为什么？ 前缀树如何？如果你想学习如何实现一个基本的前缀树，请先查看这个问题： 实现Trie（前缀树）。
 """
from typing import List


class Solution:
    # 260ms, 27.9MB
    @classmethod
    def find_words(cls, board: List[List[str]], words: List[str]) -> List[str]:
        trie = {}
        for word in words:
            t = trie
            for w in word:
                t = t.setdefault(w, {})
            t["end"] = 1
        res = []
        row = len(board)
        col = len(board[0])

        def dfs(i, j, trie, s):
            c = board[i][j]
            if c not in trie: return
            trie = trie[c]
            if "end" in trie and trie["end"] == 1:
                res.append(s + c)
                trie["end"] = 0
            board[i][j] = "#"
            for x, y in [[-1, 0], [1, 0], [0, 1], [0, -1]]:
                tmp_i = x + i
                tmp_j = y + j
                if 0 <= tmp_i < row and 0 <= tmp_j < col and board[tmp_i][tmp_j] != "#":
                    dfs(tmp_i, tmp_j, trie, s + c)
            board[i][j] = c

        for i in range(row):
            for j in range(col):
                dfs(i, j, trie, "")
        return res

    # 196ms, 28.2MB
    @classmethod
    def find_words_v2(cls, board: List[List[str]], words: List[str]) -> List[str]:
        WORD_END = '#'
        memo = {}

        for word in words:
            cur_node = memo
            for letter in word:  # 下面三行等效于cur_node=setdefault(letter,{})
                if letter not in cur_node:
                    cur_node[letter] = {}  # 新建一个
                cur_node = cur_node[letter]  # 不管有没有，进一位
            cur_node[WORD_END] = word  # 表示这个单词结束,记录单词日后好调用

        row_num = len(board)
        column_num = len(board[0])

        ans = []

        def backtrack(row, col, parent):
            letter = board[row][col]
            cur_node = parent[letter]

            if WORD_END in cur_node:
                ans.append(cur_node[WORD_END])  # 当时记录的是那个完整单词
                cur_node.pop(WORD_END)  # 剪枝

            board[row][col] = '#'  # 代表被占用了，防止后续转回来

            for (delta_x, delta_y) in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
                next_row, next_col = row + delta_x, col + delta_y
                if not (0 <= next_row < row_num and 0 <= next_col < column_num):
                    continue
                elif board[next_row][next_col] not in cur_node:
                    continue
                else:
                    backtrack(next_row, next_col, cur_node)

            board[row][col] = letter  # 还原回去

            if not cur_node:  # 这个是剪枝，从后往前剪枝
                parent.pop(letter)

        for row in range(row_num):
            for col in range(column_num):
                if board[row][col] in memo:
                    backtrack(row, col, memo)

        return ans


if __name__ == '__main__':
    board = [
                ['o', 'a', 'a', 'n'],
                ['e', 't', 'a', 'e'],
                ['i', 'h', 'k', 'r'],
                ['i', 'f', 'l', 'v']
            ]
    words = ["oath", "pea", "eat", "rain"]
    print(Solution.find_words(board, words))
    print(Solution.find_words_v2(board, words))
