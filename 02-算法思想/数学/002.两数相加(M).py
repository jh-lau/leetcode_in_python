"""
  @Author       : liujianhan
  @Date         : 2020/4/7 下午2:30
  @Project      : leetcode_in_python
  @FileName     : 002.两数相加(M).py
  @Description  : 给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，
    并且它们的每个节点只能存储一位数字。
    如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。
    您可以假设除了数字 0 之外，这两个数都不会以 0 开头。
    示例：

    输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
    输出：7 -> 0 -> 8
    原因：342 + 465 = 807
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # 84ms, 13.8MB
    @classmethod
    def add_two_numbers(cls, l1: ListNode, l2: ListNode) -> ListNode:
        carry = 0
        temp_res = res = ListNode(0)
        while l1 or l2:
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0
            temp_sum = sum([x, y, carry])
            carry = temp_sum // 10
            temp_res.next = ListNode(temp_sum % 10)
            temp_res = temp_res.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        if carry:
            temp_res.next = ListNode(1)
        return res.next

    # 88ms, 13.7MB
    @classmethod
    def add_two_numbers_v2(cls, l1: ListNode, l2: ListNode) -> ListNode:
        carry = 0
        temp_res = res = ListNode(0)
        while l1 or l2 or carry:
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0
            s = x + y + carry
            carry = s // 10
            s %= 10
            res.next = ListNode(s)
            res = res.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        return temp_res.next
