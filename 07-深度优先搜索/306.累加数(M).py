"""
  @Author       : Liujianhan
  @Date         : 20/7/26 0:47
  @FileName     : 306.累加数(M).py
  @ProjectName  : leetcode_in_python
  @Description  : 累加数是一个字符串，组成它的数字可以形成累加序列。
    一个有效的累加序列必须至少包含 3 个数。除了最开始的两个数以外，字符串中的其他数都等于它之前两个数相加的和。
    给定一个只包含数字 '0'-'9' 的字符串，编写一个算法来判断给定输入是否是累加数。
    说明: 累加序列里的数不会以 0 开头，所以不会出现 1, 2, 03 或者 1, 02, 3 的情况。
    示例 1:
    输入: "112358"
    输出: true
    解释: 累加序列为: 1, 1, 2, 3, 5, 8 。1 + 1 = 2, 1 + 2 = 3, 2 + 3 = 5, 3 + 5 = 8
    示例 2:

    输入: "199100199"
    输出: true
    解释: 累加序列为: 1, 99, 100, 199。1 + 99 = 100, 99 + 100 = 199
    进阶:
    你如何处理一个溢出的过大的整数输入?
 """


class Solution:
    # 48ms, 13.6MB
    @staticmethod
    def is_additive_number(num: str) -> bool:
        if len(num) < 3:
            return False
        result = []

        def dfs(begin, path, left_num):
            if len(path) > 2 and left_num == 0:
                result.append(path)
                return
            for i in range(begin + 1, len(num) + 1):
                if i > begin + 1 and num[begin] == '0':
                    return
                if len(path) < 2:
                    dfs(i, path + [int(num[begin:i])], len(num) - i)
                else:
                    if int(num[begin:i]) == path[-1] + path[-2]:
                        dfs(i, path + [int(num[begin:i])], len(num) - i)

        dfs(0, [], len(num))

        return bool(result)


if __name__ == '__main__':
    test_cases = [
        '112358', '199100199'
    ]
    for tc in test_cases:
        print(Solution.is_additive_number(tc))
