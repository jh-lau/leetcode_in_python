"""
  @Author       : Liujianhan
  @Date         : 20/3/22 14:34
  @FileName     : 119.杨辉三角II.py
  @ProjectName  : leetcode_in_python
  @Description  : 给定一个非负索引 k，其中 k ≤ 33，返回杨辉三角的第 k 行。
  输入: 3
    输出: [1,3,3,1]
 """


class Solution:
    # 60ms, 13.6MB
    @classmethod
    def generate(cls, num_rows):
        result = []
        for i in range(num_rows+1):
            result.append([1] * (i + 1))
            if i > 1:
                for j, num in enumerate(result[i - 1][:-1]):
                    result[i][j + 1] = num + result[i - 1][j + 1]
        return result[-1]

    # 28ms, 13.5MB
    @classmethod
    def get_row(cls, row_index):
        result = [1]
        for i in range(1, row_index+1):
            result.insert(0, 0)
            for j in range(i):
                result[j] += result[j+1]

        return result


if __name__ == '__main__':
    print(Solution.generate(3))
    print(Solution.get_row(3))