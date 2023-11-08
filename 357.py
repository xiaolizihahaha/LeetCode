class Solution(object):
    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        """

        if n == 0:
            return 1
        if n == 1:
            return 10
        else:
            cheng = 9
            for i in range(n-1):
                cheng *= (9-i)
            return  cheng + self.countNumbersWithUniqueDigits(n-1)


if __name__ == '__main__':
    n = 2

    solution = Solution()
    print(solution.countNumbersWithUniqueDigits(n))