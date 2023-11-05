# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
# class NestedInteger(object):
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class NestedIterator(object):

    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        self.curr = 0
        self.l = self.putout(nestedList)
        print(self.l)

    def next(self):
        """
        :rtype: int
        """
        if self.hasNext():
            self.curr += 1
            return self.l[self.curr-1]

    def hasNext(self):
        """
        :rtype: bool
        """
        if self.curr < len(self.l):
            return True
        else:
            return False

    def putout(self,nestedList):
        l = list()
        for i in nestedList:
            if i.isInteger():
                l.append(i.getInteger())
            else:
                l.extend(self.putout(i.getList()))

        return l




# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())
