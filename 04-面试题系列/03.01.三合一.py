"""
  @Author       : Liujianhan
  @Date         : 20/4/12 21:50
  @FileName     : 03.01.三合一.py
  @ProjectName  : leetcode_in_python
  @Description  : 三合一。描述如何只用一个数组来实现三个栈。
    你应该实现push(stackNum, value)、pop(stackNum)、isEmpty(stackNum)、peek(stackNum)方法。stackNum表示栈下标，value表示压入的值。
    构造函数会传入一个stackSize参数，代表每个栈的大小。

    示例1:

     输入：
    ["TripleInOne", "push", "push", "pop", "pop", "pop", "isEmpty"]
    [[1], [0, 1], [0, 2], [0], [0], [0], [0]]
     输出：
    [null, null, null, 1, -1, -1, true]
    说明：当栈为空时`pop, peek`返回-1，当栈满时`push`不压入元素。
    示例2:

     输入：
    ["TripleInOne", "push", "push", "push", "pop", "pop", "pop", "peek"]
    [[2], [0, 1], [0, 2], [0, 3], [0], [0], [0], [0]]
     输出：
    [null, null, null, null, 2, 1, -1, -1]
 """


# 176ms, 20.6MB
class TripleInOne:
    def __init__(self, stack_size: int):
        self.stacks = [[], [], []]
        self.stack_size = stack_size

    def push(self, stack_num: int, value: int) -> None:
        if len(self.stacks[stack_num-1]) < self.stack_size:
            self.stacks[stack_num-1].append(value)

    def pop(self, stack_num: int) -> int:
        if self.stacks[stack_num - 1]:
            return self.stacks[stack_num-1].pop()
        else:
            return -1

    def peek(self, stack_num: int) -> int:
        if self.stacks[stack_num-1]:
            return self.stacks[stack_num-1][-1]
        else:
            return -1

    def is_empty(self, stack_num: int) -> bool:
        return self.stacks[stack_num-1] == []
