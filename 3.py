class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        # s = "abcabcbb"
        maxlength = 0
        sLength = len(s)


        for i in range(sLength):
            tempLength = 1

            for j in range(i+1, sLength):
                if s.find(s[j],i,j) == -1:
                    tempLength += 1
                    # print(s[i],s[j],tempLength)
                else:
                    break
            if maxlength < tempLength:
                maxlength = tempLength
            # print(maxlength)


        return maxlength

if __name__ == '__main__':

    # s = "abcabcbb"

    # s = "bbbbb"
    #
    s = "pwwkew"

    solution = Solution()
    result = solution.lengthOfLongestSubstring(s)

    print(result)