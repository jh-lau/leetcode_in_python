"""
  @Author       : liujianhan
  @Date         : 2021/1/25 10:14
  @Project      : leetcode_in_python
  @FileName     : 959.由斜杠划分区域(M).py
  @Description  : 在由 1 x 1 方格组成的 N x N 网格 grid 中，每个 1 x 1 方块由 /、\ 或空格构成。这些字符会将方块划分为一些共边的区域。
    （请注意，反斜杠字符是转义的，因此 \ 用 "\\" 表示。）。
    返回区域的数目。

    示例 1：
    输入：
    [
      " /",
      "/ "
    ]
    输出：2
    解释：2x2 网格如下：

    示例 2：
    输入：
    [
      " /",
      "  "
    ]
    输出：1
    解释：2x2 网格如下：

    示例 3：
    输入：
    [
      "\\/",
      "/\\"
    ]
    输出：4
    解释：（回想一下，因为 \ 字符是转义的，所以 "\\/" 表示 \/，而 "/\\" 表示 /\。）
    2x2 网格如下：

    示例 4：
    输入：
    [
      "/\\",
      "\\/"
    ]
    输出：5
    解释：（回想一下，因为 \ 字符是转义的，所以 "/\\" 表示 /\，而 "\\/" 表示 \/。）
    2x2 网格如下：

    示例 5：
    输入：
    [
      "//",
      "/ "
    ]
    输出：3
    解释：2x2 网格如下：

    提示：
    1 <= grid.length == grid[0].length <= 30
    grid[i][j] 是 '/'、'\'、或 ' '。
"""


class Solution:
    #
    @staticmethod
    def regions_by_slashes(grid):
        """
        :type grid: List[str]
        :rtype: int
        """
        n = len(grid)  # 每行格子数量
        m = n + 1  # 每行节点数量

        def node_index(row, col):
            return row * m + col

        parents = list(range(m ** 2))  # 每个节点的parent（并查集）
        # 初始状态最外层的4条边上的节点是联通的，处于同一个集合
        for i in range(m):
            parents[node_index(0, i)] = 0
            parents[node_index(m - 1, i)] = 0
            parents[node_index(i, 0)] = 0
            parents[node_index(i, m - 1)] = 0

        # NOTE: 作者主要就是改了这个函数，提升查并集的效率
        def union_find(x):
            if parents[x] != x:
                parents[x] = union_find(parents[x])
            return parents[x]

        # 初始状态整个格子是一个封闭区域
        regions_count = 1
        # 遍历格子的所有连线
        for i in range(n):
            for j in range(n):
                # 连线的上下两个节点
                node_up, node_down = None, None
                if grid[i][j] == " ":
                    continue
                elif grid[i][j] == "/":
                    node_up = node_index(i, j + 1)
                    node_down = node_index(i + 1, j)
                elif grid[i][j] == "\\":
                    node_up = node_index(i, j)
                    node_down = node_index(i + 1, j + 1)
                # 上下节点的根节点
                root_up, root_down = union_find(node_up), union_find(node_down)
                if root_up == root_down:
                    # 上下节点已经是连通的，则连线会新增一个封闭区域
                    regions_count += 1
                else:
                    # 上下节点未连通，则将两个节点连通
                    parents[root_down] = root_up

        return regions_count


if __name__ == '__main__':
    test_cases = [
        [" /", "/ "],
        [" /", "  "],
        ["\\/", "/\\"],
        ["/\\", "\\/"],
        ["//", "/ "]
    ]
    for tc in test_cases:
        print(Solution.regions_by_slashes(tc))
