class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        news = ''
        for c in s:
            if ord(c) >= ord('a') and ord(c) <= ord('z') or ord(c) >= ord('0') and ord(c) <= ord('9'):
                news += c
            elif ord(c) >= ord('A') and ord(c) <= ord('Z'):
                news += chr(ord(c) + 32)
        # print(news)
        if len(news) == 0:
            print(1)
            return True

        p = 0
        q = len(news) - 1
        sig = True
        while p <= len(news) // 2:
            if news[p] == news[q]:
                p += 1
                q -= 1

            else:
                # print(p,q)
                sig = False
                break

        print(sig)
        return sig


if __name__ == '__main__':
    # s = "A man, a plan, a canal: Panama"
    s = "race a car"
    s = " "
    # s = 'aa'
    solution = Solution()
    solution.isPalindrome(s)
