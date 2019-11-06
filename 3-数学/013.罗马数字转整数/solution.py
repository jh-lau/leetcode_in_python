"""
  User: Liujianhan
 """
__author__ = 'liujianhan'


class Solution:
    mapping = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    def roman_to_int(self, string):
        result = 0
        max_ = 0
        for s in string[::-1]:
            if self.mapping[s] >= max_:
                max_ = self.mapping[s]
                result += self.mapping[s]
            else:
                result -= self.mapping[s]
        return result


if __name__ == '__main__':
    print(Solution().roman_to_int('MCMXCIV'))
