class Solution(object):
    # def wordBreak(self, s, wordDict):
    #     """
    #     :type s: str
    #     :type wordDict: List[str]
    #     :rtype: bool
    #     """
    #     if not s:
    #         return True
    #
    #     for word in wordDict:
    #         if s.startswith(word):
    #             if self.wordBreak(s[len(word):],wordDict):
    #                 return True
    #     return False

    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """

        dp = [False] * (len(s) + 1)
        dp[0] = True

        for i in range(len(s)+1):
            if dp[i] == True:
                for j in range(i+1,len(s)+1):
                    if s[i:j] in wordDict:
                        dp[j] = True


        return dp[-1]


if __name__ == '__main__':

    s = "leetcode"
    wordDict = ["leet", "code"]
    # 输出: true


    # s = "applepenapple"
    # wordDict = ["apple", "pen"]
    # # 输出: true
    #
    # s = "catsandog"
    # wordDict = ["cats", "dog", "sand", "and", "cat"]
    # # 输出: false

    solution = Solution()
    result = solution.wordBreak(s,wordDict)
    print(result)