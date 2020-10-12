"""
  @Author       : liujianhan
  @Date         : 2020/10/12 9:59
  @Project      : leetcode_in_python
  @FileName     : 530.二叉搜索树的最小绝对差.py
  @Description  : 给你一棵所有节点为非负值的二叉搜索树，请你计算树中任意两节点的差的绝对值的最小值。
    示例：

    输入：

       1
        \
         3
        /
       2

    输出：
    1

    解释：
    最小绝对差为 1，其中 2 和 1 的差的绝对值为 1（或者 2 和 3）。

    提示：

    树中至少有 2 个节点。
    本题与 783 https://leetcode-cn.com/problems/minimum-distance-between-bst-nodes/ 相同
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 60ms, 15.4MB
    @staticmethod
    def get_minimum_difference(root: TreeNode) -> int:
        res, prev = float('inf'), float('-inf')

        def dfs(root):
            nonlocal res, prev
            if not root:
                return
            dfs(root.left)
            res = min(res, root.val - prev)
            prev = root.val
            dfs(root.right)

        dfs(root)

        return int(res)


if __name__ == '__main__':
    pass
