"""
  @Author       : Liujianhan
  @Date         : 20/4/12 21:37
  @FileName     : 02.02.返回倒数第k个节点.py
  @ProjectName  : leetcode_in_python
  @Description  : 实现一种算法，找出单向链表中倒数第 k 个节点。返回该节点的值。
    注意：本题相对原题稍作改动
    示例：

    输入： 1->2->3->4->5 和 k = 2
    输出： 4
    说明：

    给定的 k 保证是有效的。
 """


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # 32ms, 13.7Mb
    @classmethod
    def kth_to_last(cls, head: ListNode, k: int) -> int:
        fast, slow = head, head
        while k > 0:
            fast = fast.next
            k -= 1
        while fast is not None:
            fast = fast.next
            slow = slow.next

        return slow.val



