"""
  @Author       : liujianhan
  @Date         : 2020/7/24 下午7:36
  @Project      : leetcode_in_python
  @FileName     : 1025.除数博弈.py
  @Description  : 爱丽丝和鲍勃一起玩游戏，他们轮流行动。爱丽丝先手开局。

    最初，黑板上有一个数字 N 。在每个玩家的回合，玩家需要执行以下操作：

    选出任一 x，满足 0 < x < N 且 N % x == 0 。
    用 N - x 替换黑板上的数字 N 。
    如果玩家无法执行这些操作，就会输掉游戏。

    只有在爱丽丝在游戏中取得胜利时才返回 True，否则返回 false。假设两个玩家都以最佳状态参与游戏。

     

    示例 1：

    输入：2
    输出：true
    解释：爱丽丝选择 1，鲍勃无法进行操作。
    示例 2：

    输入：3
    输出：false
    解释：爱丽丝选择 1，鲍勃也选择 1，然后爱丽丝无法进行操作。
     

    提示：

    1 <= N <= 1000
"""


class Solution:
    # 84ms, 13.6MB
    @staticmethod
    def divisor_game(N: int) -> bool:
        dp = [False]
        for i in range(2, N + 1):
            dp.append(any(not dp[i - j - 1] for j in range(1, i // 2 + 1) if i % j == 0))
        return dp[-1]

    # 40ms, 13.7MB
    @staticmethod
    def divisor_game_v2(N: int) -> bool:
        return not N % 2


if __name__ == '__main__':
    test_cases = [2, 3]
    for tc in test_cases:
        print(Solution.divisor_game(tc))
        print(Solution.divisor_game_v2(tc))
