"""
  User: Liujianhan
  Time: 15:51
 """
__author__ = 'liujianhan'


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    @staticmethod
    def merge_two_lists(l1, l2):
        h = ListNode(-1)
        cur = h

        cur1 = l1
        cur2 = l2

        while cur1 is not None and cur2 is not None:
            if cur1.val <= cur2.val:
                cur.next = cur1
                cur1 = cur1.next
            else:
                cur.next = cur2
                cur2 = cur2.next
            cur = cur.next

        if cur1 is not None:
            cur.next = cur1

        if cur2 is not None:
            cur.next = cur2
        return h.next
