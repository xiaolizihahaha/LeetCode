class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        temp = n
        sums = list()
        while True:

            middles = list()
            while temp != 0:
                middles.append(int(temp % 10))
                temp = (temp - (temp % 10)) / 10

            sum = 0
            for middle in middles:
                sum += middle * middle
            if sum == 1:
                return True
            if sum in sums:
                return False

            sums.append(sum)
            temp = sum



if __name__ == '__main__':
    # n = 19
    # n = 2
    n = 1111111
    solution = Solution()
    result = solution.isHappy(n)
    print(result)