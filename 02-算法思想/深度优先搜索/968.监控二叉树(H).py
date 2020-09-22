"""
  @Author       : liujianhan
  @Date         : 2020/9/22 10:21
  @Project      : leetcode_in_python
  @FileName     : 968.监控二叉树(H).py
  @Description  : 给定一个二叉树，我们在树的节点上安装摄像头。
    节点上的每个摄影头都可以监视其父对象、自身及其直接子对象。
    计算监控树的所有节点所需的最小摄像头数量。
    示例 1：
    输入：[0,0,null,0,0]
    输出：1
    解释：如图所示，一台摄像头足以监控所有节点。
    示例 2：
    输入：[0,0,null,0,null,0,null,null,0]
    输出：2
    解释：需要至少两个摄像头来监视树的所有节点。 上图显示了摄像头放置的有效位置之一。
    提示：
    给定树的节点数的范围是 [1, 1000]。
    每个节点的值都是 0。
    思路：想知道在哪里放camera，需要来按照某种顺序来遍历图，遍历的同时在每一个位置时，以某种规则来决定是否放置。
    所以想到用dfs遍历，用greedy来决定。开始遍历后，首先会一条路走到leaf。将这个leaf标记val为1，并把这个val返回，
    告诉上一层也就是这个leaf的parent：有一个child是leaf。所以，此parent必须放一个camera。下一步是为这个parent的val标记为2，
    用2代表放置camera，并将这个2返回给这个parent的parent，称他为parent_g。所以parent_g通过其得到的返回值，知道他的孩子parent是有camera，
    自己可以被cover，所以将自己的val赋值0，代表自己一种‘属性’，被自己的child节点放置的cameracover到了的属性。
    在此过程中，greedy体现在我们在parent放置camera来cover其leaf，而没有在leaf上直接放置camera。
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 60ms, 13.5MB
    @staticmethod
    def min_camera_cover(self, root: TreeNode) -> int:
        self.cameras = 0
        self.dfs_greedy(root)
        return self.cameras + int(root.val == 1)

    def dfs_greedy(self, root):
        if not root:
            return 0
        left = self.dfs_greedy(root.left)
        right = self.dfs_greedy(root.right)
        if left == 0 and right == 0:
            root.val = 1
        elif left == 1 or right == 1:
            root.val = 2
            self.cameras = self.cameras + 1
        else:  # left == 2 or right == 2:
            root.val = 0
        return root.val
