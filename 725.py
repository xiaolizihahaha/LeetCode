# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def splitListToParts(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: List[ListNode]
        """
        hlen = 0
        p = head
        nodes = list()
        while p is not None:
            hlen += 1
            nodes.append(p)
            p = p.next

        # hlen = 7
        # k = 3

        temp = int(hlen / k)
        long = int(hlen % k)
        short = k - long

        lenthlist = list()
        for i in range(long):
            lenthlist.append(temp + 1)
        for i in range(short):
            lenthlist.append((temp))

        # print(lenthlist)
        startlist = [0] * k
        for i in range(k):
            if lenthlist[i] == 0:
                startlist[i] = -1
            else:
                if i == 0:
                    startlist[i] = 0
                else:
                    startlist[i] = startlist[i-1] + lenthlist[i-1]
            # print(startlist[i])

        nodelist = list()
        for i in range(k):
            if startlist[i] == -1:
                nodelist.append(None)
            else:
                nodelist.append(nodes[startlist[i]])
                nodes[startlist[i] + lenthlist[i] - 1].next = None

        return nodelist





if __name__ == '__main__':
    solution = Solution()
    solution.splitListToParts(None,3)

