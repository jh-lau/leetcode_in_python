"""
  @Author       : Liujianhan
  @Date         : 20/4/26 22:41
  @FileName     : 025.K个一组翻转链表.py
  @ProjectName  : leetcode_in_python
  @Description  : 给你一个链表，每 k 个节点一组进行翻转，请你返回翻转后的链表。
    k 是一个正整数，它的值小于或等于链表的长度。
    如果节点总数不是 k 的整数倍，那么请将最后剩余的节点保持原有顺序。
    示例：
    给你这个链表：1->2->3->4->5
    当 k = 2 时，应当返回: 2->1->4->3->5
    当 k = 3 时，应当返回: 3->2->1->4->5
    说明：
    你的算法只能使用常数的额外空间。
    你不能只是单纯的改变节点内部的值，而是需要实际进行节点交换。
 """


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # 56ms, 14.3MB
    @classmethod
    def reverse_k_group(cls, head: ListNode, k: int) -> ListNode:
        stack = []
        p = ListNode(-1)
        result = p
        flag = True
        while head:
            for i in range(k):
                if not head:
                    flag = False
                    break
                stack.append(head)
                head = head.next
            if not flag:
                break
            else:
                temp_head = head
            for i in range(k):
                cur = stack.pop()
                p.next = cur
                p = cur
            p.next = temp_head

        return result.next