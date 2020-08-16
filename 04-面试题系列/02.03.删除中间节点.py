"""
  @Author       : Liujianhan
  @Date         : 20/4/12 21:40
  @FileName     : 02.03.删除中间节点.py
  @ProjectName  : leetcode_in_python
  @Description  : 实现一种算法，删除单向链表中间的某个节点（除了第一个和最后一个节点，不一定是中间节点），假定你只能访问该节点。
    示例：

    输入：单向链表a->b->c->d->e->f中的节点c
    结果：不返回任何数据，但该链表变为a->b->d->e->f
 """


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # 44ms, 13.8MB
    @classmethod
    def delete_node(cls, node) -> None:
        node.val = node.next.val
        node.next = node.next.next


