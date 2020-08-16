"""
  @Author       : Liujianhan
  @Date         : 20/4/5 12:47
  @FileName     : 459.重复的子字符串.py
  @ProjectName  : leetcode_in_python
  @Description  : 给定一个非空的字符串，判断它是否可以由它的一个子串重复多次构成。给定的字符串只含有小写英文字母，并且长度不超过10000。

  输入: "abab"
    输出: True
    解释: 可由子字符串 "ab" 重复两次构成。
    输入: "aba"
    输出: False
    输入: "abcabcabcabc"
    输出: True
    解释: 可由子字符串 "abc" 重复四次构成。 (或者子字符串 "abcabc" 重复两次构成。)
 """


class Solution:
    # 40ms, 13.7MB
    @classmethod
    def repeated_substring_pattern(cls, s: str) -> bool:
        """如果字符串含有重复子字符串，那么该字符串多次向右移位后，将会变成原字符串，如：
        abcabc -> bcabca -> cabcab -> abcabc，因此循环移位k个字符，直到len(s)-1
        不过这样会超时。因此创建一个新字符串new_s = s + s， 则s在移位中所有的情况都将出现在
        new_s中，只要判断是否包含即可"""
        new_s = s + s
        return s in new_s[1:len(new_s) - 1]


if __name__ == '__main__':
    test_cases = ['abab', 'aba', 'abcabcabcabc']
    for tc in test_cases:
        print(tc, Solution.repeated_substring_pattern(tc))
