class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """

        yuan = ['a','e','i','o','u','A','E','I','O','U']
        s1 = list(s)
        print(s1)

        p = 0
        q = len(s1) - 1

        while p <= q:
            while p <= q and s1[p] not in yuan:
                p += 1
            while p <= q and s1[q] not in yuan:
                q -= 1

            if p > q:
                break

            temp = s1[p]
            s1[p] = s1[q]
            s1[q] = temp
            p += 1
            q -= 1

        s2 = ''.join(s1)
        print(s2)
        return s2
if __name__ == '__main__':
    # s = "hello"
    s = "leetcode"
    solution = Solution()
    solution.reverseVowels(s)