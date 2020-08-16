"""
  @Author       : Liujianhan
  @Date         : 20/6/15 22:15
  @FileName     : 211.添加与搜索单词 - 数据结构设计(M).py
  @ProjectName  : leetcode_in_python
  @Description  : 设计一个支持以下两种操作的数据结构：
    void addWord(word)
    bool search(word)
    search(word) 可以搜索文字或正则表达式字符串，字符串只包含字母 . 或 a-z 。 . 可以表示任何一个字母。
    示例:
    addWord("bad")
    addWord("dad")
    addWord("mad")
    search("pad") -> false
    search("bad") -> true
    search(".ad") -> true
    search("b..") -> true
    说明:
    你可以假设所有单词都是由小写字母 a-z 组成的。
 """


# 404ms, 23.6MB
class WordDictionary:
    def __init__(self):
        self.d = {}  # 字典树

    def addWord(self, word: str) -> None:
        t = self.d  # 单词填进字典树
        for c in word:
            if c not in t:
                t[c] = {}
            t = t[c]
        t['end'] = True

    def search(self, word: str) -> bool:
        cut = False

        def f(td, s):  # 深搜，参数为：当前子字典，当前串
            nonlocal cut
            if cut:  # 剪枝
                return True
            t = td
            for i, c in enumerate(s):
                if c == '.':
                    return any(f(t[j], s[i + 1:]) for j in t if j != 'end')  # 深搜扩展
                if c not in t:
                    return False
                t = t[c]
            cut = 'end' in t
            return cut

        return f(self.d, word)