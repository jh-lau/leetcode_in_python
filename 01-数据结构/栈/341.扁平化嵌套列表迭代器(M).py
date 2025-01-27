"""
  @Author       : liujianhan
  @Date         : 21/3/23 9:13
  @Project      : leetcode_in_python
  @FileName     : 341.扁平化嵌套列表迭代器(M).py
  @Description  : Placeholder
"""


class NestedInteger:
    def isInteger(self) -> bool:
        """
        @return True if this NestedInteger holds a single integer, rather than a nested list.
        """

    def getInteger(self) -> int:
        """
        @return the single integer that this NestedInteger holds, if it holds a single integer
        Return None if this NestedInteger holds a nested list
        """

    def getList(self) -> ['NestedInteger']:
        """
        @return the nested list that this NestedInteger holds, if it holds a nested list
        Return None if this NestedInteger holds a single integer
        """


def gen(nestedList):
    for ele in nestedList:
        if ele.isInteger():
            yield ele.getInteger()
        else:
            yield from gen(ele.getList())


class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.gen = gen(nestedList)
        self.stored = (False, 0)

    def next(self) -> int:
        if not self.hasNext():
            return -1
        result = self.stored[1]
        self.stored = (False, 0)
        return result

    def hasNext(self) -> bool:
        if self.stored[0]:
            return True
        try:
            self.stored = (True, next(self.gen))
            return True
        except Exception:
            return False


if __name__ == '__main__':
    pass
