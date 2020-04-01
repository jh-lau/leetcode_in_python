"""
  User: Liujianhan
 """
__author__ = 'liujianhan'


class Solution:
    @staticmethod
    def plus_one(digits):
        return list(str(int(''.join([str(d) for d in digits])) + 1))


test = [1,2,3]
print(Solution().plus_one(test))
