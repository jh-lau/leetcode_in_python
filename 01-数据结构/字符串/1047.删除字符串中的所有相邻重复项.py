"""
  @Author       : liujianhan
  @Date         : 2020/12/9 10:01
  @Project      : leetcode_in_python
  @FileName     : 1047.删除字符串中的所有相邻重复项.py
  @Description  : 输入："abbaca"
    输出："ca"
    解释：
    例如，在 "abbaca" 中，我们可以删除 "bb" 由于两字母相邻且相同，这是此时唯一可以执行删除操作的重复项。之后我们得到字符串 "aaca"，
    其中又只有 "aa" 可以执行重复项删除操作，所以最后的字符串为 "ca"。
    提示：

    1 <= S.length <= 20000
    S 仅由小写英文字母组成。
"""


class Solution:
    # 3144ms, 13.9MB
    def remove_duplicates(self, S: str) -> str:
        size = len(S)
        if size < 2:
            return S
        i = 0
        res = []
        while i < size - 1:
            if S[i] == S[i + 1]:
                res.extend([i, i + 1])
                i += 2
            else:
                i += 1
        new_s = ''.join([char for i, char in enumerate(S) if i not in res])
        return new_s if new_s == S else self.remove_duplicates(new_s)

    # 60ms, 13.9MB
    @staticmethod
    def remove_duplicates_v2(S: str) -> str:
        stack = []
        for char in S:
            if stack and stack[-1] == char:
                stack.pop()
            else:
                stack.append(char)

        return ''.join(stack)


if __name__ == '__main__':
    test_cases = [
        'abbaca', 'abbacaac', "aaaaaaaaa"
    ]
    for tc in test_cases:
        print(Solution().remove_duplicates(tc))
        print(Solution.remove_duplicates_v2(tc))
