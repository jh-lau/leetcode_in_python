"""
  User: Liujianhan
 """
__author__ = 'liujianhan'


class Solution:
    @staticmethod
    def knapsack(w, v, C):
        mem = [[0 for _ in range(len(w) + 1)] for _ in range(C + 1)]
        for i in range(1, len(w) + 1):
            for j in range(1, C + 1):
                if w[i - 1] <= j:
                    mem[i, j] = max(mem[i, j], mem[i - 1, j], mem[i - 1, j - w[i - 1]] + v[i - 1])
                else:
                    mem[i, j] = mem[i - 1, j]
        return mem[-1, -1]
