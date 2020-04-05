"""
  @Author       : Liujianhan
  @Date         : 20/4/5 12:28
  @FileName     : 460.LFU缓存(H).py
  @ProjectName  : leetcode_in_python
  @Description  : 设计并实现最不经常使用（LFU）缓存的数据结构。它应该支持以下操作：get 和 put。
    get(key) - 如果键存在于缓存中，则获取键的值（总是正数），否则返回 -1。
    put(key, value) - 如果键不存在，请设置或插入值。当缓存达到其容量时，它应该在插入新项目之前，使最不经常使用的项目无效。在此问题中，当存在平局（即两个或更多个键具有相同使用频率）时，最近最少使用的键将被去除。
    进阶：
    你是否可以在 O(1) 时间复杂度内执行两项操作？

    LFUCache cache = new LFUCache( 2 /* capacity (缓存容量) */ );
    cache.put(1, 1);
    cache.put(2, 2);
    cache.get(1);       // 返回 1
    cache.put(3, 3);    // 去除 key 2
    cache.get(2);       // 返回 -1 (未找到key 2)
    cache.get(3);       // 返回 3
    cache.put(4, 4);    // 去除 key 1
    cache.get(1);       // 返回 -1 (未找到 key 1)
    cache.get(3);       // 返回 3
    cache.get(4);       // 返回 4
 """
from collections import defaultdict


class Node:
    def __init__(self, key: int, val: int, pre: int = None, nex: int = None, freq: int = 0):
        self.pre = pre
        self.nex = nex
        self.freq = freq
        self.val = val
        self.key = key

    def insert(self, nex) -> None:
        nex.pre = self
        nex.nex = self.nex
        self.nex.pre = nex
        self.nex = nex


def create_linked_list() -> tuple:
    head = Node(0, 0)
    tail = Node(0, 0)
    head.nex = tail
    tail.pre = head

    return head, tail


class LFUCache:
    # 464ms, 23.3MB
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.min_freq = 0
        self.freq_map = defaultdict(create_linked_list)
        self.key_map = dict()

    def delete(self, node) -> int:
        if node.pre:
            node.pre.nex = node.nex
            node.nex.pre = node.pre
            if node.pre is self.freq_map[node.freq][0] and node.nex is self.freq_map[node.freq][-1]:
                self.freq_map.pop(node.freq)

        return node.key

    def increase(self, node) -> None:
        node.freq += 1
        self.delete(node)
        self.freq_map[node.freq][-1].pre.insert(node)
        if node.freq == 1:
            self.min_freq = 1
        elif self.min_freq == node.freq - 1:
            head, tail = self.freq_map[node.freq - 1]
            if head.nex is tail:
                self.min_freq = node.freq

    def get(self, key: int) -> int:
        if key in self.key_map:
            self.increase(self.key_map[key])
            return self.key_map[key].val

        return -1

    def put(self, key: int, value: int) -> None:
        if self.capacity:
            if key in self.key_map:
                node = self.key_map[key]
                node.val = value
            else:
                node = Node(key, value)
                self.key_map[key] = node
                self.size += 1
            if self.size > self.capacity:
                self.size -= 1
                deleted = self.delete(self.freq_map[self.min_freq][0].nex)
                self.key_map.pop(deleted)
            self.increase(node)


if __name__ == '__main__':
    cache = LFUCache(2)
    cache.put(1, 1)
    cache.put(2, 2)
    print(cache.get(1))
    cache.put(3, 3)
    print(cache.get(2))
    print(cache.get(3))
    cache.put(4, 4)
    print(cache.get(1))
    print(cache.get(3))
    print(cache.get(4))