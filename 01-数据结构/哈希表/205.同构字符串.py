"""
  @Author       : Liujianhan
  @Date         : 20/6/6 22:58
  @FileName     : 205.同构字符串.py
  @ProjectName  : leetcode_in_python
  @Description  : 给定两个字符串 s 和 t，判断它们是否是同构的。
    如果 s 中的字符可以被替换得到 t ，那么这两个字符串是同构的。
    所有出现的字符都必须用另一个字符替换，同时保留字符的顺序。两个字符不能映射到同一个字符上，但字符可以映射自己本身。
    示例 1:
    输入: s = "egg", t = "add"
    输出: true
    示例 2:
    输入: s = "foo", t = "bar"
    输出: false
    示例 3:
    输入: s = "paper", t = "title"
    输出: true
    说明:
    你可以假设 s 和 t 具有相同的长度。
 """


class Solution:
    # 44ms, 13.7MB
    @classmethod
    def is_isomorphic(cls, s: str, t: str) -> bool:
        if not s:
            return True
        dic = {}
        for i in range(len(s)):
            if s[i] not in dic:
                if t[i] in dic.values():
                    return False
                else:
                    dic[s[i]] = t[i]
            else:
                if dic[s[i]] != t[i]:
                    return False
        return True


if __name__ == '__main__':
    test_cases = [
        ('egg', 'add'),
        ('foo', 'bar'),
        ('paper', 'title')
    ]
    for tc in test_cases:
        print(Solution.is_isomorphic(*tc))
