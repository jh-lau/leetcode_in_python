"""
  User: Liujianhan
  Time: 17:21
  输入一个链表，按链表从尾到头的顺序返回一个ArrayList
 """
__author__ = 'liujianhan'


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    @staticmethod
    def print_list_from_tail_to_head(list_node):
        return list(list_node) if not list_node else list_node[::-1]

    @staticmethod
    def another_method(list_node):
        if not list_node:
            return []
        result = []
        while list_node:
            result.insert(0, list_node.val)
            list_node = list_node.next
        return result


print(Solution().print_list_from_tail_to_head([1, 2, 3]))
print(Solution().print_list_from_tail_to_head({}))
