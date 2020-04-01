"""
  User: Liujianhan
 """
__author__ = 'liujianhan'


class Solution:
    @staticmethod
    def generate(num_rows):
        result = []
        for i in range(num_rows):
            result.append([1] * (i + 1))
            if i > 1:
                for j, num in enumerate(result[i - 1][:-1]):
                    result[i][j + 1] = num + result[i - 1][j + 1]
        return result


if __name__ == '__main__':
    print(Solution().generate(4))