"""
  @Author       : liujianhan
  @Date         : 2020/3/26 上午11:45
  @Project      : leetcode_in_python
  @FileName     : 160.相交链表.py
  @Description  : 编写一个程序，找到两个单链表相交的起始节点。
  输入：intersectVal = 8, listA = [4,1,8,4,5], listB = [5,0,1,8,4,5], skipA = 2, skipB = 3
    输出：Reference of the node with value = 8
    输入解释：相交节点的值为 8 （注意，如果两个列表相交则不能为 0）。从各自的表头开始算起，链表 A 为 [4,1,8,4,5]，链表 B 为 [5,0,1,8,4,5]。在 A 中，相交节点前有 2 个节点；在 B 中，相交节点前有 3 个节点。

    如果两个链表没有交点，返回 null.
    在返回结果后，两个链表仍须保持原有的结构。
    可假定整个链表结构中没有循环。
    程序尽量满足 O(n) 时间复杂度，且仅用 O(1) 内存。
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # 180ms, 28.8MB
    @classmethod
    def get_intersection_node(cls, head_a: ListNode, head_b: ListNode) -> ListNode:
        ha, hb = head_a, head_b
        while ha != hb:
            ha = ha.next if ha else head_b
            hb = hb.next if hb else head_a

        return ha


if __name__ == '__main__':
    pass
