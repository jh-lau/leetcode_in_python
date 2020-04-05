"""
  @Author       : Liujianhan
  @Date         : 20/4/5 17:14
  @FileName     : 551.学生出勤记录 I.py
  @ProjectName  : leetcode_in_python
  @Description  : 给定一个字符串来代表一个学生的出勤记录，这个记录仅包含以下三个字符：
    'A' : Absent，缺勤
    'L' : Late，迟到
    'P' : Present，到场
    如果一个学生的出勤记录中不超过一个'A'(缺勤)并且不超过两个连续的'L'(迟到),那么这个学生会被奖赏。
    你需要根据这个学生的出勤记录判断他是否会被奖赏。

    输入: "PPALLP"
    输出: True
    输入: "PPALLL"
    输出: False
 """


class Solution:
    # 40ms, 13.7MB
    @classmethod
    def check_record(cls, s: str) -> bool:
        if s.count("A") > 1:
            return False
        cnt = n = 0
        while n < len(s):
            if s[n] == 'L':
                cnt += 1
                n += 1
                if cnt > 2:
                    return False
            else:
                cnt = 0
                n += 1
        return True

    # 32ms, 13.7MB
    @classmethod
    def check_record_v2(cls, s: str) -> bool:
        return s.count('A') < 2 and s.count('LLL') < 1


if __name__ == '__main__':
    test_cases = ['PPALLP', 'PPALLL']
    for tc in test_cases:
        print(tc, Solution.check_record(tc))
        print(tc, Solution.check_record_v2(tc))
