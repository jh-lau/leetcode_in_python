"""
  @Author       : Liujianhan
  @Date         : 20/4/23 22:32
  @FileName     : 062.不同路径(M).py
  @ProjectName  : leetcode_in_python
  @Description  : 一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为“Start” ）。
    机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为“Finish”）。
    问总共有多少条不同的路径？

    示例 1:
    输入: m = 3, n = 2
    输出: 3
    解释:
    从左上角开始，总共有 3 条路径可以到达右下角。
    1. 向右 -> 向右 -> 向下
    2. 向右 -> 向下 -> 向右
    3. 向下 -> 向右 -> 向右
    示例 2:
    输入: m = 7, n = 3
    输出: 28
    提示：
    1 <= m, n <= 100
    题目数据保证答案小于等于 2 * 10 ^ 9
 """


class Solution:
    # 40ms, 13.7MB
    @classmethod
    def unique_paths(cls, m: int, n: int) -> int:
        nums = [[None for _ in range(n)] for _ in range(m)]
        for i in range(m):
            nums[i][0] = 1
        for j in range(n):
            nums[0][j] = 1
        for i in range(1, m):
            for j in range(1, n):
                nums[i][j] = nums[i - 1][j] + nums[i][j - 1]

        return nums[-1][-1]


if __name__ == '__main__':
    test_cases = [
        (3, 2), (7, 3)
    ]
    for tc in test_cases:
        print(Solution.unique_paths(*tc))
