"""
  @Author       : liujianhan
  @Date         : 2020/4/14 下午3:42
  @Project      : leetcode_in_python
  @FileName     : 206.反转链表.py
  @Description  : 反转一个单链表。
    示例:

    输入: 1->2->3->4->5->NULL
    输出: 5->4->3->2->1->NULL
    进阶:
    你可以迭代或递归地反转链表。你能否用两种方法解决这道题？
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # 60ms, 14.7MB
    @classmethod
    def reverse_list(cls, head: ListNode) -> ListNode:
        p, rev = head, None
        while p:
            rev, rev.next, p = p, rev, p.next

        return rev

    # 80ms, 18.5MB
    @classmethod
    def reverse_list_v2(cls, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        p = cls.reverse_list_v2(head.next)
        head.next.next = head
        head.next = None

        return p

    # 40ms, 14.5MB
    @classmethod
    def reverse_list_v3(cls, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head

        cur, pre, temp = head, None, None
        while cur:
            temp = cur.next
            cur.next = pre
            pre = cur
            cur = temp

        return pre
