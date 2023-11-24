class Solution(object):
    def numberOfSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        l = 0
        r = 0
        res = 0
        d = dict()

        while r < len(s):
            if s[r] not in d:
                d[s[r]] = 1
            else:
                d[s[r]] += 1

            r += 1

            while l < r and len(d) == 3:
                res += len(s) - r + 1
                d[s[l]] -= 1
                if d[s[l]] == 0:
                    d.pop(s[l])

                l += 1
        print(res)
        return res

if __name__ == '__main__':
    s = "abcabc"
    # 10

    s = "aaacb"
    # 3

    s = "abc"
    # 1

    solution = Solution()
    solution.numberOfSubstrings(s)
