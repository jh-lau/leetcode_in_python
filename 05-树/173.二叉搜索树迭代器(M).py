"""
  @Author       : Liujianhan
  @Date         : 20/5/25 22:35
  @FileName     : 173.二叉搜索树迭代器(M).py
  @ProjectName  : leetcode_in_python
  @Description  : 实现一个二叉搜索树迭代器。你将使用二叉搜索树的根节点初始化迭代器。
    调用 next() 将返回二叉搜索树中的下一个最小的数。
    BSTIterator iterator = new BSTIterator(root);
    iterator.next();    // 返回 3
    iterator.next();    // 返回 7
    iterator.hasNext(); // 返回 true
    iterator.next();    // 返回 9
    iterator.hasNext(); // 返回 true
    iterator.next();    // 返回 15
    iterator.hasNext(); // 返回 true
    iterator.next();    // 返回 20
    iterator.hasNext(); // 返回 false
    提示：
    next() 和 hasNext() 操作的时间复杂度是 O(1)，并使用 O(h) 内存，其中 h 是树的高度。
    你可以假设 next() 调用总是有效的，也就是说，当调用 next() 时，BST 中至少存在一个下一个最小的数。
 """


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# 96ms, 19.8MB
class BSTIterator:
    def __init__(self, root: TreeNode):
        self.nodes_sorted = []
        self.index = -1
        self._inorder(root)

    def _inorder(self,root):
        if not root:
            return
        self._inorder(root.left)
        self.nodes_sorted.append(root.val)
        self._inorder(root.right)

    def next(self) -> int:
        self.index += 1
        return self.nodes_sorted[self.index]

    def has_next(self) -> bool:
        return self.index + 1 < len(self.nodes_sorted)
