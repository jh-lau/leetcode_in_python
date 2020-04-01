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
        """
        从尾往前匹配
        :param strs:
        :return:
        """
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
            # todo:可优化，否则需要等到temp减小到0才退出
            temp -= 1
        return shortest_string if shortest_string else ''

    # 使用api
    @staticmethod
    def longest_common_prefix_api(strs):
        result = ''
        for temp in zip(*strs):
            if len(set(temp)) != 1:
                break
            result += temp[0]
        return result


if __name__ == '__main__':
    t = Solution()
    assert t.longest_common_prefix([]) == ''
    assert t.longest_common_prefix([""]) == ''
    assert t.longest_common_prefix(['a']) == 'a'
    assert t.longest_common_prefix(['a', 'b']) == ''
    assert t.longest_common_prefix(['a', 'a']) == 'a'
    assert t.longest_common_prefix_api([]) == ''
    assert t.longest_common_prefix_api([""]) == ''
    assert t.longest_common_prefix_api(['a']) == 'a'
    assert t.longest_common_prefix_api(['a', 'b']) == ''
    assert t.longest_common_prefix_api(['a', 'a']) == 'a'
    print('test pass')
