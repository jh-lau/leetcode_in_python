"""
  @Author       : liujianhan
  @Date         : 2020/5/14 下午1:49
  @Project      : leetcode_in_python
  @FileName     : 147.对链表进行插入排序(M).py
  @Description  : 对链表进行插入排序。
    插入排序算法：
    插入排序是迭代的，每次只移动一个元素，直到所有元素可以形成一个有序的输出列表。
    每次迭代中，插入排序只从输入数据中移除一个待排序的元素，找到它在序列中适当的位置，并将其插入。
    重复直到所有输入数据插入完为止。
    示例 1：
    输入: 4->2->1->3
    输出: 1->2->3->4
    示例 2：
    输入: -1->5->3->4->0
    输出: -1->0->3->4->5
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # 212ms, 15.4MB
    @classmethod
    def insertion_sort_list(cls, head: ListNode) -> ListNode:
        dummy = ListNode(float('-inf'))
        pre = dummy
        tail = dummy
        cur = head
        while cur:
            if tail.val < cur.val:
                tail.next = cur
                tail = cur
                cur = cur.next
            else:
                tmp = cur.next
                tail.next = tmp
                while pre.next and pre.next.val < cur.val:
                    pre = pre.next
                cur.next = pre.next
                pre.next = cur
                pre = dummy
                cur = tmp

        return dummy.next

