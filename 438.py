# 暴力 超时
# class Solution(object):
#     def findAnagrams(self, s, p):
#         """
#         :type s: str
#         :type p: str
#         :rtype: List[int]
#         """
#         res = []
#         sortp = sorted(p)
#         for index,s1 in enumerate(s):
#             temp = s[index:index+len(p)]
#             sorttemp = sorted(temp)
#             if sorttemp == sortp:
#                 res.append(index)
#
#         print(res)
#         return res


# 滑动窗口
class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        if len(s) < len(p):
            return []
        res = []
        sdict = dict()
        pdict = dict()
        for i in range(26):
            sdict[chr(ord('a') + i)] = 0
        for i in range(26):
            pdict[chr(ord('a') + i)] = 0

        for s1 in p:
            pdict[s1] += 1

        left = 0
        right = left + len(p) - 1

        for i in range(left,right+1):
            sdict[s[i]] += 1

        while left <= len(s) - len(p):
            if sdict == pdict:
                res.append(left)


            if right+1 >= len(s):
                break
            sdict[s[left]] -= 1
            sdict[s[right+1]] += 1
            left += 1
            right += 1

        print(res)
        return res








if __name__ == '__main__':
    s = "cbaebabacd"
    p = "abc"
    # [0,6]
    #
    # s = "abab"
    # p = "ab"
    #[0,1,2]

    s = "aaaaaaaaaa"
    p = "aaaaaaaaaaaaa"
    #
    # d = {'a':1,"b":1,"c":1}
    # print('d' in d)

    solution = Solution()
    solution.findAnagrams(s,p)