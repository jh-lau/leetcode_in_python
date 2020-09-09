"""
  @Author       : Liujianhan
  @Date         : 20/5/7 22:49
  @FileName     : 105.从前序与中序遍历序列构造二叉树(M).py
  @ProjectName  : leetcode_in_python
  @Description  : 根据一棵树的前序遍历与中序遍历构造二叉树。
    注意:
    你可以假设树中没有重复的元素。
    例如，给出
    前序遍历 preorder = [3,9,20,15,7]
    中序遍历 inorder = [9,3,15,20,7]
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
    # 212ms, 87.7MB
    @classmethod
    def build_tree(cls, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder:
            return None
        root = TreeNode(preorder[0])

        i = inorder.index(root.val)
        root.left = cls.build_tree(preorder[1:i + 1], inorder[:i])
        root.right = cls.build_tree(preorder[i + 1:], inorder[i + 1:])

        return root
