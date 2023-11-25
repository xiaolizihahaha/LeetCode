class Solution(object):
    def maxVowels(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        l = 0
        r = l + k - 1
        maxcount = 0

        sd = {
            'a':0,
            'e':0,
            'i':0,
            'o':0,
            'u':0
        }
        # if k == 1:
        #     if s.count('a') == 0 and s.count('e') == 0 and s.count('i') == 0 and s.count('o') == 0 and s.count('u') == 0:
        #         return 0
        #     else:
        #         return 1

        while r < len(s):
            if l == 0:
                for i in range(k):
                    if s[i] == 'a' or s[i] == 'e' or s[i] == 'i' or s[i] == 'o' or s[i] == 'u':
                        sd[s[i]] += 1
                # print(sd)
            else:

                if s[r] == 'a' or s[r] == 'e' or s[r] == 'i' or s[r] == 'o' or s[r] == 'u':
                    sd[s[r]] += 1
                if l != 0 :
                    if s[l-1] == 'a' or s[l-1] == 'e' or s[l-1] == 'i' or s[l-1] == 'o' or s[l-1] == 'u':
                        sd[s[l-1]] -= 1

                    # if sd[s[l]] < 0:
                    #     sd[s[l]] = 0

            maxcount = max(maxcount,sum(sd.values()))

            l += 1
            r += 1

        print(maxcount)
        return maxcount



if __name__ == '__main__':
    s = "abciiidef"
    k = 3

    s = "aeiou"
    k = 2

    s = "leetcode"
    k = 3

    s = "rhythms"
    k = 4
    #
    s = "tryhard"
    k = 4

    s = "novowels"
    k = 1

    # s = "tnfazcwrryitgacaabwm"
    # k = 4
    solution = Solution()
    solution.maxVowels(s,k)