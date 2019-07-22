"""
  Created by PyCharm.
  User: Liujianhan
  Date: 2019/6/11
  Time: 19:25
 """
import random

__author__ = 'liujianhan'


class BucketSort:
    @staticmethod
    def _max(num_list):
        largest = num_list[0]
        for num in num_list:
            if num > largest:
                largest = num
        return largest

    @staticmethod
    def _min(num_list):
        smallest = num_list[0]
        for num in num_list:
            if num < smallest:
                smallest = num
        return smallest

    @staticmethod
    def bucket_sort(num_list):
        pass


if __name__ == '__main__':
    test_1 = [random.randint(0, 100) for i in range(20)]
    print(test_1)
    print(BucketSort._max(test_1))
    print(BucketSort._min(test_1))
