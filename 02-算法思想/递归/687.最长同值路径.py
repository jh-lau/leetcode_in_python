"""
  @Author       : Liujianhan
  @Date         : 20/4/19 22:21
  @FileName     : 687.最长同值路径.py
  @ProjectName  : leetcode_in_python
  @Description  : 给定一个二叉树，找到最长的路径，这个路径中的每个节点具有相同值。 这条路径可以经过也可以不经过根节点。
    注意：两个节点之间的路径长度由它们之间的边数表示。
 """


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left, self.right = None, None


class Solution:
    # 484ms, 17.5MB
    @classmethod
    def longest_uni_value_path(cls, root: TreeNode) -> int:
        cls.ans = 0

        def arrow_length(node):
            if not node: return 0
            left_length = arrow_length(node.left)
            right_length = arrow_length(node.right)
            left_arrow = right_arrow = 0
            if node.left and node.left.val == node.val:
                left_arrow = left_length + 1
            if node.right and node.right.val == node.val:
                right_arrow = right_length + 1
            cls.ans = max(cls.ans, left_arrow + right_arrow)
            return max(left_arrow, right_arrow)

        arrow_length(root)
        return cls.ans


if __name__ == '__main__':
    pass
