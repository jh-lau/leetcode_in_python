"""
  @Author       : Liujianhan
  @Date         : 20/5/9 21:40
  @FileName     : 117.填充每个节点的下一个右侧节点指针II(M).py
  @ProjectName  : leetcode_in_python
  @Description  : 给定一个二叉树
    struct Node {
      int val;
      Node *left;
      Node *right;
      Node *next;
    }
    填充它的每个 next 指针，让这个指针指向其下一个右侧节点。如果找不到下一个右侧节点，则将 next 指针设置为 NULL。
    初始状态下，所有 next 指针都被设置为 NULL。
 """


class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    @classmethod
    def process_child(cls, childNode, prev, leftmost):
        if childNode:
            if prev:
                prev.next = childNode
            else:
                leftmost = childNode
            prev = childNode
        return prev, leftmost

    # 72ms, 15MB
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root
        leftmost = root
        while leftmost:
            prev, curr = None, leftmost
            leftmost = None
            while curr:
                prev, leftmost = self.process_child(curr.left, prev, leftmost)
                prev, leftmost = self.process_child(curr.right, prev, leftmost)
                curr = curr.next
        return root
