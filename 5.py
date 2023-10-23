class Solution(object):

    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """

        reverses = s[::-1]

        # s = "babad"
        # s = "dabab"


        slength = len(s)

        maxlength = 1
        maxsub = ''

        for i in range(slength):
            for j in range(i,slength):

                tempsub = s[i:j+1]
                templength = len(tempsub)


                if s[i:j+1] == reverses[slength-i-templength:slength-i]:
                    # print(tempsub,templength)

                    if maxlength <= templength:
                        maxsub = tempsub
                        maxlength = templength

        return maxsub















if __name__ == '__main__':


    # s = "babad"
    # s1= "dabab"

    # s = "cbbd"
    # s1= "dbbc"

    s = "aacabdkacaa"
    s1= "aacakdbacaa"

    s1 = s[::-1]


    solution = Solution()
    result = solution.longestPalindrome(s)

    print(result)

