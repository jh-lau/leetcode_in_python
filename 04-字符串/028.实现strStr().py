"""
  @Author       : liujianhan
  @Date         : 2020/1/23 下午2:59
  @Project      : leetcode_in_python
  @FileName     : 028.实现strStr().py
  @Description  : 给定一个 haystack 字符串和一个 needle 字符串，在 haystack 字符串中找出 needle 字符串出现的第一个位置 (从0开始)。
  如果不存在，则返回  -1。
"""


class Solution:
    @staticmethod
    def str_str(haystack: str, needle: str) -> int:
        if not needle:
            return 0
        return haystack.index(needle) if needle in haystack else -1


if __name__ == '__main__':
    a, b = 'hello', 'll'
    c, d = 'aaaaa', 'bba'
    print(Solution().str_str(a, b))
    print(Solution().str_str(c, d))
