"""
  @Author       : Liujianhan
  @Date         : 20/5/7 22:53
  @FileName     : 106.从中序与后序遍历序列构造二叉树(M).py
  @ProjectName  : leetcode_in_python
  @Description  : 根据一棵树的中序遍历与后序遍历构造二叉树。
    注意:
    你可以假设树中没有重复的元素。
    例如，给出
    中序遍历 inorder = [9,3,15,20,7]
    后序遍历 postorder = [9,15,7,20,3]
    返回如下的二叉树：

        3
       / \
      9  20
        /  \
       15   7
 """
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 52ms, 18.2MB
    @classmethod
    def build_tree(cls, inorder: List[int], postorder: List[int]) -> TreeNode:
        def helper(left, right):
            if left > right:
                return None
            val = postorder.pop()
            root = TreeNode(val)

            index = idx_map[val]
            root.right = helper(index + 1, right)
            root.left = helper(left, index - 1)

            return root

        idx_map = {val: idx for idx, val in enumerate(inorder)}

        return helper(0, len(inorder) - 1)
