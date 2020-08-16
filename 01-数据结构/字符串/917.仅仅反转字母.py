"""
  @Author       : liujianhan
  @Date         : 2020/4/10 上午9:47
  @Project      : leetcode_in_python
  @FileName     : 917.仅仅反转字母.py
  @Description  : 给定一个字符串 S，返回 “反转后的” 字符串，其中不是字母的字符都保留在原地，而所有字母的位置发生反转。
    示例 1：

    输入："ab-cd"
    输出："dc-ba"
    示例 2：

    输入："a-bC-dEf-ghIj"
    输出："j-Ih-gfE-dCba"
    示例 3：

    输入："Test1ng-Leet=code-Q!"
    输出："Qedo1ct-eeLg=ntse-T!"

    提示：

    S.length <= 100
    33 <= S[i].ASCIIcode <= 122 
    S 中不包含 \ or "
"""


class Solution:
    # 40ms, 13.7MB
    @classmethod
    def reverse_only_letters(cls, s: str) -> str:
        letters = [c for c in s if c.isalpha()]
        ans = []
        for c in s:
            if c.isalpha():
                ans.append(letters.pop())
            else:
                ans.append(c)
        return "".join(ans)


if __name__ == '__main__':
    test_cases = ['ab-cd', 'a-bC-dEf-ghIj', "Test1ng-Leet=code-Q!"]
    for tc in test_cases:
        print(Solution.reverse_only_letters(tc))
