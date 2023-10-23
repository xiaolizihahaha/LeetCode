class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        nList = [1]
        point2 = 0
        point3 = 0
        point5 = 0
        pointNow = 0

        while pointNow < n - 1:

            newnum = min(nList[point2] * 2, nList[point3] * 3, nList[point5] * 5)

            if newnum == nList[point2] * 2:
                point2 += 1
            if newnum == nList[point3] * 3:
                point3 += 1
            if newnum == nList[point5] * 5:
                point5 += 1
            pointNow += 1
            nList.append(newnum)
        # print(nList)
        return nList[n-1]


if __name__ == '__main__':

    n = 1
    n = 10

    solution = Solution()
    result = solution.nthUglyNumber(n)
    print(result)