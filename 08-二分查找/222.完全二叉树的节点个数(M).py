"""
  @Author       : Liujianhan
  @Date         : 20/6/25 16:19
  @FileName     : 222.完全二叉树的节点个数(M).py
  @ProjectName  : leetcode_in_python
  @Description  : 给出一个完全二叉树，求出该树的节点个数。
    说明：
    完全二叉树的定义如下：在完全二叉树中，除了最底层节点可能没填满外，其余每层节点数都达到最大值，并且最下面一层的节点都集中在该层最左边的若干位置。若最底层为第 h 层，则该层包含 1~ 2h 个节点。
    示例:
    输入:
        1
       / \
      2   3
     / \  /
    4  5 6
    输出: 6
 """


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 80ms, 20.9MB
    @classmethod
    def count_deep(cls, node: TreeNode) -> int:
        d = 0
        while node:
            node = node.left
            d += 1
        return d

    def count_nodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        lnode = self.count_deep(root.left)
        rnode = self.count_deep(root.right)
        if lnode == rnode:
            return 2 ** lnode + self.count_nodes(root.right)
        else:
            return 2 ** rnode + self.count_nodes(root.left)


if __name__ == '__main__':
    pass