"""
  @Author       : Liujianhan
  @Date         : 20/5/2 13:44
  @FileName     : 061.旋转链表(M).py
  @ProjectName  : leetcode_in_python
  @Description  : 给定一个链表，旋转链表，将链表每个节点向右移动 k 个位置，其中 k 是非负数。
    示例 1:
    输入: 1->2->3->4->5->NULL, k = 2
    输出: 4->5->1->2->3->NULL
    解释:
    向右旋转 1 步: 5->1->2->3->4->NULL
    向右旋转 2 步: 4->5->1->2->3->NULL
    示例 2:
    输入: 0->1->2->NULL, k = 4
    输出: 2->0->1->NULL
    解释:
    向右旋转 1 步: 2->0->1->NULL
    向右旋转 2 步: 1->2->0->NULL
    向右旋转 3 步: 0->1->2->NULL
    向右旋转 4 步: 2->0->1->NULL
 """


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # 48ms, 13.7MB
    @classmethod
    def rotate_right(cls, head: ListNode, k: int) -> ListNode:
        if not head:
            return head
        if not head.next:
            return head

        old_tail = head
        n = 1
        while old_tail.next:
            old_tail = old_tail.next
            n += 1
        old_tail.next = head

        new_tail = head
        for i in range(n - k % n - 1):
            new_tail = new_tail.next
        new_head = new_tail.next

        new_tail.next = None

        return new_head
