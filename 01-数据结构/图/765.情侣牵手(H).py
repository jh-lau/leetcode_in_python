"""
  @Author       : liujianhan
  @Date         : 21/2/14 0:29
  @Project      : leetcode_in_python
  @FileName     : 765.情侣牵手(H).py
  @Description  : N 对情侣坐在连续排列的 2N 个座位上，想要牵到对方的手。 计算最少交换座位的次数，以便每对情侣可以并肩坐在一起。
    一次交换可选择任意两人，让他们站起来交换座位。
    人和座位用 0 到 2N-1 的整数表示，情侣们按顺序编号，第一对是 (0, 1)，第二对是 (2, 3)，以此类推，最后一对是 (2N-2, 2N-1)。
    这些情侣的初始座位  row[i] 是由最初始坐在第 i 个座位上的人决定的。

    示例 1:
    输入: row = [0, 2, 1, 3]
    输出: 1
    解释: 我们只需要交换row[1]和row[2]的位置即可。

    示例 2:
    输入: row = [3, 2, 0, 1]
    输出: 0
    解释: 无需交换座位，所有的情侣都已经可以手牵手了。
    说明:

    len(row) 是偶数且数值在 [4, 60]范围内。
    可以保证row 是序列 0...len(row)-1 的一个全排列。
"""
from typing import List


class UnionFind:
    def __init__(self, n):
        self.father = list(range(n))
        self.count = 0

    def find(self, x):
        if self.father[x] != x:
            self.father[x] = self.find(self.father[x])
        return self.father[x]

    def union(self, x, y):
        fx = self.find(x)
        fy = self.find(y)
        if fx == fy: return
        self.count += 1
        self.father[fx] = fy


class Solution:
    # 26ms, 14.9MB
    @staticmethod
    def min_swaps_couples(row: List[int]) -> int:
        length = len(row)
        couples = [i // 2 for i in row]
        uf = UnionFind(length // 2)
        for i in range(0, length, 2):
            uf.union(couples[i], couples[i + 1])
        return uf.count


if __name__ == '__main__':
    test_cases = [
        [0, 2, 1, 3],
        [3, 2, 0, 1]
    ]
    for tc in test_cases:
        print(Solution.min_swaps_couples(tc))
