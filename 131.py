class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        results = list()
        self.dfs(s,[],results)

        print(results)

    def dfs(self,s,path,results):
        if len(s) == 0:
            results.append(path[:])
            return

        for i in range(len(s)):
            r1 = s[:i+1]
            r1r = s[i+1:]
            r2 = r1[::-1]

            if r1 == r2:
                path.append(r1)
                self.dfs(r1r,path,results)
                path.pop(-1)


if __name__ == '__main__':
    s = 'aab'
    s = 'a'
    # a = 'abcba'
    # b = a[::-1]
    # print(a == b)
    solution = Solution()
    solution.partition(s)
