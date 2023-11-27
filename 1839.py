class Solution(object):
    def longestBeautifulSubstring(self, word):
        """
        :type word: str
        :rtype: int
        """



        beau = []
        total = []

        i = 0
        k = 0
        while i < len(word):
            curr = word[i]
            if i == 0:
                beau.append(word[i])
                total.append(1)
                k += 1
                i += 1
            else:
                beau.append(word[i])
                total.append(1)
                k += 1
                i += 1


            while i < len(word) and word[i] == curr:
                total[k-1] += 1
                i += 1

        print(beau)
        print(total)
        if len(beau) < 5:
            return 0

        l = 0
        r = l + 5 - 1
        maxlength = 0

        while r < len(beau):
            if beau[l:r+1] == ['a','e','i','o','u']:
                maxlength = max(maxlength,sum(total[l:r+1]))
            l += 1
            r += 1
        print(maxlength)

        return maxlength






if __name__ == '__main__':
    word = "aeiaaioaaaaeiiiiouuuooaauuaeiu"
    word = "aeeeiiiioooauuuaeiou"
    s = Solution()
    s.longestBeautifulSubstring(word)