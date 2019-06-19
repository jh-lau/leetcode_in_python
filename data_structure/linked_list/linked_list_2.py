"""
  Created by PyCharm.
  User: Liujianhan
  Date: 2019/5/30
  Time: 13:11
 """
__author__ = 'liujianhan'


class Node:
    def __init__(self, elem, next_=None):
        self.elem = elem
        self.next = next_

    def get_data(self):
        return self.elem

    def get_next(self):
        return self.next

    def set_data(self, new_data):
        self.elem = new_data

    def set_next(self, new_next):
        self.next = new_next


class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, data):
        # 头插法
        new_node = Node(data)
        new_node.set_next(self.head)
        self.head = new_node

    def search(self, data):
        # 查找结点是否存在
        present = self.head
        while present is not None:
            if present.get_data == data:
                return True
            present = present.get_next()
        return False

    def remove(self, data):
        present = self.head
        previous = None
        # 删除一般结点
        while present is not None:
            if present.get_data == data:
                break
            previous = present
            present = present.get_next()

        # 删除头结点
        if previous is None:
            self.head = present.get_next()
        else:
            previous.set_next(present.get_next())

    def is_empty(self):
        return self.head is None

    def size(self):
        count = 0
        counting = self.head
        while counting is not None:
            count += 1
            counting = counting.get_next()
        return count


class OrderedLinkedList:
    # 有序链表
    def __init__(self):
        self.head = None

    def add(self, data):
        present = self.head
        previous = None
        while present is not None:
            if present.get_data() > data:
                break
            previous = present
            present = present.get_next()

        new_node = Node(data)
        if previous is None:
            # 头插法
            new_node.set_next(self.head)
            self.head = new_node
        else:
            previous.set_next(new_node)
            new_node.set_next(present)

    def search(self, data):
        # 查找结点是否存在
        present = self.head
        while present is not None:
            if present.get_data() == data:
                return True
            elif present.get_data() > data:
                return False
            present = present.get_next()
        return False

    def remove(self, data):
        present = self.head
        previous = None
        # 删除一般结点
        while present is not None:
            if present.get_data == data:
                break
            previous = present
            present = present.get_next()

        # 删除头结点
        if previous is None:
            self.head = present.get_next()
        else:
            previous.set_next(present.get_next())

    def is_empty(self):
        return self.head is None

    def size(self):
        count = 0
        counting = self.head
        while counting is not None:
            count += 1
            counting = counting.get_next()
        return count


