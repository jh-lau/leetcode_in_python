"""
  @Author       : liujianhan
  @Date         : 2020/4/15 上午10:19
  @Project      : leetcode_in_python
  @FileName     : 542.01矩阵(M).py
  @Description  : 给定一个由 0 和 1 组成的矩阵，找出每个元素到最近的 0 的距离。
    两个相邻元素间的距离为 1 。
    示例 1:
    输入:
    0 0 0
    0 1 0
    0 0 0
    输出:
    0 0 0
    0 1 0
    0 0 0

    示例 2:
    输入:
    0 0 0
    0 1 0
    1 1 1
    输出:
    0 0 0
    0 1 0
    1 2 1
    注意:
    给定矩阵的元素个数不超过 10000。
    给定矩阵中至少有一个元素是 0。
    矩阵中的元素只在四个方向上相邻: 上、下、左、右。
"""
from collections import deque
from typing import List


class Solution:
    # 896ms, 17.4MB
    @classmethod
    def update_matrix(cls, matrix: List[List[int]]) -> List[List[int]]:
        """广度优先搜索"""
        m, n = len(matrix), len(matrix[0])
        dist = [[0] * n for _ in range(m)]
        zeros_pos = [(i, j) for i in range(m) for j in range(n) if matrix[i][j] == 0]
        q = deque(zeros_pos)
        seen = set(zeros_pos)

        while q:
            i, j = q.popleft()
            for ni, nj in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
                if 0 <= ni < m and 0 <= nj < n and (ni, nj) not in seen:
                    dist[ni][nj] = dist[i][j] + 1
                    q.append((ni, nj))
                    seen.add((ni, nj))

        return dist


if __name__ == '__main__':
    test_cases = [
        [[0, 0, 0], [0, 1, 0], [0, 0, 0]],
        [[0, 0, 0], [0, 1, 0], [1, 1, 1]]
    ]
    for tc in test_cases:
        print(Solution.update_matrix(tc))
