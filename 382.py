import random
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):

    def __init__(self, head):
        """
        :type head: Optional[ListNode]
        """
        self.l = list
        p = head
        while p is not None:
            self.l.append(p)
            p = p.next


    def getRandom(self):
        """
        :rtype: int
        """
        return random.choice(self.l).val



# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()