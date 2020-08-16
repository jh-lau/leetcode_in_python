"""
  User: Liujianhan
  Time: 15:51
 """


class Solution:
    @staticmethod
    def is_valid(s):
        stack = []
        match = {'{': '}', '(': ')', '[': ']'}
        for i in s:
            if i in '({[':
                stack.append(i)
            else:
                if not stack:
                    return False
                top = stack.pop()
                if match[top] != i:
                    return False
        return len(stack) == 0
