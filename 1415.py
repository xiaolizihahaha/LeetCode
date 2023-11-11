class Solution(object):
    def getHappyString(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        results = list()

        self.dfs('abc', n, '', results)
        if k > len(results):
            print('')
            return ''
        else:
            print(results[k-1])
            return results[k-1]


    def dfs(self,chars,n,path,results):
        if len(path) == n:
            results.append(path[:])
            return

        char1 = ''
        for char in chars:
            if char == 'a':
                char1 = 'bc'
            elif char == 'b':
                char1 = 'ac'
            elif char == 'c':
                char1 = 'ab'
            self.dfs(char1,n,path+char,results)


if __name__ == '__main__':
    # n = 1
    # k = 3

    n = 1
    k = 3
    #
    # n = 3
    # k = 9
    solution = Solution()
    solution.getHappyString(n,k)