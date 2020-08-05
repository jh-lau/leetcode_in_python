"""
  @Author       : liujianhan
  @Date         : 2020/8/5 上午10:13
  @Project      : leetcode_in_python
  @FileName     : 337打家劫舍III(M).py
  @Description  : 在上次打劫完一条街道之后和一圈房屋后，小偷又发现了一个新的可行窃的地区。这个地区只有一个入口，我们称之为“根”。 除了“根”之外，每栋房子有且只有一个“父“房子与之相连。一番侦察之后，聪明的小偷意识到“这个地方的所有房屋的排列类似于一棵二叉树”。 如果两个直接相连的房子在同一天晚上被打劫，房屋将自动报警。
    计算在不触动警报的情况下，小偷一晚能够盗取的最高金额。

    示例 1:

    输入: [3,2,3,null,3,null,1]

         3
        / \
       2   3
        \   \
         3   1

    输出: 7
    解释: 小偷一晚能够盗取的最高金额 = 3 + 3 + 1 = 7.
    示例 2:

    输入: [3,4,5,1,3,null,1]

         3
        / \
       4   5
      / \   \
     1   3   1

    输出: 9
    解释: 小偷一晚能够盗取的最高金额 = 4 + 5 = 9.

题解思路:
# 递归求解+DP
# 当前节点取得最大收益取决于两个值，当前节点值，和上一层节点取得的最大收益
# 当前节点取得最大收益的两种情况：
# 1. 当前节点被计入，以及其孙子及更深的节点
# 2. 当前节点未计入，其孩子及一些更深的节点
# 因此，当前节点是否被计入到收益中，是这层节点如何取最大值的条件
# 对于一个节点，我们只需要比较：它不参与计算时的最大值=其最左右节点最大值之和 VS 它参与计算=value+左右节点不参与结算时的最大值
# 显然，我们每一层节点需要保留两个值：
# [当前节点不参与计算取得的最大收益，当前节点可以取得的最大收益（参与/不参与）]
# 那么，这两个值的转移方程:
# 当前节点不参与计算取得的最大收益: helper(root)[0] = helper(root.left)[1]+helper(root.right)[1]
# 当前节点可以取得的最大收益: helper(root)[1] = max(root.val+helper(root.left)[0]+helper(root.right)[0], helper(root)[0])
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 80ms, 15.7MB
    def rob(self, root: TreeNode) -> int:
        return self.helper(root)[1]

    # helper函数返回一个节点为根的最大值 = [当前节点不参与计算的最大收益，当前节点的最大收益(参与/不参与)]
    def helper(self, root):
        if root is None:
            return [0, 0]
        left_amount = self.helper(root.left)
        right_amount = self.helper(root.right)
        without_root = left_amount[1] + right_amount[1]
        with_root = root.val + left_amount[0] + right_amount[0]
        return [without_root, max(with_root, without_root)]


if __name__ == '__main__':
    pass
