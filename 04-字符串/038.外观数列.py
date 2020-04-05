"""
  @Author       : liujianhan
  @Date         : 2020/3/18 上午10:05
  @Project      : leetcode_in_python
  @FileName     : 38.外观数列.py
  @Description  : 「外观数列」是一个整数序列，从数字 1 开始，序列中的每一项都是对前一项的描述。前五项如下：
    1.     1
    2.     11；上一项为1个1
    3.     21；上一项为2个1
    4.     1211；上一项为1个2,1个1
    5.     111221；上一项为1个1,1个2,2个1
  解法：要求第n个s字符串只需分析第n-1个字符串：
    创建一个栈（用其他结构可能更好）
    遍历字符串：
    1.当字符与栈内字符相同或者栈为空时入栈
    2.当字符与栈内字符不相同时，取栈的长度+栈内字符，清空栈并将新的元素入栈
    （注意：最后栈不为空所以在循环结束后需要在进行一次取栈的长度+栈内字符的操作）
"""


class Solution:
    @classmethod
    def count_and_say(cls, n: int) -> str:
        num = ['', '1']
        if n == 1:
            return num[1]
        for i in range(2, n + 1):
            p = []
            s = ''
            for x in num[i - 1]:
                if p == [] or x == p[0]:
                    p.append(x)
                else:
                    s += str(len(p))
                    s += p[0]
                    p = []
                    p.append(x)
            s += str(len(p))
            s += p[0]
            num.append(s)

        return num[n]


if __name__ == '__main__':
    for s in range(1, 6):
        print(Solution.count_and_say(s))
