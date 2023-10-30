# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution(object):
    def numComponents(self, head, nums):
        """
        :type head: ListNode
        :type nums: List[int]
        :rtype: int
        """

        p = head
        hlen = 0
        while p is not None:
            hlen += 1
            p = p.next

        nodel = [0] * (hlen + 1)

        p = head
        for i in range(hlen):
            if p.val in nums:
                nodel[i + 1] = 1

            p = p.next
        print("aaa", nodel)

        for i in range(hlen):
            if nodel[i + 1] != 0:
                nodel[i + 1] = nodel[i] + 1

        print('bbb', nodel)

        start = 0
        end = hlen + 1

        while nodel[start] == 0:
            start += 1
        for i in range(1, hlen + 1):
            last = nodel[i:hlen + 1]
            if last.count(0) == hlen - i + 1:
                end = i
                break

        num = 0
        i = start

        print(start,end)
        while i < end:
            if nodel[i] != 0:
                num += 1
                while i < end  and nodel[i] != 0:
                    i += 1

            else:
                while i < end  and nodel[i] == 0:
                    i += 1


        print('bbb', num)

        return num


