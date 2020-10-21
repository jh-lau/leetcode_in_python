"""
  @Author       : Liujianhan
  @Date         : 20/4/11 23:13
  @FileName     : 925.长按键入.py
  @ProjectName  : leetcode_in_python
  @Description  : 你的朋友正在使用键盘输入他的名字 name。偶尔，在键入字符 c 时，按键可能会被长按，而字符可能被输入 1 次或多次。
    你将会检查键盘输入的字符 typed。如果它对应的可能是你的朋友的名字（其中一些字符可能被长按），那么就返回 True。
    示例 1：

    输入：name = "alex", typed = "aaleex"
    输出：true
    解释：'alex' 中的 'a' 和 'e' 被长按。
    示例 2：

    输入：name = "saeed", typed = "ssaaedd"
    输出：false
    解释：'e' 一定需要被键入两次，但在 typed 的输出中不是这样。
    示例 3：

    输入：name = "leelee", typed = "lleeelee"
    输出：true
    示例 4：

    输入：name = "laiden", typed = "laiden"
    输出：true
    解释：长按名字中的字符并不是必要的。
     

    提示：

    name.length <= 1000
    typed.length <= 1000
    name 和 typed 的字符都是小写字母。
 """


class Solution:
    # 52ms, 13.6MB
    @classmethod
    def is_long_press_name(cls, name: str, typed: str) -> bool:
        i = 0
        j = 0
        while j < len(typed):
            if i < len(name) and name[i] == typed[j]:
                i += 1
                j += 1
            elif j > 0 and typed[j] == name[i - 1]:  # 这里也可以用  “i > 0” 或者 官方的 "typed[j] == typed[j - 1]"
                j += 1
            else:
                return False
        return i == len(name)


if __name__ == '__main__':
    test_cases = [('alex', 'aaleex'), ('saeed', 'ssaaedd'), ('leelee', 'lleelee'), ('laiden', 'laiden'),
                  ("alex", "aaleelx")]
    for tc in test_cases:
        print(tc, Solution.is_long_press_name(*tc))
