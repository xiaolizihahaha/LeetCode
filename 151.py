class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        length = len(s)

        p = length - 1
        q = length - 1

        newstr = ''
        while p >= 0:
            while s[p] == ' ':
                p -= 1
                if p < 0:
                    break
            q = p
            while s[q] != ' ' and q >= 0:
                q -= 1
            sig = q
            q = q + 1

            while q != p+1:
                newstr += s[q]
                q = q+1
            print(sig,'aa')
            if s[:sig+1].count(' ') != sig+1:
                newstr += ' '

            p = sig
        print(newstr+'1')
        return newstr




if __name__ == '__main__':
    s = "the sky is blue"
    # s = "  hello world  "
    # s = "a good   example"
    solution = Solution()
    solution.reverseWords(s)