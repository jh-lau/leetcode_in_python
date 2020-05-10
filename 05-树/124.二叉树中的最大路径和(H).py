"""
  @Author       : Liujianhan
  @Date         : 20/5/10 14:58
  @FileName     : 124.二叉树中的最大路径和(H).py
  @ProjectName  : leetcode_in_python
  @Description  : 给定一个非空二叉树，返回其最大路径和。
    本题中，路径被定义为一条从树中任意节点出发，达到任意节点的序列。该路径至少包含一个节点，且不一定经过根节点。
    示例 1:
    输入: [1,2,3]

           1
          / \
         2   3

    输出: 6
    示例 2:
    输入: [-10,9,20,null,null,15,7]
       -10
       / \
      9  20
        /  \
       15   7

    输出: 42
 """


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 96ms, 21.1MB
    @classmethod
    def max_path_sum(cls, root: TreeNode) -> int:
        def max_gain(node):
            nonlocal max_sum
            if not node:
                return 0
            left_gain = max(max_gain(node.left), 0)
            right_gain = max(max_gain(node.right), 0)
            price_new_path = node.val + left_gain + right_gain
            max_sum = max(max_sum, price_new_path)

            return node.val + max(left_gain, right_gain)

        max_sum = float('-inf')
        max_gain(root)

        return int(max_sum)
