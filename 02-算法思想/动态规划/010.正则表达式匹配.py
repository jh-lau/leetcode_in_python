"""
  User: Liujianhan
  Time: 15:51
 """
__author__ = 'liujianhan'


class Solution:
    @staticmethod
    def is_match(s: str, p: str) -> bool:
        mem = {}

        def _is_match(i, j):
            if (i, j) not in mem:
                if j == len(p):
                    result = i == len(s)
                else:
                    first_match = i < len(s) and p[j] in (s[i], '.')
                    if j + 1 < len(p) and p[j + 1] == '*':
                        result = _is_match(i, j + 2) or (first_match and _is_match(i + 1, j))
                    else:
                        result = first_match and _is_match(i + 1, j + 1)
                mem[i, j] = result
            return mem[i, j]

        return _is_match(0, 0)
