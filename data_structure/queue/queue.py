"""
  Created by PyCharm.
  User: Liujianhan
  Date: 2019/5/30
  Time: 12:04
 """
__author__ = 'liujianhan'


class QueueTest:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        item = self.items.pop()
        return item

    def is_empty(self):
        return 0 == len(self.items)

    def size(self):
        return len(self.items)


def da_tao_sha(name_list, kill_num):
    queue = QueueTest()
    for name in name_list:
        queue.enqueue(name)

    # 此处>1不能省略，否则当最后一个元素出列后，return语句会再次pop一个元素，而此时队列已经为空，会报错
    while queue.size() > 1:
        for i in range(1, kill_num):
            queue.enqueue(queue.dequeue())
        print(f"Kill the number {queue.dequeue()} ")

    return queue.dequeue()


def main():
    kill_num = 7
    origin_list = list(range(1, 41))
    safe_name = da_tao_sha(origin_list, kill_num)
    print('------------------')
    print(f"Safe number is {safe_name}")


if __name__ == '__main__':
    main()
