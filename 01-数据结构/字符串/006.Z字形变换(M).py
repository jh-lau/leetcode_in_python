"""
  @Author       : Liujianhan
  @Date         : 20/4/29 22:37
  @FileName     : 006.Z字形变换(M).py
  @ProjectName  : leetcode_in_python
  @Description  : 将一个给定字符串根据给定的行数，以从上往下、从左到右进行 Z 字形排列。
    比如输入字符串为 "LEETCODEISHIRING" 行数为 3 时，排列如下：
    L   C   I   R
    E T O E S I I G
    E   D   H   N
    之后，你的输出需要从左往右逐行读取，产生出一个新的字符串，比如："LCIRETOESIIGEDHN"。
    请你实现这个将字符串进行指定行数变换的函数：
    string convert(string s, int numRows);
    示例 1:
    输入: s = "LEETCODEISHIRING", numRows = 3
    输出: "LCIRETOESIIGEDHN"
    示例 2:
    输入: s = "LEETCODEISHIRING", numRows = 4
    输出: "LDREOEIIECIHNTSG"
    解释:
    L     D     R
    E   O E   I I
    E C   I H   N
    T     S     G
 """


class Solution:
    # 80ms, 13.4MB
    @classmethod
    def convert(cls, s: str, num_rows: int) -> str:
        if num_rows < 2:
            return s
        res = ["" for _ in range(num_rows)]
        i, flag = 0, -1
        for c in s:
            res[i] += c
            if i == 0 or i == num_rows - 1:
                flag = -flag
            i += flag
        return "".join(res)


if __name__ == '__main__':
    test_cases = [
        ('LEETCODEISHIRING', 3), ('LEETCODEISHIRING', 4)
    ]
    for tc in test_cases:
        print(Solution.convert(*tc))

