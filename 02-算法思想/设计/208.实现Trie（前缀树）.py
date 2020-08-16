"""
  @Author       : liujianhan
  @Date         : 2020/3/16 下午6:47
  @Project      : leetcode_in_python
  @FileName     : 208.实现Trie（前缀树）.py
  @Description  : 实现一个 Trie (前缀树)，包含 insert, search, 和 startsWith 这三个操作。
  你可以假设所有的输入都是由小写字母 a-z 构成的。
  保证所有输入均为非空字符串。
"""


class Trie:
    def __init__(self):
        self.lookup = {}

    def insert(self, word: str) -> None:
        tree = self.lookup
        for a in word:
            if a not in tree:
                tree[a] = {}
            tree = tree[a]
        tree['#'] = '#'

    def search(self, word: str) -> bool:
        tree = self.lookup
        for a in word:
            if a not in tree:
                return False
            tree = tree[a]
        if '#' in tree:
            return True
        return False

    def starts_with(self, prefix: str) -> bool:
        tree = self.lookup
        for a in prefix:
            if a not in tree:
                return False
            tree = tree[a]
        return True


if __name__ == '__main__':
    trie = Trie()
    trie.insert('apple')
    print(trie.search('apple'))
    print(trie.search('app'))
    print(trie.starts_with('app'))
    trie.insert('app')
    print(trie.search('app'))