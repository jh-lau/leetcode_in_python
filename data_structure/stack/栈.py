"""
  Created by PyCharm.
  User: Liujianhan
  Date: 2019/5/31
  Time: 9:44
 """
__author__ = 'liujianhan'


class Stack:
    # 列表最后元素作为栈顶元素
    def __init__(self):
        self.items = []

    def push(self, elem):
        self.items.append(elem)

    def pop(self):
        return self.items.pop()

    def top(self):
        return self.items[-1]

    def is_empty(self):
        return 0 == len(self.items)

    def size(self):
        return len(self.items)


def parentheses_check(checking_string):
    stack = Stack()

    for checking_char in checking_string:
        if checking_char == '(':
            stack.push(checking_char)
        else:
            if stack.is_empty():
                return False
            else:
                stack.pop()

    return True if stack.is_empty() else False


def multi_parentheses_check(checking_string, left_list, right_list):
    stack = Stack()

    for checking_char in checking_string:
        if checking_char in left_list:
            stack.push(checking_char)
        else:
            if stack.is_empty():
                return False
            else:
                need_match = stack.pop()
                if left_list.index(need_match) != right_list.index(checking_char):
                    return False

    return True if stack.is_empty() else False


def main_1():
    string_list = ['(()()()())', '(((())))', '(()((())()))', '((((((())', '()))', '(()()(()']
    for checking_string in string_list:
        print(f"{parentheses_check(checking_string)} ----- {checking_string}")
        print('*****************')


def main():
    left_list = ['(', '[', '{']
    right_list = [')', ']', '}']
    string_list = ['{{([][])}()}','[[{{(())}}]]','[][][](){}','([)]','((()]))','[{()]']
    for checking_string in string_list:
        print(f"{multi_parentheses_check(checking_string, left_list, right_list)} ---- {checking_string}")
        print('***********')


if __name__ == '__main__':
    main()
