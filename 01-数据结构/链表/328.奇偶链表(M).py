"""
  @Author       : liujianhan
  @Date         : 2020/11/13 10:05
  @Project      : leetcode_in_python
  @FileName     : 328.奇偶链表(M).py
  @Description  : 给定一个单链表，把所有的奇数节点和偶数节点分别排在一起。请注意，这里的奇数节点和偶数节点指的是节点编号的奇偶性，
    而不是节点的值的奇偶性。
    请尝试使用原地算法完成。你的算法的空间复杂度应为 O(1)，时间复杂度应为 O(nodes)，nodes 为节点总数。
    示例 1:

    输入: 1->2->3->4->5->NULL
    输出: 1->3->5->2->4->NULL
    示例 2:

    输入: 2->1->3->5->6->4->7->NULL
    输出: 2->3->6->7->1->5->4->NULL
    说明:

    应当保持奇数节点和偶数节点的相对顺序。
    链表的第一个节点视为奇数节点，第二个节点视为偶数节点，以此类推。
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # 52ms, 15.4MB
    @staticmethod
    def odd_even_list(head: ListNode) -> ListNode:
        if not head:
            return head
        even_head = head.next
        odd, even = head, even_head
        while even and even.next:
            # 更新奇数节点时，奇数节点的后一个节点需要指向偶数节点的后一个节点，因此令 odd.next = even.next，
            # 然后令 odd = odd.next，此时 odd 变成 even 的后一个节点。
            odd.next = even.next
            odd = odd.next
            # 更新偶数节点时，偶数节点的后一个节点需要指向奇数节点的后一个节点，因此令 even.next = odd.next，
            # 然后令 even = even.next，此时 even 变成 odd 的后一个节点。
            even.next = odd.next
            even = even.next
        odd.next = even_head

        return head


if __name__ == '__main__':
    pass
