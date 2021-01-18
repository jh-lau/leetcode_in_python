"""
  @Author       : liujianhan
  @Date         : 2021/1/18 13:58
  @Project      : leetcode_in_python
  @FileName     : 721.账户合并(M).py
  @Description  : 给定一个列表 accounts，每个元素 accounts[i] 是一个字符串列表，其中第一个元素 accounts[i][0] 是 名称 (name)，
    其余元素是 emails 表示该账户的邮箱地址。
    现在，我们想合并这些账户。如果两个账户都有一些共同的邮箱地址，则两个账户必定属于同一个人。请注意，即使两个账户具有相同的名称，
    它们也可能属于不同的人，因为人们可能具有相同的名称。一个人最初可以拥有任意数量的账户，但其所有账户都具有相同的名称。
    合并账户后，按以下格式返回账户：每个账户的第一个元素是名称，其余元素是按顺序排列的邮箱地址。账户本身可以以任意顺序返回。

    示例 1：
    输入：
    accounts = [["John", "johnsmith@mail.com", "john00@mail.com"], ["John", "johnnybravo@mail.com"], ["John",
    "johnsmith@mail.com", "john_newyork@mail.com"], ["Mary", "mary@mail.com"]]
    输出：
    [["John", 'john00@mail.com', 'john_newyork@mail.com', 'johnsmith@mail.com'],  ["John", "johnnybravo@mail.com"],
    ["Mary", "mary@mail.com"]]
    解释：
    第一个和第三个 John 是同一个人，因为他们有共同的邮箱地址 "johnsmith@mail.com"。
    第二个 John 和 Mary 是不同的人，因为他们的邮箱地址没有被其他帐户使用。
    可以以任何顺序返回这些列表，例如答案 [['Mary'，'mary@mail.com']，['John'，'johnnybravo@mail.com']，
    ['John'，'john00@mail.com'，'john_newyork@mail.com'，'johnsmith@mail.com']] 也是正确的。

    提示：

    accounts的长度将在[1，1000]的范围内。
    accounts[i]的长度将在[1，10]的范围内。
    accounts[i][j]的长度将在[1，30]的范围内。
"""
import collections
from typing import List


class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))

    def union(self, index1: int, index2: int):
        self.parent[self.find(index2)] = self.find(index1)

    def find(self, index: int) -> int:
        if self.parent[index] != index:
            self.parent[index] = self.find(self.parent[index])
        return self.parent[index]


class Solution:
    # 228ms, 18.8MB
    @staticmethod
    def accounts_merge(accounts: List[List[str]]) -> List[List[str]]:
        emailToIndex = dict()
        emailToName = dict()

        for account in accounts:
            name = account[0]
            for email in account[1:]:
                if email not in emailToIndex:
                    emailToIndex[email] = len(emailToIndex)
                    emailToName[email] = name

        uf = UnionFind(len(emailToIndex))
        for account in accounts:
            firstIndex = emailToIndex[account[1]]
            for email in account[2:]:
                uf.union(firstIndex, emailToIndex[email])

        indexToEmails = collections.defaultdict(list)
        for email, index in emailToIndex.items():
            index = uf.find(index)
            indexToEmails[index].append(email)

        ans = list()
        for emails in indexToEmails.values():
            ans.append([emailToName[emails[0]]] + sorted(emails))
        return ans


if __name__ == '__main__':
    test_cases = [
        [["John", "johnsmith@mail.com", "john00@mail.com"], ["John", "johnnybravo@mail.com"], ["John",
                                                                                               "johnsmith@mail.com",
                                                                                               "john_newyork@mail.com"],
         ["Mary", "mary@mail.com"]]
    ]
    for tc in test_cases:
        print(Solution.accounts_merge(tc))
