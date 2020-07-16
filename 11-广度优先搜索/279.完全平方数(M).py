"""
  @Author       : liujianhan
  @Date         : 2020/7/16 下午5:51
  @Project      : leetcode_in_python
  @FileName     : 279.完全平方数(M).py
  @Description  : 给定正整数 n，找到若干个完全平方数（比如 1, 4, 9, 16, ...）使得它们的和等于 n。你需要让组成和的完全平方数的个数最少。
    示例 1:
    输入: n = 12
    输出: 3
    解释: 12 = 4 + 4 + 4.
    示例 2:
    输入: n = 13
    输出: 2
    解释: 13 = 4 + 9.
"""
import math


class Solution:
    # 5316ms, 13.8MB
    @staticmethod
    def num_square(n: int) -> int:
        # dp
        square_nums = [i ** 2 for i in range(int(math.sqrt(n)) + 1)]
        dp = [float('inf')] * (n + 1)
        dp[0] = 0
        for i in range(1, n + 1):
            for square in square_nums:
                if i < square:
                    break
                dp[i] = min(dp[i], dp[i - square] + 1)

        return int(dp[-1])

    # 208ms, 14.7MB
    @staticmethod
    def num_square_v2(n: int) -> int:
        # greedy and bfs
        # list of square numbers that are less than `n`
        square_nums = [i * i for i in range(1, int(n ** 0.5) + 1)]

        level = 0
        queue = {n}
        while queue:
            level += 1
            # ! Important: use set() instead of list() to eliminate the redundancy,
            # which would even provide a 5-times speedup, 200ms vs. 1000ms.
            next_queue = set()
            # construct the queue for the next level
            for remainder in queue:
                for square_num in square_nums:
                    if remainder == square_num:
                        return level  # find the node!
                    elif remainder < square_num:
                        break
                    else:
                        next_queue.add(remainder - square_num)
            queue = next_queue
        return level


if __name__ == '__main__':
    test_cases = [
        12, 13
    ]
    for tc in test_cases:
        print(Solution.num_square(tc))
        print(Solution.num_square_v2(tc))
