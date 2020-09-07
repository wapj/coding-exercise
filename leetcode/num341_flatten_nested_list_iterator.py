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

    def getList(self) -> []:
        """
        @return the nested list that this NestedInteger holds, if it holds a nested list
        Return None if this NestedInteger holds a single integer
        """


"""
1. 재귀를 사용하여 배열을 펴는 방법을 사용
2. 스택을 사용하는 방법도 있는듯하다. 
3. 제너레이터를 사용하는 방법도 있는데 좀 복잡 
"""


class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.arr = []
        self.flattenList(nestedList)

    def flattenList(self, nestedList):
        for item in nestedList:
            if not item.isInteger():
                self.flattenList(item.getList())
            else:
                self.arr.append(item.getInteger())

    def next(self) -> int:
        return self.arr.pop(0)

    def hasNext(self) -> bool:
        return self.arr


"""
스택을 사용하는 방법
리스트가 나오면 다시 스택에 풀어서 넣는게 포인트이다.
"""
class NestedIterator(object):

    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        self.stack = nestedList[::-1]

    def next(self):
        """
        :rtype: int
        """
        return self.stack.pop().getInteger()

    def hasNext(self):
        """
        :rtype: bool
        """
        while self.stack:
            top = self.stack[-1]
            if top.isInteger():
                return True
            self.stack = self.stack[:-1] + top.getList()[::-1]
        return False
