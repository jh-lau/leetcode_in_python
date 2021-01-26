"""
  @Author       : liujianhan
  @Date         : 2021/1/26 10:05
  @Project      : leetcode_in_python
  @FileName     : 1128.等价多米诺骨牌对的数量.py
  @Description  : 给你一个由一些多米诺骨牌组成的列表 dominoes。
    如果其中某一张多米诺骨牌可以通过旋转 0 度或 180 度得到另一张多米诺骨牌，我们就认为这两张牌是等价的。
    形式上，dominoes[i] = [a, b] 和 dominoes[j] = [c, d] 等价的前提是 a==c 且 b==d，或是 a==d 且 b==c。
    在 0 <= i < j < dominoes.length 的前提下，找出满足 dominoes[i] 和 dominoes[j] 等价的骨牌对 (i, j) 的数量。
     
    示例：
    输入：dominoes = [[1,2],[2,1],[3,4],[5,6]]
    输出：1

    提示：
    1 <= dominoes.length <= 40000
    1 <= dominoes[i][j] <= 9
"""
from typing import List


class Solution:
    # 284ms, 24.3MB
    @staticmethod
    def num_equiv_domino_pairs(dominoes: List[List[int]]) -> int:
        num = [0] * 100
        res = 0
        for x, y in dominoes:
            val = 10 * x + y if x > y else 10 * y + x
            res += num[val]
            num[val] += 1

        return res


if __name__ == '__main__':
    test_cases = [
        [[1, 2], [2, 1], [3, 4], [5, 6]],
        [[1, 2], [2, 1], [3, 4], [4, 3]],
    ]
    for tc in test_cases:
        print(Solution.num_equiv_domino_pairs(tc))
