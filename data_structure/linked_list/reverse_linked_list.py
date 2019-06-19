"""
  Created by PyCharm.
  User: Liujianhan
  Date: 2019/5/31
  Time: 6:39
 """
__author__ = 'liujianhan'
from .linked_list import LList


class LList2(LList):
    def rev(self):
        p = None
        while self._head is not None:
            q = self._head
            self._head = q.next
            q.next = p
            p = q
        self._head = p
