class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        anum = 0
        bnum = 0
        snum = 10 * [0]
        gnum = 10 * [0]
        for s,g in zip(secret,guess):
            # print(s,g)
            if s == g :
                anum += 1
            else:
                snum[int(s)] += 1
                gnum[int(g)] += 1

        bnum = sum(min(s,g)for s,g in zip(snum,gnum))

        return str(anum) + 'A' + str(bnum) + 'B'



if __name__ == '__main__':
    secret = "1807"
    guess = "7810"
    # 输出："1A3B"

    # secret = "1123"
    # guess = "0111"
    # 输出："1A1B"

    solution = Solution()
    result = solution.getHint(secret,guess)
    print(result)