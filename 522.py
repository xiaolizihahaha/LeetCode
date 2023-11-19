class Solution(object):
    def findLUSlength(self, strs):
        """
        :type strs: List[str]
        :rtype: int
        """

        strs.sort(key=lambda x:(-len(x),x))
        print(strs)

        maxlength = len(strs[0])



        for index,str in enumerate(strs):
            if len(str) == maxlength:
                sth = strs[:index]
                sth.extend(strs[index+1:])
                if str not in sth:
                    print(maxlength)
                    return maxlength
                else:
                    continue

            else:
                flag = True
                sth = strs[:index]
                sth.extend(strs[index+1:])
                for index1,str1 in enumerate(sth):
                    i = 0
                    j = 0
                    if len(str1) < len(str):
                        continue
                    while j != len(str) and i != len(str1):
                        if str1[i] == str[j]:
                            i += 1
                            j += 1
                        else:
                            i += 1
                    if j == len(str):
                        flag = False
                        break
                if flag is True:
                    print(len(str))
                    return len(str)
        print(-1)
        return -1




if __name__ == '__main__':
    strs = ["aba", "cdc", "eae"]
    # strs = ["aaaa", "aab",'aaa', "aa",'aaab','aaaaa','b','aac']
    # strs = ["aaa", "aaa", "aa"]

    strs = ["j", "j", "viez", "ogk", "ogk", "lfn", "ypmhwx", "ypmhwx", "m", "m", "ak", "ivivzoncju", "ivivzoncju", "wmybi",
     "wmybi", "dyzfjg", "dyzfjg"]
    solution = Solution()
    solution.findLUSlength(strs)