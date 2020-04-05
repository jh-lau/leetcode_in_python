"""
  @Author       : Liujianhan
  @Date         : 20/4/5 15:06
  @FileName     : 541.反转字符串 II.py
  @ProjectName  : leetcode_in_python
  @Description  : 给定一个字符串和一个整数 k，你需要对从字符串开头算起的每个 2k 个字符的前k个字符进行反转。如果剩余少于 k 个字符，则将剩余的所有全部反转。如果有小于 2k 但大于或等于 k 个字符，则反转前 k 个字符，并将剩余的字符保持原样。
    输入: s = "abcdefg", k = 2
    输出: "bacdfeg"

    要求:
    该字符串只包含小写的英文字母。
    给定字符串的长度和 k 在[1, 10000]范围内。
 """


class Solution:
    # 40ms, 13.6MB
    @classmethod
    def reverse_str(cls, s: str, k: int) -> str:
        new_s = list(s)
        for i in range(0, len(s), 2*k):
            new_s[i: i+k] = new_s[i: i+k][::-1]

        return ''.join(new_s)


if __name__ == '__main__':
    test_cases = [('abcdefg', 2)]
    for tc in test_cases:
        print(tc, Solution.reverse_str(*tc))
