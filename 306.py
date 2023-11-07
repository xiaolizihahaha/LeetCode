class Solution(object):
    def isAdditiveNumber(self, num):
        """
        :type num: str
        :rtype: bool
        """

        result = []
        sig = False
        for i in range(0, int(len(num) / 2)):
            for j in range(i + 1, i + 1 + int((len(num) - i) / 2)):

                r1 = num[:i + 1]
                r2 = num[i + 1:j + 1]
                r3 = num[j + 1:]
                if len(r3) < len(r1) or len(r3) < len(r2):
                    continue
                if len(r1) != len(str(int(r1))) or len(r2) != len(str(int(r2))):
                    continue




                print(r1, r2, r3)
                self.dfs(num, result, r1, r2, r3)
                if 1 in result:
                    sig = True
                    break
        print(result)
        print(sig)
        return sig

    def dfs(self,num,result,r1,r2,r3):
        if len(r3) == 0:
            result.append(1)

        if r3.startswith(str(int(r1)+int(r2))) is False:
            return


        else:
            newstr = r2+r3
            sum = str(int(r1)+int(r2))
            self.dfs(newstr,result,r2,sum,r3[len(sum):])




if __name__ == '__main__':
    num = "112358"
    num = "199100199"
    num = '123'
    num = "0235813"
    # num = '0000'
    s = '0'
    print('aaa',len(str(int(s))))

    solution = Solution()
    solution.isAdditiveNumber(num)
