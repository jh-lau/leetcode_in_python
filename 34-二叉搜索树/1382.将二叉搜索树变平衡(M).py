"""
  @Author       : liujianhan
  @Date         : 2020/4/20 下午2:23
  @Project      : leetcode_in_python
  @FileName     : 1382.将二叉搜索树变平衡(M).py
  @Description  : 给你一棵二叉搜索树，请你返回一棵 平衡后 的二叉搜索树，新生成的树应该与原来的树有着相同的节点值。
    如果一棵二叉搜索树中，每个节点的两棵子树高度差不超过 1 ，我们就称这棵二叉搜索树是 平衡的 。
    如果有多种构造方法，请你返回任意一种。
    输入：root = [1,null,2,null,3,null,4,null,null]
    输出：[2,1,3,null,null,null,4]
    解释：这不是唯一的正确答案，[3,1,4,null,2,null,null] 也是一个可行的构造方案。
    提示：
    树节点的数目在 1 到 10^4 之间。
    树节点的值互不相同，且在 1 到 10^5 之间。
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left, self.right = None, None


# 260ms, 18MB
class Solution:
    def mid_sort(self, root, res):
        if root:
            if root.left:
                self.mid_sort(root.left, res)
            res.append(root)
            if root.right:
                self.mid_sort(root.right, res)

    def create_bst(self, res, l_idx, r_idx):
        mid = (l_idx + r_idx) // 2
        mid_point = res[mid]
        mid_point.left = None
        mid_point.right = None
        if l_idx < mid:
            mid_point.left = self.create_bst(res, l_idx, mid - 1)
        if r_idx > mid:
            mid_point.right = self.create_bst(res, mid + 1, r_idx)
        return mid_point

    def balance_bst(self, root: TreeNode) -> TreeNode:
        if not root:
            return root
        res = []
        self.mid_sort(root, res)
        return self.create_bst(res, 0, len(res) - 1)


if __name__ == '__main__':
    pass