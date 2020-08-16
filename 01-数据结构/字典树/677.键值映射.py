"""
  @Author       : liujianhan
  @Date         : 2020/3/17 上午9:41
  @Project      : leetcode_in_python
  @FileName     : 677.键值映射.py
  @Description  : 实现一个 MapSum 类里的两个方法，insert 和 sum。
    对于方法 insert，你将得到一对（字符串，整数）的键值对。字符串表示键，整数表示值。如果键已经存在，那么原来的键值对将被替代成新的键值对。
    对于方法 sum，你将得到一个表示前缀的字符串，你需要返回所有以该前缀开头的键的值的总和。

    输入: insert("apple", 3), 输出: Null
    输入: sum("ap"), 输出: 3
    输入: insert("app", 2), 输出: Null
    输入: sum("ap"), 输出: 5
"""


class MapSum:
    # 40ms, 13.6M --> 45.64%, 6.98%
    def __init__(self):
        self.lookup = {}

    def insert(self, key: str, val: int) -> None:
        tree = self.lookup
        for k in key:
            if k not in tree:
                tree[k] = {}
            tree = tree[k]
        tree['val'] = val

    def sum(self, prefix: str) -> int:
        tree = self.lookup
        for p in prefix:
            if p not in tree:
                return 0
            tree = tree[p]
        ans = 0

        def dfs(t):
            for c in t:
                if c == 'val':
                    nonlocal ans
                    ans += t[c]
                else:
                    dfs(t[c])

        dfs(tree)

        return ans


if __name__ == '__main__':
    ms = MapSum()
    print(ms.insert('apple', 3))
    print(ms.sum('ap'))
    print(ms.insert('app', 2))
    print(ms.sum('ap'))
