class Solution(object):
    def longestNiceSubstring(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) == 0:
            return ''
        if len(s) == 1:
            return ''
        i = 0
        while i < len(s):
            if ord(s[i]) >= ord('a') and ord(s[i]) <= ord('z'):
                if chr(ord(s[i])-32) not in s[:i] and chr(ord(s[i])-32)  not in s[i+1:]:
                    break
            if ord(s[i]) >= ord('A') and ord(s[i]) <= ord('Z'):
                if chr(ord(s[i])+32) not in s[:i] and chr(ord(s[i])+32) not in s[i+1:]:
                    break
            i += 1

        if i == len(s):
            return s

        l1 = self.longestNiceSubstring(s[:i])
        l2 = self.longestNiceSubstring(s[i+1:])

        if len(l1) >= len(l2):
            return l1
        else:
            return l2


if __name__ == '__main__':
    s = "aYazaAay"
    # s = "Bb"
    s = "dDzeE"
    solution = Solution()
    res = solution.longestNiceSubstring(s)
    print(res)
