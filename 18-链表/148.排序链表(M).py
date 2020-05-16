"""
  @Author       : Liujianhan
  @Date         : 20/5/16 21:25
  @FileName     : 148.排序链表(M).py
  @ProjectName  : leetcode_in_python
  @Description  : 在 O(n log n) 时间复杂度和常数级空间复杂度下，对链表进行排序。
    示例 1:
    输入: 4->2->1->3
    输出: 1->2->3->4
    示例 2:
    输入: -1->5->3->4->0
    输出: -1->0->3->4->5
 """


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # 作弊写法，空间不满足要求，使用了内置排序算法
    # 76ms, 20.8MB
    @classmethod
    def sort_list(cls, head: ListNode) -> ListNode:
        ptr = head
        queue = []
        while ptr is not None:
            queue.append(ptr.val)
            ptr = ptr.next
        ptr = head
        for item in sorted(queue):
            ptr.val = item
            ptr = ptr.next
        return head

    # 292ms, 20.6MB
    @classmethod
    def sort_list_v2(cls, head: ListNode) -> ListNode:
        h, length, intv = head, 0, 1
        while h:
            h, length = h.next, length + 1
        res = ListNode(0)
        res.next = head
        while intv < length:
            pre, h = res, res.next
            while h:
                h1, i = h, intv
                while i and h: h, i = h.next, i - 1
                if i: break
                h2, i = h, intv
                while i and h: h, i = h.next, i - 1
                c1, c2 = intv, intv - i
                while c1 and c2:
                    if h1.val < h2.val:
                        pre.next, h1, c1 = h1, h1.next, c1 - 1
                    else:
                        pre.next, h2, c2 = h2, h2.next, c2 - 1
                    pre = pre.next
                pre.next = h1 if c1 else h2
                while c1 > 0 or c2 > 0: pre, c1, c2 = pre.next, c1 - 1, c2 - 1
                pre.next = h
            intv *= 2
        return res.next
