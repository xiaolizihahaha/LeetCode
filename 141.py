# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        nodeList = []
        pre = head

        while pre != None and pre not in nodeList:
            nodeList.append(pre)
            pre = pre.next

        if pre in nodeList:
            return True

        return False
