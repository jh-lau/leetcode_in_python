"""
  Created by PyCharm.
  User: Liujianhan
  Date: 2019/5/30
  Time: 13:11
 """
__author__ = 'liujianhan'


class LNode:
    def __init__(self, elem, next_=None):
        self.elem = elem
        self.next = next_


class LList:
    def __init__(self):
        self._head = None

    def is_empty(self):
        return self._head is None

    def prepend(self, elem):
        # 表头插入数据
        self._head = LNode(elem, self._head)

    def append(self, elem):
        # 表尾插入数据
        if self._head is None:
            self._head = LNode(elem)
            return
        p = self._head
        while p.next is not None:
            p = p.next
        p.next = LNode(elem)

    def pop(self):
        # 删除表头元素并返回该元素
        if self._head is None:
            return '空表'
        e = self._head.elem
        self._head = self._head.next
        return e

    def pop_last(self):
        # 删除表尾数据并返回
        if self._head is None:
            return '空表'
        p = self._head
        if p.next is None:
            e = p.elem
            self._head = None
            return e
        while p.next.next is not None:
            p = p.next
        e = p.next.elem
        p.next = None
        return e

    def find(self, pred):
        # 寻找满足给定条件的表元素
        p = self._head
        while p is not None:
            if pred(p.elem):
                return p.elem
            p = p.next

    def print_all(self):
        p = self._head
        while p is not None:
            print(p.elem, end='')
            if p.next is not None:
                print(', ', end='')
            p = p.next
        print('')


class LList1(LList):
    # 添加尾结点引用的单链表，提高尾端加入数据的效率
    def __init__(self):
        LList.__init__(self)
        self._rear = None

    def prepend(self, elem):
        if self._rear is None:  # 空表
            self._head = LNode(elem, self._head)
            self._rear = self._head
        else:
            self._head = LNode(elem, self._head)

    def append(self, elem):
        if self._head is None:  # 空表
            self._head = LNode(elem, self._head)
            self._rear = self._head
        else:
            self._rear.next = LNode(elem)
            self._rear = self._rear.next

    def pop_last(self):
        if self._head is None:
            return '空表'
        p = self._head
        if p.next is None:
            e = p.elem
            self._head = None
            return e
        while p.next.next is not None:
            p = p.next
        e = p.next.elem
        p.next = None
        self._rear = p
        return e


def test(num):
    if num == 1:
        return 'hello'


mlist1 = LList()
for i in range(10):
    mlist1.prepend(i)
for i in range(11, 20):
    mlist1.append(i)
mlist1.print_all()
print(mlist1.find(test))
