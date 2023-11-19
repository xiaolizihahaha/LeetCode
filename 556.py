class Solution(object):
    def nextGreaterElement(self, n):
        """
        :type n: int
        :rtype: int
        """
        num = list(str(n))
        print(num)
        nmax = sorted(num,reverse=True)

        if nmax == num:
            print(-1)
            return -1

        i = len(num) - 2
        while i >= 0:
            j = len(num) - 1
            while j > i:
                if num[j] > num[i]:
                    temp = num[j]
                    num[j] = num[i]
                    num[i] = temp

                    newnum1 = num[:i+1]
                    newnum2 = num[i+1:]
                    newnum2.sort()
                    newnum1.extend(newnum2)
                    print(newnum1)
                    res1 = ''.join(newnum1)
                    res = int(res1)
                    print(res)
                    if res > pow(2,31) - 1:
                        return -1
                    else:
                        return res

                else:
                    j -= 1
            i -= 1







if __name__ == '__main__':
    n = 12
    n = 21
    n = 31254
    # n =9
    # n = 54321
    solution = Solution()
    solution.nextGreaterElement(n)
