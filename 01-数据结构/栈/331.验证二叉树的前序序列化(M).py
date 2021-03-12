"""
  @Author       : liujianhan
  @Date         : 21/3/12 10:09
  @Project      : leetcode_in_python
  @FileName     : 331.验证二叉树的前序序列化(M).py
  @Description  : 序列化二叉树的一种方法是使用前序遍历。当我们遇到一个非空节点时，我们可以记录下这个节点的值。如果它是一个空节点，
    我们可以使用一个标记值记录，例如 #。

         _9_
        /   \
       3     2
      / \   / \
     4   1  #  6
    / \ / \   / \
    # # # #   # #
    例如，上面的二叉树可以被序列化为字符串 "9,3,4,#,#,1,#,#,2,#,6,#,#"，其中 # 代表一个空节点。
    给定一串以逗号分隔的序列，验证它是否是正确的二叉树的前序序列化。编写一个在不重构树的条件下的可行算法。
    每个以逗号分隔的字符或为一个整数或为一个表示 null 指针的 '#' 。
    你可以认为输入格式总是有效的，例如它永远不会包含两个连续的逗号，比如 "1,,3" 。

    示例 1:
    输入: "9,3,4,#,#,1,#,#,2,#,6,#,#"
    输出: true

    示例 2:
    输入: "1,#"
    输出: false

    示例 3:
    输入: "9,#,#,1"
    输出: false
"""


class Solution:
    # 44ms, 14.7MB
    @staticmethod
    def is_valid_serialization(preorder: str) -> bool:
        num = 1
        preorder = preorder.split(',')
        for i in preorder:
            if num == 0:
                return False
            if i == '#':
                num -= 1
                if num < 0:
                    return False
            else:
                num += 1
        if num == 0:
            return True
        else:
            return False


if __name__ == '__main__':
    test_cases = [
        "9,3,4,#,#,1,#,#,2,#,6,#,#",
        "1,#",
        "9,#,#,1"
    ]
    for test_case in test_cases:
        print(Solution.is_valid_serialization(test_case))
