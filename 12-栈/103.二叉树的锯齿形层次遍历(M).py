"""
  @Author       : Liujianhan
  @Date         : 20/5/7 22:37
  @FileName     : 103.二叉树的锯齿形层次遍历(M).py
  @ProjectName  : leetcode_in_python
  @Description  : 给定一个二叉树，返回其节点值的锯齿形层次遍历。（即先从左往右，再从右往左进行下一层遍历，以此类推，层与层之间交替进行）。
    例如：
    给定二叉树 [3,9,20,null,null,15,7],
        3
       / \
      9  20
        /  \
       15   7
    返回锯齿形层次遍历如下：
    [
      [3],
      [20,9],
      [15,7]
    ]
 """
from collections import deque
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 36ms, 14MB
    @classmethod
    def zigzag_level_order(cls, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        stack = deque()
        stack.append(root)
        ans = []

        def bfs(root):
            level = 0
            while stack:
                tmp = []
                if level % 2 == 0:
                    for i in range(len(stack)):
                        node = stack.popleft()
                        tmp.append(node.val)
                        if node.left is not None:
                            stack.append(node.left)
                        if node.right is not None:
                            stack.append(node.right)
                    level += 1
                    ans.append(tmp)
                else:
                    for i in range(len(stack)):
                        node = stack.pop()
                        tmp.append(node.val)
                        if node.right:
                            stack.insert(0, node.right)
                        if node.left:
                            stack.insert(0, node.left)
                    level += 1
                    ans.append(tmp)

        bfs(root)
        return ans

    # 44ms, 14.1MB
    @classmethod
    def zigzag_level_order_v2(cls, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        res = []
        stack = [root]
        level = 0
        while len(stack) > 0:
            tmp = []
            new_stack = []
            while len(stack) > 0:
                cur = stack.pop()
                tmp.append(cur.val)
                if level % 2 == 0:
                    if cur.left:
                        new_stack.append(cur.left)
                    if cur.right:
                        new_stack.append(cur.right)
                else:
                    if cur.right:
                        new_stack.append(cur.right)
                    if cur.left:
                        new_stack.append(cur.left)
            res.append(tmp)
            stack = new_stack
            level += 1

        return res
