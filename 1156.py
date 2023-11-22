#没思路 看了别人的代码

class Solution(object):
    def maxRepOpt1(self, text):
        """
        :type text: str
        :rtype: int
        """
        dtext = dict()
        for t in text:
            if t not in dtext:
                dtext[t] = 1
            else:
                dtext[t] += 1

        # print(dtext)

        res = 0
        i = 0

        while i < len(text):
            j = i
            while j < len(text) and text[j] == text[i]:
                j += 1
            l = j - i
            k = j + 1
            while k < len(text) and text[k] == text[i]:
                k += 1
            r = k - j - 1

            res = max(res,min(l+r+1,dtext[text[i]]))
            i = j

        print(res)
        return res





if __name__ == '__main__':
    # text = "ababa"
    # 输出：3

    text = "aaabaaa"
    # # 输出：6
    #
    text = "aaabbaaa"
    # # 输出：4
    #
    text = "aaaaa"
    # # 输出：5
    #
    text = "abcdef"
    # # 输出：1

    solution = Solution()
    solution.maxRepOpt1(text)
