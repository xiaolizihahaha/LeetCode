class Solution(object):
    def maxFreq(self, s, maxLetters, minSize, maxSize):
        """
        :type s: str
        :type maxLetters: int
        :type minSize: int
        :type maxSize: int
        :rtype: int
        """

        l = 0
        r = 0
        differ = dict()
        res = dict()

        while r < len(s):
            if s[r] not in differ:
                differ[s[r]] = 1
                r += 1
            else:
                differ[s[r]] += 1
                r += 1

            while l < r and len(differ) > maxLetters:
                if r - l - 1 >= minSize:
                    k = r
                    while k - l - 1 > maxSize:
                        k -= 1
                    while k - l -1 >= minSize:
                        if s[l:k-1] not in res:
                            res[s[l:k-1]] = 1
                        else:
                            res[s[l:k-1]] += 1

                        k -= 1

                differ[s[l]] -= 1
                if differ[s[l]] == 0:
                    differ.pop(s[l])

                l += 1

        r += 1

        if len(differ) <= maxLetters:
            while l < len(s):
                if r - l - 1 >= minSize:
                    k = r
                    while k - l - 1 > maxSize:
                        k -= 1
                    while k - l -1 >= minSize:
                        if s[l:k-1] not in res:
                            res[s[l:k-1]] = 1
                        else:
                            res[s[l:k-1]] += 1
                        k -= 1

                differ[s[l]] -= 1
                if differ[s[l]] == 0:
                    differ.pop(s[l])

                l += 1



        # print(max(res.values()))
        if len(res) == 0:
            return 0
        else:
            return max(res.values())




if __name__ == '__main__':
    # s = "aababcaab"
    # maxLetters = 2
    # minSize = 3
    # maxSize = 4
    # 输出：2

    # s = "aaaa"
    # maxLetters = 1
    # minSize = 3
    # maxSize = 3
    # # 输出：2
    #
    s = "aabcabcab"
    maxLetters = 2
    minSize = 2
    maxSize = 3
    # # 输出：3
    #
    s = "abcde"
    maxLetters = 2
    minSize = 3
    maxSize = 3
    # # 输出：0

    solution = Solution()
    solution.maxFreq(s, maxLetters, minSize, maxSize)
