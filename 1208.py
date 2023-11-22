class Solution(object):
    def equalSubstring(self, s, t, maxCost):
        """
        :type s: str
        :type t: str
        :type maxCost: int
        :rtype: int
        """
        res = 0
        l = 0
        r = 0
        cost = 0

        while r < len(s):
            if s[r] == t[r]:
                r += 1
            else:
                cost += abs(ord(s[r]) - ord(t[r]))
                r += 1
            while l < r and cost > maxCost:
                res = max(res,r-l-1)
                cost -= abs(ord(s[l]) - ord(t[l]))
                l += 1

        res = max(res, r - l)

        print(res)
        return res


if __name__ == '__main__':
    s = "aabcd"
    t = "zbcdf"
    maxCost = 3

    # s = "abcd"
    # t = "cdef"
    # maxCost = 3
    #
    s = "abcd"
    t = "acde"
    maxCost = 0

    solution = Solution()
    solution.equalSubstring(s,t,maxCost)