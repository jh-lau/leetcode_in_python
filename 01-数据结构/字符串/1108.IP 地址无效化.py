"""
  @Author       : liujianhan
  @Date         : 20/12/20 1:54
  @Project      : leetcode_in_python
  @FileName     : 1108.IP 地址无效化.py
  @Description  : 给你一个有效的 IPv4 地址 address，返回这个 IP 地址的无效化版本。
    所谓无效化 IP 地址，其实就是用 "[.]" 代替了每个 "."。

    示例 1：
    输入：address = "1.1.1.1"
    输出："1[.]1[.]1[.]1"

    示例 2：
    输入：address = "255.100.50.0"
    输出："255[.]100[.]50[.]0"

    提示：
    给出的 address 是一个有效的 IPv4 地址
"""


class Solution:
    # 36ms, 14.8MB
    @staticmethod
    def defang_ip_addr(address: str) -> str:
        address = address.replace('.', '[.]')

        return address


if __name__ == '__main__':
    test_cases = [
        "1.1.1.1", "255.100.50.0"
    ]
    for tc in test_cases:
        print(Solution.defang_ip_addr(tc))
