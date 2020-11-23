"""
  @Author       : liujianhan
  @Date         : 20/11/22 3:24
  @Project      : leetcode_in_python
  @FileName     : 796.旋转字符串.py
  @Description  : 给定两个字符串, A 和 B。
    A 的旋转操作就是将 A 最左边的字符移动到最右边。 
    例如, 若 A = 'abcde'，在移动一次之后结果就是'bcdea' 。
    如果在若干次旋转操作之后，A 能变成B，那么返回True。
    示例 1:
    输入: A = 'abcde', B = 'cdeab'
    输出: true
    示例 2:
    输入: A = 'abcde', B = 'abced'
    输出: false
    注意：
    A 和 B 长度不超过 100。
"""


class Solution:
    # 32ms, 13.5MB
    @staticmethod
    def rotate_string(A: str, B: str) -> bool:
        if not A and not B:
            return True
        for i, char in enumerate(A):
            if char == B[0]:
                new_string = A[i:] + A[:i]
                if B == new_string:
                    return True

        return False

    # 44ms, 13.2MB
    @staticmethod
    def rotate_string_v2(A: str, B: str) -> bool:
        if len(A) != len(B):
            return False
        if B in A+A:
            return True
        return False


if __name__ == '__main__':
    test_cases = [
        ('abcde', 'cdeab'),
        ('abcde', 'abced'),
        ('', '')
    ]
    for tc in test_cases:
        print(Solution.rotate_string(*tc))
