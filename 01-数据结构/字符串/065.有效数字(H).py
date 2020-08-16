"""
  @Author       : Liujianhan
  @Date         : 20/5/2 13:49
  @FileName     : 065.有效数字(H).py
  @ProjectName  : leetcode_in_python
  @Description  : 验证给定的字符串是否可以解释为十进制数字。
    例如:
    "0" => true
    " 0.1 " => true
    "abc" => false
    "1 a" => false
    "2e10" => true
    " -90e3   " => true
    " 1e" => false
    "e3" => false
    " 6e-1" => true
    " 99e2.5 " => false
    "53.5e93" => true
    " --6 " => false
    "-+3" => false
    "95a54e53" => false
    说明: 我们有意将问题陈述地比较模糊。在实现代码之前，你应当事先思考所有可能的情况。这里给出一份可能存在于有效十进制数字中的字符列表：
    数字 0-9
    指数 - "e"
    正/负号 - "+"/"-"
    小数点 - "."
    当然，在输入中，这些字符的上下文也很重要。
 """


class Solution:
    # 32ms, 13.7MB
    @classmethod
    def is_number(cls, s: str) -> bool:
        s = s.strip()
        have_dot = have_e = have_num = False
        for index, char in enumerate(s):
            if char.isdigit():
                have_num = True
            elif char == '.':
                if have_e or have_dot:
                    return False
                have_dot = True
            elif char == 'e':
                if have_e or not have_num:
                    return False
                have_num = False
                have_e = True
            elif char in '+-':
                if index > 0 and s[index-1] != 'e':
                    return False
            else:
                return False

        return have_num

    # 44ms, 13.8MB
    @classmethod
    def is_number_v2(cls, s: str) -> bool:
        """有限自动机"""
        state = [
            {},
            # 状态1,初始状态(扫描通过的空格)
            {"blank": 1, "sign": 2, "digit": 3, ".": 4},
            # 状态2,发现符号位(后面跟数字或者小数点)
            {"digit": 3, ".": 4},
            # 状态3,数字(一直循环到非数字)
            {"digit": 3, ".": 5, "e": 6, "blank": 9},
            # 状态4,小数点(后面只有紧接数字)
            {"digit": 5},
            # 状态5,小数点之后(后面只能为数字,e,或者以空格结束)
            {"digit": 5, "e": 6, "blank": 9},
            # 状态6,发现e(后面只能符号位, 和数字)
            {"sign": 7, "digit": 8},
            # 状态7,e之后(只能为数字)
            {"digit": 8},
            # 状态8,e之后的数字后面(只能为数字或者以空格结束)
            {"digit": 8, "blank": 9},
            # 状态9, 终止状态 (如果发现非空,就失败)
            {"blank": 9}
        ]
        cur_state = 1
        for c in s:
            if c.isdigit():
                c = "digit"
            elif c in " ":
                c = "blank"
            elif c in "+-":
                c = "sign"
            if c not in state[cur_state]:
                return False
            cur_state = state[cur_state][c]
        if cur_state not in [3, 5, 8, 9]:
            return False
        return True


if __name__ == '__main__':
    test_cases = [
        "0",
        " 0.1 ",
        "abc",
        "1 a",
        "2e10",
        " -90e3   ",
        " 1e",
        "e3",
        " 6e-1",
        " 99e2.5 ",
        "53.5e93",
        " --6 ",
        "-+3",
        "95a54e53"
    ]
    for tc in test_cases:
        print(tc, Solution.is_number(tc))
        print(tc, Solution.is_number_v2(tc))