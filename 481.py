class Solution(object):
    def magicalString(self, n):
        """
        :type n: int
        :rtype: int
        """

        s = '12'
        p = 1
        q = 1

        if n <= 3:
            return 1

        while q < n - 1:
            if s[p] == '1':
                if s[q] =='1':
                    s += '2'
                else:
                    s += '1'
                q += 1

            elif s[p] == '2':
                if q == 1:
                    s += '2'
                    q += 1
                else:
                    if s[q] == '1':
                        s += '22'
                    else:
                        s += '11'
                    q += 2
            p += 1
        print(s[:n])
        print(s[:n].count('1'))
        return s[:n-1].count('1')


if __name__ == '__main__':
    n = 4
    solution = Solution()
    solution.magicalString(n)



