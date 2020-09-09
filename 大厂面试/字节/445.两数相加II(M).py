"""
  @Author       : liujianhan
  @Date         : 2020/4/14 下午3:26
  @Project      : leetcode_in_python
  @FileName     : 445.两数相加II(M).py
  @Description  : 给你两个 非空 链表来代表两个非负整数。数字最高位位于链表开始位置。它们的每个节点只存储一位数字。
    将这两数相加会返回一个新的链表。
    你可以假设除了数字 0 之外，这两个数字都不会以零开头。
    进阶：
    如果输入链表不能修改该如何处理？换句话说，你不能对列表中的节点进行翻转。
    示例：

    输入：(7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
    输出：7 -> 8 -> 0 -> 7
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # 88ms, 13.4MB
    @classmethod
    def add_two_numbers(cls, l1: ListNode, l2: ListNode) -> ListNode:
        s1, s2 = [], []
        while l1:
            s1.append(l1.val)
            l1 = l1.next

        while l2:
            s2.append(l2.val)
            l2 = l2.next

        ans = None
        carry = 0
        while s1 or s2 or carry:
            a = 0 if not s1 else s1.pop()
            b = 0 if not s2 else s2.pop()
            cur = sum([a, b, carry])
            carry = cur // 10
            cur %= 10
            cur_node = ListNode(cur)
            cur_node.next = ans
            ans = cur_node

        return ans
