class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        #暴力循环
        # result = []
        # slen = len(s)
        # for i in range(slen):
        #     subs1 = s[i:i+10]
        #     for j in range(i+1,slen):
        #         subs2 = s[j:j+10]
        #         if subs1 == subs2:
        #             result.append(subs1)
        # return list(set(result))

        #哈希表存一下
        result = list()
        sdic = dict()
        slen = len(s)
        for i in range(slen):
            if sdic.get(s[i:i+10]) is None:
                sdic[s[i:i+10]] = 1
            else:
                sdic[s[i:i+10]] += 1

        for key, value in sdic.items():
            if value > 1:
                result.append(key)

        return result






if __name__ == '__main__':
    # s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
    # 输出：["AAAAACCCCC", "CCCCCAAAAA"]

    s = "AAAAAAAAAAAAA"
    # 输出：["AAAAAAAAAA"]

    solution = Solution()
    result = solution.findRepeatedDnaSequences(s)
    print(result)
