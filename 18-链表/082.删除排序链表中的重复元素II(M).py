"""
  @Author       : Liujianhan
  @Date         : 20/5/5 15:59
  @FileName     : 082.删除排序链表中的重复元素II(M).py
  @ProjectName  : leetcode_in_python
  @Description  : 给定一个排序链表，删除所有含有重复数字的节点，只保留原始链表中 没有重复出现 的数字。
    示例 1:
    输入: 1->2->3->3->4->4->5
    输出: 1->2->5
    示例 2:
    输入: 1->1->1->2->3
    输出: 2->3
 """


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # 52ms, 13.5MB
    @classmethod
    def delete_duplicates(cls, head: ListNode) -> ListNode:
        thead = ListNode('a')
        thead.next = head
        pre, cur = None, thead
        while cur:
            pre = cur
            cur = cur.next
            while cur and cur.next and cur.next.val == cur.val:
                t = cur.val
                while cur and cur.val == t:
                    cur = cur.next
                pre.next = cur

        return thead.next
