"""
  @Author       : liujianhan
  @Date         : 2020/7/23 上午9:32
  @Project      : leetcode_in_python
  @FileName     : 863.二叉树中所有距离为K的节点(M).py
  @Description  : 给定一个二叉树（具有根结点 root）， 一个目标结点 target ，和一个整数值 K 。
    返回到目标结点 target 距离为 K 的所有结点的值的列表。 答案可以以任何顺序返回。
    示例 1：
    输入：root = [3,5,1,6,2,0,8,null,null,7,4], target = 5, K = 2
    输出：[7,4,1]
    解释：
    所求结点为与目标结点（值为 5）距离为 2 的结点，
    值分别为 7，4，以及 1
    注意，输入的 "root" 和 "target" 实际上是树上的结点。
    上面的输入仅仅是对这些对象进行了序列化描述。
    提示：
    给定的树是非空的。
    树上的每个结点都具有唯一的值 0 <= node.val <= 500 。
    目标结点 target 是树上的结点。
    0 <= K <= 1000.
"""

# Definition for a binary tree node.
import collections
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 52ms, 13.9MB
    @staticmethod
    def distance_k(root: TreeNode, target: TreeNode, K: int) -> List[int]:
        h, f = {}, {}

        def g(r, i, fs):
            if r:
                h[r.val] = i
                f[r.val] = [r.val] + fs  # 让最近的父节点排在最前面
                g(r.left, i + 1, f[r.val])
                g(r.right, i + 1, f[r.val])

        g(root, 0, [])
        ans, ft, ht = [], set(f[target.val]), h[target.val]
        for i in h:
            for common in f[i]:  # 由近到远遍历目标点的父节点
                if common in ft:  # 如果存在共同父节点且满足条件
                    if ht + h[i] - 2 * h[common] == K:
                        ans += [i]  # 就加入答案
                    break
        return ans

    # 44ms, 14.1MB
    @staticmethod
    def distance_k_v2(root, target, K):
        def dfs(node, par=None):
            if node:
                node.par = par
                dfs(node.left, node)
                dfs(node.right, node)

        dfs(root)

        queue = collections.deque([(target, 0)])
        seen = {target}
        while queue:
            if queue[0][1] == K:
                return [node.val for node, d in queue]
            node, d = queue.popleft()
            for nei in (node.left, node.right, node.par):
                if nei and nei not in seen:
                    seen.add(nei)
                    queue.append((nei, d + 1))

        return []


if __name__ == '__main__':
    pass
