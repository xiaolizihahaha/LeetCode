class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        result = 0
        for i in range(0,len(haystack)-len(needle)+1):
            # print(i)
            p = i
            q = 0

            while True:
                if q == len(needle):
                    break
                if haystack[p] == needle[q]:
                    p += 1
                    q += 1

                else:
                    break
            if q == len(needle):

                result = p - len(needle)
                print(result)
                return result
        print(-1)
        return -1



if __name__ == '__main__':
    # haystack = "sadbutsad"
    # needle = "sad"

    haystack = "leetcode"
    needle = "leeto"
    solution = Solution()
    solution.strStr(haystack,needle)