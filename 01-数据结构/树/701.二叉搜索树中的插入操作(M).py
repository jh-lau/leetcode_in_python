"""
  @Author       : liujianhan
  @Date         : 20/9/30 21:05
  @Project      : leetcode_in_python
  @FileName     : 701.二叉搜索树中的插入操作(M).py
  @Description  : 给定二叉搜索树（BST）的根节点和要插入树中的值，将值插入二叉搜索树。
    返回插入后二叉搜索树的根节点。 输入数据保证，新值和原始二叉搜索树中的任意节点值都不同。
    注意，可能存在多种有效的插入方式，只要树在插入后仍保持为二叉搜索树即可。 你可以返回任意有效的结果。

    例如, 

    给定二叉搜索树:

            4
           / \
          2   7
         / \
        1   3

    和 插入的值: 5
    你可以返回这个二叉搜索树:

             4
           /   \
          2     7
         / \   /
        1   3 5
    或者这个树也是有效的:

             5
           /   \
          2     7
         / \
        1   3
             \
              4
     

    提示：

    给定的树上的节点数介于 0 和 10^4 之间
    每个节点都有一个唯一整数值，取值范围从 0 到 10^8
    -10^8 <= val <= 10^8
    新值和原始二叉搜索树中的任意节点值都不同
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # 156ms, 15.6MB
    @staticmethod
    def insert_into_BST(root: TreeNode, val: int) -> TreeNode:
        if not root:
            return TreeNode(val)

        pos = root
        while pos:
            if val < pos.val:
                if not pos.left:
                    pos.left = TreeNode(val)
                    break
                else:
                    pos = pos.left
            else:
                if not pos.right:
                    pos.right = TreeNode(val)
                    break
                else:
                    pos = pos.right

        return root
