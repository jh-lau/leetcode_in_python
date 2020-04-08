"""
  @Author       : liujianhan
  @Date         : 2020/4/8 下午5:03
  @Project      : leetcode_in_python
  @FileName     : 13.机器人的运动范围(M).py
  @Description  : 地上有一个m行n列的方格，从坐标 [0,0] 到坐标 [m-1,n-1] 。一个机器人从坐标 [0, 0] 的格子开始移动，它每次可以向左、右、上、下移动一格（不能移动到方格外），也不能进入行坐标和列坐标的数位之和大于k的格子。例如，当k为18时，机器人能够进入方格 [35, 37] ，因为3+5+3+7=18。但它不能进入方格 [35, 38]，因为3+5+3+8=19。请问该机器人能够到达多少个格子？
    示例 1：

    输入：m = 2, n = 3, k = 1
    输出：3
    示例 1：

    输入：m = 3, n = 1, k = 0
    输出：1
    https://leetcode-cn.com/problems/ji-qi-ren-de-yun-dong-fan-wei-lcof/solution/mian-shi-ti-13-ji-qi-ren-de-yun-dong-fan-wei-dfs-b/
"""


class Solution:
    # 52ms, 14.2MB
    @classmethod
    def moving_count(cls, m: int, n: int, k: int) -> int:
        def dfs(i, j, si, sj):
            if i >= m or j >= n or k < si + sj or (i, j) in visited:
                return 0
            visited.add((i, j))
            return 1 + dfs(i + 1, j, si + 1 if (i + 1) % 10 else si - 8, sj) + \
                   dfs(i, j + 1, si, sj + 1 if (j + 1) % 10 else sj - 8)

        visited = set()
        return dfs(0, 0, 0, 0)

    # 52ms, 14MB
    @classmethod
    def moving_count_v2(cls, m: int, n: int, k: int) -> int:
        queue, visited = [(0, 0, 0, 0)], set()
        while queue:
            i, j, si, sj = queue.pop(0)
            if i >= m or j >= n or k < si + sj or (i, j) in visited:
                continue
            visited.add((i, j))
            queue.append((i + 1, j, si + 1 if (i + 1) % 10 else si - 8, sj))
            queue.append((i, j + 1, si, sj + 1 if (j + 1) % 10 else sj - 8))

        return len(visited)


if __name__ == '__main__':
    test_cases = [(2, 3, 1), (3, 1, 0)]
    for tc in test_cases:
        print(tc, Solution.moving_count(*tc))
        print(tc, Solution.moving_count_v2(*tc))
