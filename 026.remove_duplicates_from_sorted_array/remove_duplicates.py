"""
  User: Liujianhan
  Time: 20:58
 """
__author__ = 'liujianhan'

class Solution:
    @staticmethod
    def remove_duplicates(num_list) -> int:
        for _index, num in enumerate(num_list):
            while num_list[_index+1] == num:
                num_list[_index] = num
                _index += 1
        return len(num_list)


if __name__ == '__main__':
    print(Solution.remove_duplicates([1,1,2,3,4]))