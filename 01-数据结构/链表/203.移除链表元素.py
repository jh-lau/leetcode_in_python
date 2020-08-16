"""
  @Author       : liujianhan
  @Date         : 2020/4/14 下午3:33
  @Project      : leetcode_in_python
  @FileName     : 203.移除链表元素.py
  @Description  : 删除链表中等于给定值 val 的所有节点。
    示例:

    输入: 1->2->6->3->4->5->6, val = 6
    输出: 1->2->3->4->5
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # 76ms, 24.4MB
    @classmethod
    def remove_elements(cls, head: ListNode, val: int) -> ListNode:
        if not head:
            return
        head.next = cls.remove_elements(head.next, val)

        return head.next if head.val == val else head

    # 92ms, 16.7MB
    @classmethod
    def remove_elements_v2(cls, head: ListNode, val: int) -> ListNode:
        sentinel = ListNode(0)
        sentinel.next = head

        prev, curr = sentinel, head
        while curr:
            if curr.val == val:
                prev.next = curr.next
            else:
                prev = curr
            curr = curr.next

        return sentinel.next
