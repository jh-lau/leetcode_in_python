"""
  @Author       : liujianhan
  @Date         : 2020/3/24 下午1:56
  @Project      : leetcode_in_python
  @FileName     : 141.环形链表.py
  @Description  : 给定一个链表，判断链表中是否有环。
为了表示给定链表中的环，我们使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。 如果 pos 是 -1，则在该链表中没有环。
输入：head = [3,2,0,-4], pos = 1
输出：true
解释：链表中有一个环，其尾部连接到第二个节点。
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # 48ms, 16.7MB
    @classmethod
    def has_cycle(cls, head: ListNode) -> bool:
        if head is None:
            return False
        slow, quick = head, head
        while quick.next is not None and quick.next.next is not None:
            slow = slow.next
            quick = quick.next.next
            if slow == quick:
                return True
        return False


if __name__ == '__main__':
    pass
