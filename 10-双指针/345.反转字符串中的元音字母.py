"""
  @Author       : Liujianhan
  @Date         : 20/4/4 20:42
  @FileName     : 345.反转字符串中的元音字母.py
  @ProjectName  : leetcode_in_python
  @Description  : 编写一个函数，以字符串作为输入，反转该字符串中的元音字母。
    输入: "hello"
    输出: "holle"

    输入: "leetcode"
    输出: "leotcede"
 """


class Solution:
    # 60ms, 14.7MB
    @classmethod
    def reverse_vowels(cls, s: str) -> str:
        """<双指针>"""
        vowels = 'aeiouAEIOU'
        new_s = list(s)
        left, right = 0, len(s) - 1
        while left < right:
            if s[left] not in vowels:
                left += 1
                continue
            if s[right] not in vowels:
                right -= 1
                continue
            new_s[left], new_s[right] = new_s[right], new_s[left]
            left += 1
            right -= 1

        return ''.join(new_s)


if __name__ == '__main__':
    test_cases = ['aA', 'hello', 'leetcode']
    for tc in test_cases:
        print(tc, Solution.reverse_vowels(tc))
