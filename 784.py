class Solution(object):
    def letterCasePermutation(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        results = list()
        self.dfs(s,'',results,0)

        print(results)
        return results



    def dfs(self,ss,path,results,index):
        if len(path) == len(ss):
            results.append(path)
            return


        if ord(ss[index]) >= ord('0') and ord(ss[index]) <= ord('9'):
            self.dfs(ss,path + ss[index],results,index+1)
        elif ord(ss[index]) >= ord('a') and ord(ss[index]) <= ord('z'):
            self.dfs(ss,path + ss[index],results,index+1)
            self.dfs(ss,path + chr(ord(ss[index]) - 32),results,index+1)

        else:
            self.dfs(ss, path + ss[index], results, index + 1)
            self.dfs(ss, path + chr(ord(ss[index]) + 32), results, index + 1)



if __name__ == '__main__':
    s = "a1b2"
    # s = "3z4"

    # s = '1b'
    solution = Solution()
    solution.letterCasePermutation(s)

