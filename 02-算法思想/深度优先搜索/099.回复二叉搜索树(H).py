"""
  @Author       : Liujianhan
  @Date         : 20/5/6 22:46
  @FileName     : 099.回复二叉搜索树(H).py
  @ProjectName  : leetcode_in_python
  @Description  : 二叉搜索树中的两个节点被错误地交换。
    请在不改变其结构的情况下，恢复这棵树。
    示例 1:
    输入: [1,3,null,null,2]
       1
      /
     3
      \
       2

    输出: [3,1,null,null,2]
       3
      /
     1
      \
       2
    示例 2:
    输入: [3,1,4,null,null,2]
      3
     / \
    1   4
       /
      2
    输出: [2,1,4,null,null,3]
      2
     / \
    1   4
       /
      3
    进阶:
    使用 O(n) 空间复杂度的解法很容易实现。
    你能想出一个只使用常数空间的解决方案吗？
 """


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # 92ms, 14.1MB
    @classmethod
    def recover_tree(cls, root: TreeNode) -> None:
        x = y = pred = None

        while root:
            if root.left:
                predecessor = root.left
                while predecessor.right and predecessor.right != root:
                    predecessor = predecessor.right

                if predecessor.right is None:
                    predecessor.right = root
                    root = root.left
                else:
                    if pred and root.val < pred.val:
                        y = root
                        if x is None:
                            x = pred
                    pred = root

                    predecessor.right = None
                    root = root.right
            else:
                if pred and root.val < pred.val:
                    y = root
                    if x is None:
                        x = pred
                pred = root

                root = root.right

        x.val, y.val = y.val, x.val
