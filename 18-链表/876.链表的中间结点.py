"""
  @Author       : liujianhan
  @Date         : 2020/4/15 上午10:35
  @Project      : leetcode_in_python
  @FileName     : 876.链表的中间结点.py
  @Description  : 给定一个带有头结点 head 的非空单链表，返回链表的中间结点。
    如果有两个中间结点，则返回第二个中间结点。
    示例 1：

    输入：[1,2,3,4,5]
    输出：此列表中的结点 3 (序列化形式：[3,4,5])
    返回的结点值为 3 。 (测评系统对该结点序列化表述是 [3,4,5])。
    注意，我们返回了一个 ListNode 类型的对象 ans，这样：
    ans.val = 3, ans.next.val = 4, ans.next.next.val = 5, 以及 ans.next.next.next = NULL.
    示例 2：

    输入：[1,2,3,4,5,6]
    输出：此列表中的结点 4 (序列化形式：[4,5,6])
    由于该列表有两个中间结点，值分别为 3 和 4，我们返回第二个结点。
    提示：
    给定链表的结点数介于 1 和 100 之间。
"""


class ListNode:
    def __int__(self, x):
        self.val = x
        self.next = None


class Solution:
    # 40ms, 13.7MB
    @classmethod
    def middle_node(cls, head: ListNode) -> ListNode:
        """数组"""
        array = [head]
        while array[-1].next:
            array.append(array[-1].next)

        return array[len(array) // 2]

    # 40ms, 13.5MB
    @classmethod
    def middle_node_v2(cls, head: ListNode) -> ListNode:
        """单指针"""
        n, cur = 0, head
        while cur:
            n += 1
            cur = cur.next
        k, cur = 0, head
        while k < n // 2:
            k += 1
            cur = cur.next

        return cur

    # 32ms, 13.6MB
    @classmethod
    def middle_node_v3(cls, head: ListNode) -> ListNode:
        """快慢指针"""
        fast = slow = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow
