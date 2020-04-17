"""
  @Author       : liujianhan
  @Date         : 2020/4/17 上午10:46
  @Project      : leetcode_in_python
  @FileName     : 937.重新排列日志文件.py
  @Description  : 你有一个日志数组 logs。每条日志都是以空格分隔的字串。
    对于每条日志，其第一个字为字母数字标识符。然后，要么：
    标识符后面的每个字将仅由小写字母组成，或；
    标识符后面的每个字将仅由数字组成。
    我们将这两种日志分别称为字母日志和数字日志。保证每个日志在其标识符后面至少有一个字。
    将日志重新排序，使得所有字母日志都排在数字日志之前。字母日志按内容字母顺序排序，忽略标识符；在内容相同时，按标识符排序。
    数字日志应该按原来的顺序排列。
    返回日志的最终顺序。
    示例 ：

    输入：["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo"]
    输出：["g1 act car","a8 act zoo","ab1 off key dog","a1 9 2 3 1","zo4 4 7"]
"""


class Solution:
    # 44ms, 13.7MB
    @classmethod
    def recorder_log_files(cls, logs):
        def f(log):
            id_, rest = log.split(' ', 1)
            # 字母日志，内容，标识符；逐一比对
            return (0, rest, id_) if rest[0].isalpha() else (1,)

        return sorted(logs, key=f)


if __name__ == '__main__':
    print(Solution.recorder_log_files(["a1 9 2 3 1", "g1 act car", "zo4 4 7", "ab1 off key dog", "a8 act zoo"]))
