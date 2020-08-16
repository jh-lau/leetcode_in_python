"""
  @Author       : liujianhan
  @Date         : 2020/4/14 下午3:53
  @Project      : leetcode_in_python
  @FileName     : 234.回文链表.py
  @Description  : 请判断一个链表是否为回文链表。
    示例 1:

    输入: 1->2
    输出: false
    示例 2:

    输入: 1->2->2->1
    输出: true
    进阶：
    你能否用 O(n) 时间复杂度和 O(1) 空间复杂度解决此题？
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # 92ms, 23.9MB
    @classmethod
    def is_palindrome(cls, head: ListNode) -> bool:
        """将值复制到数组中判断是否回文"""
        val_list = []
        cur = head
        while cur:
            val_list.append(cur.val)
            cur = cur.next

        return val_list == val_list[::-1]

    # 84ms, 23.8MB
    @classmethod
    def is_palindrome_v2(cls, head: ListNode) -> bool:
        """双指针"""
        rev = None
        fast, slow = head, head

        while fast and fast.next:
            fast = fast.next.next
            rev, rev.next, slow = slow, rev, slow.next

        if fast:
            slow = slow.next

        while rev and rev.val == slow.val:
            rev, slow = rev.next, slow.next

        return not rev

