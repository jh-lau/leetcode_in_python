"""
  @Author       : liujianhan
  @Date         : 2020/4/15 上午10:49
  @Project      : leetcode_in_python
  @FileName     : 02.06.回文链表.py
  @Description  : 编写一个函数，检查输入的链表是否是回文的。
    示例 1：

    输入： 1->2
    输出： false
    示例 2：

    输入： 1->2->2->1
    输出： true

    进阶：
    你能否用 O(n) 时间复杂度和 O(1) 空间复杂度解决此题？
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # 84ms, 24MB
    @classmethod
    def is_palindrome(cls, head: ListNode) -> bool:
        temp = []
        while head:
            temp.append(head.val)
            head = head.next

        return temp == temp[::-1]

    # 84ms, 23.8MB
    @classmethod
    def is_palindrome_v2(cls, head: ListNode) -> bool:
        pre = ListNode(None)
        old_cur = head
        fast = head
        while fast and fast.next:
            fast = fast.next.next
            tmp_1 = old_cur.next
            old_cur.next = pre
            pre = old_cur
            old_cur = tmp_1
        if fast:
            old_cur = old_cur.next
        while old_cur:
            if pre.val != old_cur.val:
                return False
            pre = pre.next
            old_cur = old_cur.next

        return True


