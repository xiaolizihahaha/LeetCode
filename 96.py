class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        result = [-1] * 20
        result[0] = 1
        result[1] = 1

        if n == 0:
            return 0


        for i in range(2,n+1):
            sum = 0
            for j in range(0,i):
                sum += result[j] * result[i-1-j]
            result[i] = sum

        print(result)
        return result[n]





