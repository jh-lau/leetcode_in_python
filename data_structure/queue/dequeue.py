"""
  Created by PyCharm.
  User: Liujianhan
  Date: 2019/5/30
  Time: 12:47
 """
__author__ = 'liujianhan'


class DeQueueTest:
    def __init__(self):
        self.items = []

    def enqueue_end(self, item):
        self.items.append(item)

    def enqueue_head(self, item):
        self.items.insert(0, item)

    def dequeue_end(self):
        return self.items.pop()

    def dequeue_head(self):
        return self.items.pop(0)

    def is_empty(self):
        return 0 == len(self.items)

    def size(self):
        return len(self.items)


def is_palindromic(string):
    dequeue = DeQueueTest()

    for ch in string:
        dequeue.enqueue_head(ch)

    while dequeue.size() > 1:
        head_ch = dequeue.dequeue_head()
        end_ch = dequeue.dequeue_end()
        if head_ch != end_ch:
            return False
    return True


def main():
    word_list = ['random', 'carrac', 'dooooood', '12321', 'helloworld']
    for word in word_list:
        print(f"'{word}' is palindromic number? {is_palindromic(word)}")
        print('--------------')


if __name__ == '__main__':
    main()
