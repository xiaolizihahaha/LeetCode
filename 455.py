class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g.sort()
        s.sort()

        p = 0
        q = 0

        while p < len(g) and q < len(s):
            if g[p] <= s[q]:
                p += 1
                q += 1
            else:
                q += 1

        print(p)
        return p

if __name__ == '__main__':
    g = [1, 2, 3]
    s = [1, 1]

    g = [1, 2]
    s = [1, 2, 3]
    solution = Solution()
    solution.findContentChildren(g,s)