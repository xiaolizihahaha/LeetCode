class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """

        results = list()
        self.dfs(s,'',results,0)
        print(results)

    def dfs(self,remain,path,results,time):
        if time == 3 and int(remain) >= 0 and int(remain) <= 255 and len(remain) == len(str(int(remain))):
            path += remain
            results.append(path)
            return


        r1 = remain[:1]
        r1r = remain[1:]
        if int(r1) >= 0 and int(r1) <= 255 and len(r1) == len(str(int(r1))):
            if len(r1r) > 0 and len(r1r) <= (3-time) * 3:
                self.dfs(r1r,path + r1 + '.',results,time + 1)

        r2 = remain[:2]
        r2r = remain[2:]
        if int(r2) >= 0 and int(r2) <= 255 and len(r2) == len(str(int(r2))):
            if len(r2r) > 0 and len(r2r) <= (3-time) * 3:
                self.dfs(r2r,path + r2 + '.',results,time + 1)

        r3 = remain[:3]
        r3r = remain[3:]
        if int(r3) >= 0 and int(r3) <= 255 and len(r3) == len(str(int(r3))):
            if len(r3r) > 0 and len(r3r) <= (3-time) * 3:
                self.dfs(r3r,path + r3 + '.',results,time + 1)

if __name__ == '__main__':
    s = "25525511135"
    s = "0000"
    # s = "101023"
    solution = Solution()
    solution.restoreIpAddresses(s)