"""
  User: Liujianhan
  Time: 17:41
  用两个栈来实现一个队列，完成队列的Push和Pop操作。 队列中的元素为int类型。
 """
__author__ = 'liujianhan'


class CQueue:
    def __init__(self):
        self.st1 = []
        self.st2 = []

    def append_tail(self, value: int) -> None:
        self.st1.append(value)

    def delete_head(self) -> int:
        if not self.st2:
            while self.st1:
                cur = self.st1.pop()
                self.st2.append(cur)
        return self.st2.pop() if self.st2 else -1


if __name__ == '__main__':
    pass
