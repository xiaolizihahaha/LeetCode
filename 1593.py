class Solution(object):
    def maxUniqueSplit(self, s):
        """
        :type s: str
        :rtype: int
        """
        results = list()
        for i in range(len(s)):
            r1 = s[:i+1]
            r2 = s[i+1:]
            # print(r1,r2)
            self.dfs(s,r1,r2,[r1],results)

        # print(results)
        re = 0
        for r in results:
            if len(r) > re:
                re = len(r)

        print(re)
        return re

    def dfs(self,s,r1,r2,path,results):
        if len(r2) == 0:
            results.append(path[:])
            return

        for i in range(len(r2)):
            r1r = r2[:i+1]
            r2r = r2[i+1:]

            if r1r not in path:
                path.append(r1r)
                self.dfs(s,r1r,r2r,path,results)
                path.pop(-1)


if __name__ == '__main__':
    # s = "ababccc"
    # s = 'aba'
    s = 'aa'

    solution = Solution()
    solution.maxUniqueSplit(s)

