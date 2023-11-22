class Solution(object):
    def balancedString(self, s):
        """
        :type s: str
        :rtype: int
        """
        n4 = int(len(s) / 4)
        sdict = {
            'Q':n4,
            'W':n4,
            'E':n4,
            'R':n4
        }

        for i in s:
            sdict[i] -= 1

        flag = True
        needchange = 0
        for key in sdict:
            if sdict[key] < 0:
                flag = False
                sdict[key] = abs(sdict[key])
                needchange += sdict[key]
            else:
                sdict[key] = -1

        print(sdict)
        print(needchange)

        if flag is True:
            print(0)
            return 0

        if sdict['Q'] == -1:
            sdict.pop('Q')

        if sdict['W'] == -1:
            sdict.pop('W')

        if sdict['E'] == -1:
            sdict.pop('E')

        if sdict['R'] == -1:
            sdict.pop('R')

        print(sdict)



        l = 0
        r = 0
        minlength = len(s) + 1
        length = len(s) + 1


        while r < len(s):
            if s[r] in sdict:
                sdict[s[r]] -= 1
                r += 1
            else:
                r += 1

            # dict 都小于等于0时,flag = T
            flag = True
            for d in sdict:
                if sdict[d] > 0:
                    flag = False

            while l < r and flag is True:
                minlength = min(minlength,r-l)
                if s[l] in sdict:
                    sdict[s[l]] += 1
                    l += 1


                else:
                    l += 1

                flag = True
                for d in sdict:
                    if sdict[d] > 0:
                        flag = False

        minlength = min(minlength,r-l+1)

        print(minlength)
        return minlength








if __name__ == '__main__':
    s = "QWER"
    # 输出：0

    # s = "QQWE"
    # 输出：1

    # s = "QQQW"
    # 输出：2

    s = "QQQQ"
    # 输出：3

    # s = "QRQWEQWQ"
    # 输出：3

    s = "WQWRQQQW"
    solution = Solution()
    solution.balancedString(s)