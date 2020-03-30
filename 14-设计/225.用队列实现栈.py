"""
  @Author       : liujianhan
  @Date         : 2020/3/30 上午10:07
  @Project      : leetcode_in_python
  @FileName     : 225.用队列实现栈.py
  @Description  : 使用队列实现栈的下列操作：
push(x) -- 元素 x 入栈
pop() -- 移除栈顶元素
top() -- 获取栈顶元素
empty() -- 返回栈是否为空

你只能使用队列的基本操作-- 也就是 push to back, peek/pop from front, size, 和 is empty 这些操作是合法的。
你所使用的语言也许不支持队列。 你可以使用 list 或者 deque（双端队列）来模拟一个队列 , 只要是标准的队列操作即可。
你可以假设所有操作都是有效的（例如, 对一个空的栈不会调用 pop 或者 top 操作）。
"""
from collections import deque


# 36ms, 13.8MB
class MyStack:
    def __init__(self):
        self.stack = deque()

    def push(self, x: int) -> None:
        self.stack.appendleft(x)

    def pop(self) -> int:
        if self.stack:
            return self.stack.popleft()

    def top(self) -> int:
        if self.stack:
            return self.stack[0]

    def empty(self) -> bool:
        return not bool(self.stack)


if __name__ == '__main__':
    obj = MyStack()
    obj.push(1)
    obj.push(2)
    print(obj.top())
    print(obj.pop())
    print(obj.empty())
