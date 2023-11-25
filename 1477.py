from sortedcontainers import SortedDict,SortedList

class Solution(object):
    def minSumOfLengths(self, arr, target):
        """
        :type arr: List[int]
        :type target: int
        :rtype: int
        """

        # minlen = []
        startend = []
        # startendmap = SortedDict()
        startendList = SortedList()




        # end = []

        l = 0
        r = 0
        sum1 = 0

        if sum(arr) < target:
            return -1
        while r < len(arr):
            sum1 += arr[r]
            r += 1

            while l < r and sum1 >= target:
                if sum1 == target:
                    #     if len(minlen) < 2:
                    #         minlen.append(r - l)
                    #     else:
                    #         if r-l < max(minlen):
                    #             minlen.pop(minlen.index(max(minlen)))
                    #             minlen.append(r-l)
                    #     minlen.append(r - l)
                    # startend.append([l, r - 1])
                    startendList.add([r-l,l,r-1])

                sum1 -= arr[l]
                l += 1
        # print(minlen)
        # print(start)
        # print(startend)

        # startend.sort(key=lambda x: x[1] - x[0] + 1)
        # print(startend)
        minres = pow(10, 7)
        res = 0

        print(startendList[0])

        for i in range(len(startendList)):
            if startendList[i][0] >= minres:
                break
            for j in range(i + 1, len(startendList)):
                if startendList[i][1] > startendList[j][2] or startendList[i][2] < startendList[j][1]:
                    if startendList[j][0] >= minres:
                        break
                    res = startendList[i][0] + startendList[j][0]
                    minres = min(minres, res)


                    # print(res)
                    # return res

        if minres != pow(10, 7):
            print(minres)
            return minres

        else:
            print(-1)
            return -1




        # if len(minlen) != 2:
        #     return -1
        # else:
        #     return sum(minlen)




if __name__ == '__main__':
    arr = [3, 2, 2, 4, 3]
    target = 3
    # arr = [7, 3, 4, 7]
    # target = 7

    # arr = [4, 3, 2, 6, 2, 3, 4]
    # target = 6
    #
    # arr = [5, 5, 4, 4, 5]
    # target = 3

    # arr = [3, 1, 1, 1, 5, 0, 2, 1,4]
    # target = 3

    arr = [1, 6, 1]
    target = 7

    arr = [2,2,4,4,4,4,4,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
    target = 20


    solution = Solution()
    solution.minSumOfLengths(arr, target)