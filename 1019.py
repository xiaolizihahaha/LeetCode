# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def nextLargerNodes(self, head):
        """
        :type head: ListNode
        :rtype: List[int]
        """
        nodel = list()
        p = head
        while p is not None:
            nodel.append(p.val)
            p = p.next

        answer = [-1] * len(nodel)
        answer[-1] = len(nodel) + 1

        i = len(nodel) - 2
        while i >= 0:
            if nodel[i] < nodel[i + 1]:
                answer[i] = i + 1
            else:
                j = i+1
                while j < len(answer):
                    if answer[j] == len(nodel) + 1:
                        break
                    if nodel[answer[j]] > nodel[i]:
                        break
                    j = answer[j]

                if answer[j] !=len(answer) + 1 and nodel[answer[j]] > nodel[i]:
                    answer[i] = answer[j]
                else:
                    answer[i] =len(nodel) + 1
            # print(answer[i])
            i -= 1
        # print(answer)


        result = [0] * len(nodel)

        for i in range(len(nodel)):
            if answer[i] != len(nodel) + 1:
                result[i] = nodel[answer[i]]
            else:
                result[i] = 0


                # last = answer[i:]
                # j = 0
                # while j < len(last):
                #     if last[j] > nodel[i]:
                #         break
                #     j += 1
                # if j != len(last) and last[j] > nodel[i]:
                #     answer[i] = last[j]
                # else:
                #     answer[i] = 0


                # if answer[i + 1] > nodel[i]:
                #     answer[i] = answer[i + 1]
                #
                #
                #
                #
                # else:
                #     last = nodel[i + 1:]
                #     # print("aaa",last)
                #     j = 0
                #     for j in range(len(last)):
                #         if last[j] > nodel[i]:
                #             break
                #     if last[j] > nodel[i]:
                #         answer[i] = last[j]
                #     else:
                #         answer[i] = 0

        print(result)
        return result


if __name__ == '__main__':

    nodel = [2,1,5]
    # nodel = [2,7,4,3,5]
    solution = Solution()

    solution.nextLargerNodes(nodel)
