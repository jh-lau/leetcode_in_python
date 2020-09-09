"""
  @Author       : Liujianhan
  @Date         : 20/4/23 22:37
  @FileName     : 063.不同路径II(M).py
  @ProjectName  : leetcode_in_python
  @Description  : 一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为“Start” ）。
    机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为“Finish”）。
    现在考虑网格中有障碍物。那么从左上角到右下角将会有多少条不同的路径？
    网格中的障碍物和空位置分别用 1 和 0 来表示。

    说明：m 和 n 的值均不超过 100。

    示例 1:

    输入:
    [
      [0,0,0],
      [0,1,0],
      [0,0,0]
    ]
    输出: 2
    解释:
    3x3 网格的正中间有一个障碍物。
    从左上角到右下角一共有 2 条不同的路径：
    1. 向右 -> 向右 -> 向下 -> 向下
    2. 向下 -> 向下 -> 向右 -> 向右
 """
from typing import List


class Solution:
    # 40ms, 13.7MB
    @classmethod
    def unique_paths_with_obstacles(cls, obstacle_grid: List[List[int]]) -> int:
        m = len(obstacle_grid)
        n = len(obstacle_grid[0])
        dp = [1] + [0] * n
        for i in range(0, m):
            for j in range(0, n):
                dp[j] = 0 if obstacle_grid[i][j] else dp[j] + dp[j - 1]

        return dp[-2]


if __name__ == '__main__':
    test_cases = [
        [
            [0, 0, 0],
            [0, 1, 0],
            [0, 0, 0]
        ]
    ]
    for tc in test_cases:
        print(tc)
        print(Solution.unique_paths_with_obstacles(tc))

