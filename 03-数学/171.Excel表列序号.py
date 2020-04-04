"""
  @Author       : Liujianhan
  @Date         : 20/4/4 15:02
  @FileName     : 171.Excel表列序号.py
  @ProjectName  : leetcode_in_python
  @Description  : 给定一个Excel表格中的列名称，返回其相应的列序号。
  168题的逆过程。
 """


class Solution:
    # 48ms, 13.7MB
    @classmethod
    def title_to_number(cls, s: str) -> int:
        table = [chr(k) for k in range(65, 91)]
        while len(s) > 1:
            return cls.title_to_number(s[:-1]) * 26 + table.index(s[-1]) + 1

        return table.index(s) + 1


if __name__ == '__main__':
    test_cases = ['A', 'B', 'Z', 'AB', 'ZY', 'AAA']
    for tc in test_cases:
        print(tc, Solution.title_to_number(tc))



