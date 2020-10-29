"""
  @Author       : liujianhan
  @Date         : 2020/10/29 9:34
  @Project      : leetcode_in_python
  @FileName     : 599.两个列表的最小索引总和.py
  @Description  : 假设Andy和Doris想在晚餐时选择一家餐厅，并且他们都有一个表示最喜爱餐厅的列表，每个餐厅的名字用字符串表示。
    你需要帮助他们用最少的索引和找出他们共同喜爱的餐厅。 如果答案不止一个，则输出所有答案并且不考虑顺序。 你可以假设总是存在一个答案。
    示例 1:

    输入:
    ["Shogun", "Tapioca Express", "Burger King", "KFC"]
    ["Piatti", "The Grill at Torrey Pines", "Hungry Hunter Steakhouse", "Shogun"]
    输出: ["Shogun"]
    解释: 他们唯一共同喜爱的餐厅是“Shogun”。
    示例 2:

    输入:
    ["Shogun", "Tapioca Express", "Burger King", "KFC"]
    ["KFC", "Shogun", "Burger King"]
    输出: ["Shogun"]
    解释: 他们共同喜爱且具有最小索引和的餐厅是“Shogun”，它有最小的索引和1(0+1)。
    提示:

    两个列表的长度范围都在 [1, 1000]内。
    两个列表中的字符串的长度将在[1，30]的范围内。
    下标从0开始，到列表的长度减1。
    两个列表都没有重复的元素。
"""
from typing import List


class Solution:
    # 68ms, 13.7MB
    @staticmethod
    def find_restaurant(list1: List[str], list2: List[str]) -> List[str]:
        result = {}
        dic1 = {res: index for index, res in enumerate(list1)}
        for i, res in enumerate(list2):
            if res in dic1.keys():
                result[res] = dic1[res] + i
        minimum_index_sum = min([value for _, value in result.items()])
        return [key for key, value in result.items() if value == minimum_index_sum]

    # 380ms, 13.9MB
    @staticmethod
    def find_restaurant_v2(list1: List[str], list2: List[str]) -> List[str]:
        if len(list1) < len(list2):
            list1, list2 = list2, list1
        dic_long = {ele: index for index, ele in enumerate(list1)}
        mini_index_sum = 2000
        result = []
        for i, ele in enumerate(list2):
            if ele in set(list1):
                current_index_sum = i + dic_long[ele]
                if current_index_sum < mini_index_sum:
                    mini_index_sum = current_index_sum
                    result = [ele]
                elif current_index_sum == mini_index_sum:
                    result.append(ele)

        return result


if __name__ == '__main__':
    test_cases = [
        (["Shogun", "Tapioca Express", "Burger King", "KFC"],
         ["Piatti", "The Grill at Torrey Pines", "Hungry Hunter Steakhouse", "Shogun"]),
        (["Shogun", "Tapioca Express", "Burger King", "KFC"],
         ["KFC", "Shogun", "Burger King"]),
        (["Shogun", "KFC", "Tapioca Express", "Burger King"],
         ["KFC", "Shogun", "Burger King"])
    ]
    for tc in test_cases:
        print(Solution.find_restaurant(*tc))
        print(Solution.find_restaurant_v2(*tc))
