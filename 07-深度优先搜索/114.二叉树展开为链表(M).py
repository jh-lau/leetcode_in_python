"""
  @Author       : Liujianhan
  @Date         : 20/5/8 22:20
  @FileName     : 114.二叉树展开为链表(M).py
  @ProjectName  : leetcode_in_python
  @Description  : 给定一个二叉树，原地将它展开为链表。
    例如，给定二叉树

        1
       / \
      2   5
     / \   \
    3   4   6
    将其展开为：

    1
     \
      2
       \
        3
         \
          4
           \
            5
             \
              6
 """


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # 40ms, 14.6MB
    @classmethod
    def flatten(cls, root: TreeNode) -> None:
        cur = root
        while cur:
            if cur.left:
                p = cur.left
                while p.right:
                    p = p.right
                p.right = cur.right
                cur.right = cur.left
                cur.left = None
            cur = cur.right
