"""
  @Author       : liujianhan
  @Date         : 21/3/5 9:32
  @Project      : leetcode_in_python
  @FileName     : 232.用栈实现队列.py
  @Description  : Placeholder
"""


class MyQueue:
    def __init__(self):
        self.a = []
        self.b = []

    def push(self, x: int) -> None:
        while self.b:
            self.a.append(self.b.pop())
        self.a.append(x)
        while self.a:
            self.b.append(self.a.pop())

    def pop(self) -> int:
        return self.b.pop()

    def peek(self) -> int:
        return self.b[-1]

    def empty(self) -> bool:
        return len(self.b) == 0


if __name__ == '__main__':
    pass
