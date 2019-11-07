"""
  Created by PyCharm.
  User: Liujianhan
  Date: 2019/6/8
  Time: 1:29
 """
__author__ = 'liujianhan'


class Solution:
    @staticmethod
    def generate_matrix(n):
        matrix = [[0] * n for _ in range(n)]
        i, j, di, dj = 0, 0, 0, 1
        for k in range(1, n ** 2 + 1):
            matrix[i][j] = k
            if matrix[(i + di) % n][(j + dj) % n]:
                di, dj = dj, -di

            i += di
            j += dj

        return matrix


if __name__ == '__main__':
    print(Solution.generate_matrix(7))
