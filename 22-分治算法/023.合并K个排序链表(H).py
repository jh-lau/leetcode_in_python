"""
  @Author       : Liujianhan
  @Date         : 20/4/26 22:29
  @FileName     : 023.合并K个排序链表(H).py
  @ProjectName  : leetcode_in_python
  @Description  : 合并 k 个排序链表，返回合并后的排序链表。请分析和描述算法的复杂度。
    示例:
    输入:
    [
      1->4->5,
      1->3->4,
      2->6
    ]
    输出: 1->1->2->3->4->4->5->6
 """
from typing import List


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    @staticmethod
    def merge(node_a, node_b):
        dummy = ListNode(None)
        cursor_a, cursor_b, cursor_res = node_a, node_b, dummy
        while cursor_a and cursor_b:  # 对两个节点的 val 进行判断，直到一方的 next 为空
            if cursor_a.val <= cursor_b.val:
                cursor_res.next = ListNode(cursor_a.val)
                cursor_a = cursor_a.next
            else:
                cursor_res.next = ListNode(cursor_b.val)
                cursor_b = cursor_b.next
            cursor_res = cursor_res.next
        # 有一方的next的为空，就没有比较的必要了，直接把不空的一边加入到结果的 next 上
        if cursor_a:
            cursor_res.next = cursor_a
        if cursor_b:
            cursor_res.next = cursor_b
        return dummy.next

    # 184ms, 18.8MB
    def merge_k_lists(self, lists: List[ListNode]) -> ListNode:
        length = len(lists)

        # 边界情况
        if length == 0:
            return None
        if length == 1:
            return lists[0]

        # 分治
        mid = length // 2
        return self.merge(self.merge_k_lists(lists[:mid]), self.merge_k_lists(lists[mid:length]))

    # 96ms, 16.7MB
    @classmethod
    def merge_k_lists_v(cls, lists: List[ListNode]) -> ListNode:
        pre = ListNode(-1)
        tmp = pre
        nodes = []
        k = len(lists)
        for i in range(k):
            l = lists[i]
            while l:
                nodes.append(l)
                l = l.next
        nodes = sorted(nodes, key=lambda x: x.val)
        for node in nodes:
            tmp.next = node
            tmp = tmp.next

        return pre.next


if __name__ == '__main__':
    pass
