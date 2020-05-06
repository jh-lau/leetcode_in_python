"""
  @Author       : Liujianhan
  @Date         : 20/5/6 22:24
  @FileName     : 093.复原IP地址(M).py
  @ProjectName  : leetcode_in_python
  @Description  : 给定一个只包含数字的字符串，复原它并返回所有可能的 IP 地址格式。
    示例:
    输入: "25525511135"
    输出: ["255.255.11.135", "255.255.111.35"]
 """
from typing import List


class Solution:
    # 52ms, 13.8MB
    @classmethod
    def restore_ip_addresses(cls, s: str) -> List[str]:
        res = []
        n = len(s)

        def backtrack(i, tmp, flag):
            if i == n and not flag:
                res.append(tmp[:-1])
                return
            if flag < 0:
                return
            for j in range(i, i + 3):
                if j < n:
                    if i == j and s[j] == '0':
                        backtrack(j + 1, tmp + s[j] + '.', flag - 1)
                        break
                    if 0 < int(s[i:j + 1]) <= 255:
                        backtrack(j + 1, tmp + s[i:j + 1] + '.', flag - 1)

        backtrack(0, '', 4)

        return res


if __name__ == '__main__':
    print(Solution.restore_ip_addresses('25525511135'))
