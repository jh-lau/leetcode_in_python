"""
  @Author       : liujianhan
  @Date         : 20/12/27 16:15
  @Project      : leetcode_in_python
  @FileName     : 1154.一年中的第几天.py
  @Description  : 给你一个按 YYYY-MM-DD 格式表示日期的字符串 date，请你计算并返回该日期是当年的第几天。
    通常情况下，我们认为 1 月 1 日是每年的第 1 天，1 月 2 日是每年的第 2 天，依此类推。每个月的天数与现行公元纪年法（格里高利历）一致。

    示例 1：
    输入：date = "2019-01-09"
    输出：9

    示例 2：
    输入：date = "2019-02-10"
    输出：41

    示例 3：
    输入：date = "2003-03-01"
    输出：60

    示例 4：
    输入：date = "2004-03-01"
    输出：61
     
    提示：

    date.length == 10
    date[4] == date[7] == '-'，其他的 date[i] 都是数字。
    date 表示的范围从 1900 年 1 月 1 日至 2019 年 12 月 31 日。
"""


class Solution:
    # 32ms, 14.9MB
    @staticmethod
    def day_of_year(date: str) -> int:
        y, m, d = map(int, date.split('-'))
        a = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if y != 1900 and y % 4 == 0:
            a[2] += 1
        return sum(a[: m]) + d


if __name__ == '__main__':
    test_cases = [
        "2019-01-09",
        "2019-02-10",
        "2003-03-01",
        "2004-03-01"
    ]
    for tc in test_cases:
        print(Solution.day_of_year(tc))
