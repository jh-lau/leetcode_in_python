"""
  @Author       : liujianhan
  @Date         : 2020/12/3 9:59
  @Project      : leetcode_in_python
  @FileName     : 1046.最后一块石头的重量.py
  @Description  : 有一堆石头，每块石头的重量都是正整数。
    每一回合，从中选出两块 最重的 石头，然后将它们一起粉碎。假设石头的重量分别为 x 和 y，且 x <= y。那么粉碎的可能结果如下：
    如果 x == y，那么两块石头都会被完全粉碎；
    如果 x != y，那么重量为 x 的石头将会完全粉碎，而重量为 y 的石头新重量为 y-x。
    最后，最多只会剩下一块石头。返回此石头的重量。如果没有石头剩下，就返回 0。
    示例：

    输入：[2,7,4,1,8,1]
    输出：1
    解释：
    先选出 7 和 8，得到 1，所以数组转换为 [2,4,1,1,1]，
    再选出 2 和 4，得到 2，所以数组转换为 [2,1,1,1]，
    接着是 2 和 1，得到 1，所以数组转换为 [1,1,1]，
    最后选出 1 和 1，得到 0，最终数组转换为 [1]，这就是最后剩下那块石头的重量。
    提示：
    1 <= stones.length <= 30
    1 <= stones[i] <= 1000
"""
from typing import List
import heapq


class Solution:
    # 36ms, 13.5MB
    @staticmethod
    def last_stone_weight(stones: List[int]) -> int:
        stones.sort()
        while len(stones) > 1:
            n1 = stones.pop()
            n2 = stones.pop()
            diff = n1 - n2
            if diff:
                stones.append(diff)
                stones.sort()

        return stones[0] if stones else 0

    # 48ms, 13.5MB
    @staticmethod
    def last_stone_weight_v2(stones: List[int]) -> int:
        h = [-stone for stone in stones]
        heapq.heapify(h)

        while len(h) > 1:
            a, b = heapq.heappop(h), heapq.heappop(h)
            if a != b:
                heapq.heappush(h, a - b)

        return -h[0] if h else 0


if __name__ == '__main__':
    test_cases = [
        [2, 7, 4, 1, 8, 1]
    ]
    for tc in test_cases:
        print(Solution.last_stone_weight(tc))
        print(Solution.last_stone_weight_v2(tc))
