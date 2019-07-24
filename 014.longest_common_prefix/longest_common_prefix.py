"""
  User: Liujianhan
  Time: 15:01
 """
__author__ = 'liujianhan'


class Solution:
    @staticmethod
    def get_shortest_string(strs):
        if len(strs) == 1:
            return strs[0]
        temp = ''
        for i, _ in enumerate(strs):
            if len(strs[i]) <= len(strs[i - 1]):
                temp = strs[i]
        return temp

    def longest_common_prefix(self, strs) -> str:
        if not strs:
            return ''
        shortest_string = self.get_shortest_string(strs)
        length = len(shortest_string)
        strs.pop(strs.index(shortest_string))
        temp = length
        while shortest_string and temp:

            for string in strs:
                if string[:length] == shortest_string:
                    continue
                else:
                    shortest_string = shortest_string[:-1]
                    length -= 1
            #todo:可优化，否则需要等到temp减小到0才退出
            temp -= 1
        return shortest_string if shortest_string else ''