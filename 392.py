class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) == 0:
            return True
        p = 0
        q = 0

        while p < len(s) and q < len(t):
            while q < len(t) and t[q] != s[p]:
                q += 1
            if q >= len(t):
                break
            if t[q] == s[p]:
                q += 1
                p += 1

            if p == len(s):
                print(1)
                return True

        print(0)
        return False



s = "abc"
t = "bcahbgdc"

s = "axc"
t = "ahbgdc"
