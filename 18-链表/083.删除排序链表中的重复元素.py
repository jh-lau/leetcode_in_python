"""
  @Author       : liujianhan
  @Date         : 2020/3/21 上午10:47
  @Project      : leetcode_in_python
  @FileName     : 083.删除排序链表中的重复元素.py
  @Description  : 给定一个排序链表，删除所有重复的元素，使得每个元素只出现一次。
  输入: 1->1->2
    输出: 1->2
  输入: 1->1->2->3->3
    输出: 1->2->3
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # 68ms, 13.5MB
    def delete_duplicates(self, head: ListNode) -> ListNode:
        if head:
            head.next = self.delete_duplicates(head.next)
            return head.next if head.next and head.val == head.next.val else head


def create_list():
    head = ListNode(1)
    cur = head
    cur.next = ListNode(1)
    cur.next.next = ListNode(2)
    cur.next.next.next = ListNode(3)
    return head


def print_list(head):
    cur = head
    while cur is not None:
        print(cur.val, '-->', end=' ')
        cur = cur.next

    print('NULL')


if __name__ == '__main__':
    head = create_list()
    print_list(head)
    print_list(Solution().delete_duplicates(head))
