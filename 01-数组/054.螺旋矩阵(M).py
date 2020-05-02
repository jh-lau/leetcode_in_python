"""
  @Author       : Liujianhan
  @Date         : 20/5/2 13:36
  @FileName     : 054.螺旋矩阵(M).py
  @ProjectName  : leetcode_in_python
  @Description  : 给定一个包含 m x n 个元素的矩阵（m 行, n 列），请按照顺时针螺旋顺序，返回矩阵中的所有元素。
    示例 1:
    输入:
    [
     [ 1, 2, 3 ],
     [ 4, 5, 6 ],
     [ 7, 8, 9 ]
    ]
    输出: [1,2,3,6,9,8,7,4,5]
    示例 2:
    输入:
    [
      [1, 2, 3, 4],
      [5, 6, 7, 8],
      [9,10,11,12]
    ]
    输出: [1,2,3,4,8,12,11,10,9,5,6,7]
 """
from typing import List


class Solution:
    # 28ms, 13.7MB
    @classmethod
    def spiral_order(cls, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []
        m, n = len(matrix), len(matrix[0])
        x = y = di = 0
        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]
        res = []
        visited = set()

        for i in range(m * n):
            res.append(matrix[x][y])
            visited.add((x, y))
            nx, ny = x + dx[di], y + dy[di]
            if 0 <= nx < m and 0 <= ny < n and (nx, ny) not in visited:
                x, y = nx, ny
            else:
                di = (di + 1) % 4  # 如果不满足条件，换一个方向进行遍历
                x, y = x + dx[di], y + dy[di]

        return res


if __name__ == '__main__':
    test_cases = [
        [
            [1, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 10, 11, 12]
        ],
        [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]
    ]
    for tc in test_cases:
        print(Solution.spiral_order(tc))
