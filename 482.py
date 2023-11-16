class Solution(object):
    def licenseKeyFormatting(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        toreverse = ''
        p = len(s) - 1

        while p >= 0:
            i = 0
            while i < k:
                if s[p] == '-':
                    p -= 1
                elif ord(s[p]) >= ord('a') and ord(s[p]) <= ord('z'):
                    toreverse += chr(ord(s[p]) - 32)
                    p -= 1
                    i += 1
                else:
                    toreverse += s[p]
                    p -= 1
                    i += 1
                if p < 0:
                    break

            toreverse += '-'

        print(toreverse)
        # toreverse
        print(toreverse[::-1].strip('-'))
        return toreverse[::-1].strip('-')




if __name__ == '__main__':
    S = "5F3Z-2e-9-w"
    k = 4
    #
    # S = "2-5g-3-J"
    # k = 2

    solution = Solution()
    solution.licenseKeyFormatting(S,k)
    # path = ''
    # path += chr(ord('a') - 32)
    # print(path)