"""
  @Author       : Liujianhan
  @Date         : 20/4/26 22:37
  @FileName     : 024.两两交换链表中的节点(M).py
  @ProjectName  : leetcode_in_python
  @Description  : 给定一个链表，两两交换其中相邻的节点，并返回交换后的链表。
    你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。
    示例:
    给定 1->2->3->4, 你应该返回 2->1->4->3.
 """


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # 40ms, 13.7MB
    @classmethod
    def swap_pairs(cls, head: ListNode) -> ListNode:
        """迭代"""
        dummy = ListNode(-1)
        dummy.next = head

        prev_node = dummy

        while head and head.next:
            first_node = head;
            second_node = head.next;

            prev_node.next = second_node
            first_node.next = second_node.next
            second_node.next = first_node

            prev_node = first_node
            head = first_node.next

        return dummy.next

    # 48ms, 13.5MB
    @classmethod
    def swap_pairs_v2(cls, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head

        first_node = head
        second_node = head.next

        first_node.next = cls.swap_pairs_v2(second_node.next)
        second_node.next = first_node

        return second_node