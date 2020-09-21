"""
  @Author       : liujianhan
  @Date         : 2020/9/21 20:01
  @Project      : leetcode_in_python
  @FileName     : 1038.从二叉搜索树到更大和树(M).py
  @Description  : 给出二叉 搜索 树的根节点，该二叉树的节点值各不相同，修改二叉树，使每个节点 node 的新值等于原树中大于或等于 node.val 的值之和。

    提醒一下，二叉搜索树满足下列约束条件：

    节点的左子树仅包含键 小于 节点键的节点。
    节点的右子树仅包含键 大于 节点键的节点。
    左右子树也必须是二叉搜索树。
     

    示例：



    输入：[4,1,6,0,2,5,7,null,null,null,3,null,null,null,8]
    输出：[30,36,21,36,35,26,15,null,null,null,33,null,null,null,8]
     

    提示：

    树中的节点数介于 1 和 100 之间。
    每个节点的值介于 0 和 100 之间。
    给定的树为二叉搜索树。
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 44ms, 13.4MB
    @staticmethod
    def bst_to_gst(root: TreeNode) -> TreeNode:
        bn = None

        def helper(node):
            nonlocal bn
            if node.right:
                helper(node.right)
            if bn:
                node.val += bn.val
            bn = node
            if node.left:
                helper(node.left)
            return node.val

        if root:
            helper(root)
        return root

    # 40ms, 13.5MB
    @staticmethod
    def bst_to_gst_v2(root: TreeNode) -> TreeNode:
        stack, bn, cur = [], 0, root
        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.right
            if stack:
                this = stack.pop()
                bn += this.val
                this.val = bn
                cur = this.left
        return root
