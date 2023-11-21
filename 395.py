class Solution(object):
    def longestSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        ds = dict()
        for ch in s:
            if ch not in ds:
                ds[ch] = 1
            else:
                ds[ch] += 1

        flag = True
        tag = ''
        for d in ds:
            if ds[d] < k:
                tag = d
                flag = False
                break
        if flag is True:
            return len(s)
        else:
            ress = []
            # print(tag)
            slist = s.split(tag)
            # print(slist)
            for sl in slist:
                if len(sl) != 0:
                    ress.append(self.longestSubstring(sl,k))
            if len(ress) != 0:
                print(max(ress))
                return max(ress)
            else:
                print(0)
                return 0



if __name__ == '__main__':
    s = "aaabb"
    k = 3

    s = "ababbc"
    k = 2

    s = "weitong"
    k = 2
    solution = Solution()
    print('a',solution.longestSubstring(s,k))