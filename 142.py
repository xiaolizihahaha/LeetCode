# Definition for singly-linked list.
class ListNode:
    def __init__(self,val,next):
        self.val = val
        self.next = next

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        #记录链表节点的索引到nodeList中，每次遇到节点都查询nodelist，如果存在其中，则返回该节点。
        # nodeList = []
        # pre = head
        #
        #
        # while pre != None and pre not in nodeList:
        #     nodeList.append(pre)
        #     pre = pre.next
        #
        # return pre

        #构造两个指针fast、slow，相遇两次
        fast = head
        slow = head

        while True:

            if fast == None or fast.next == None:
                return None

            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                break

        fast = head
        while fast != slow:
            fast = fast.next
            slow = slow.next

        return slow



