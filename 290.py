class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        sList = s.split(' ')
        if len(pattern) != len(sList):
            return False


        s1 = list()
        s2 = list()
        for i in range(len(pattern)):
            if pattern[i] not in s1 and sList[i] not in s2:
                s1.append(pattern[i])
                s2.append(sList[i])
                # print(s1,s2)
            elif pattern[i] in s1:
                index = s1.index(pattern[i])
                if sList[i] != s2[index]:
                    return False
            elif sList[i] in s2:
                index = s2.index(sList[i])
                if s1[index] != pattern[i]:
                    return False
        return True




if __name__ == '__main__':
    # pattern = "abba"
    # s = "dog cat cat dog"
    #t

    # pattern = "abba"
    # s = "dog cat cat fish"
    #f

    pattern = "aaaa"
    s = "dog cat cat dog"
    #f

    solution = Solution()
    result = solution.wordPattern(pattern,s)
    print(result)