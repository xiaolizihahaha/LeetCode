import math


class Solution(object):
    def splitIntoFibonacci(self, num):
        """
        :type num: str
        :rtype: List[int]
        """
        paths = list()
        results = list()
        for i in range(1,int(len(num) / 2)+1):
            r1 = num[:i]
            # print(r1)
            for j in range(1,int((len(num) - i) / 2) + 1):
                r2 = num[i:i+j]
                r3 = num[i+j:]
                if len(r3) >= len(r2) and len(r3) >= len(r1):
                    if len(str(int(r1))) == len(r1) and len(str(int(r2))) == len(r2):
                        if r3.startswith(str(int(r1) + int(r2))):
                            if int(r1) < pow(2,31) and int(r2) < pow(2,31):
                            # print(r1,r2,r3)
                                pa = list()
                                pa.append(int(r1))
                                pa.append(int(r2))
                                self.dfs(r1,r2,r3,pa,results)
        if len(results) == 0:
            print([])
            return []
        else:
            print(results[0])
            return results[0]
        # print(results[0])

    def dfs(self,r1,r2,r3,path,results):
        if len(r3) == 0:
            results.append(path[:])
            return
        if r3.startswith(str(int(r1) + int(r2))) is True:
            if int(r1) + int(r2) < pow(2,31):
                path.append(int(r1) + int(r2))
                self.dfs(r2,str(int(r1) + int(r2)),r3[len(str(int(r1) + int(r2))):],path,results)
                path.pop(-1)




if __name__ == '__main__':
    num = "1101111"
    # num = "112358130"
    # num = "0123"
    # num = "539834657215398346785398346991079669377161950407626991734534318677529701785098211336528511"
    solution = Solution()
    solution.splitIntoFibonacci(num)