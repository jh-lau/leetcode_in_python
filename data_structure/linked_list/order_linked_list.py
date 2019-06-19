"""
  Created by PyCharm.
  User: Liujianhan
  Date: 2019/5/31
  Time: 6:39
 """
__author__ = 'liujianhan'
from .linked_list import LList


class LList2(LList):
    def sort(self):
        p = self._head
        if p is None or p.next is None:
            return
        rem = p.next
        p.next = None
        while rem is not None:
            p = self._head
            q = None
            while p is not None and p.elem <= rem.elem:
                q = p
                p = p.next
            if q is None:
                self._head = rem
            else:
                q.next = rem
            q = rem
            rem = rem.next
            q.next = p
