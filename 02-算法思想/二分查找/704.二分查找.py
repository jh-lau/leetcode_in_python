"""
  Created by PyCharm.
  User: Liujianhan
  Date: 2019/5/25
  Time: 20:55
 """
__author__ = 'liujianhan'


class Solution:

    def __init__(self):
        pass

    @staticmethod
    def search(array, target):
        if not isinstance(array, list):
            return False
        low = 0
        high = len(array) - 1
        while low <= high:
            mid = low + ((high - low) >> 1)
            if array[mid] < target:
                low = mid + 1
            elif array[mid] > target:
                high = mid - 1
            else:
                return array[mid], mid
        return False


test = [-1, 0, 3, 5, 9, 12]
test_1 = [1, 3, 5, 100, -1, 20]
print(Solution.search(test, 9))
